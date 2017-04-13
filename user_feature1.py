import pandas as pd
from collections import Counter


action_2016_02_file='jdata_sam/JData_Action_201602.csv'
action_2016_03_file='jdata_sam/JData_Action_201603.csv'
action_2016_04_file='jdata_sam/JData_Action_201604.csv'
user_file='jdata_ori/JData_User.csv'

user_feature1='jdata_sam/user_feature1.csv'


#每个用户六种行为统计
def counter_type(group):
    #behavior_type = group.type.astype(int)
    type_cnt=Counter(group['type'])
    group['browse_num']=type_cnt[1]
    group['addcart_num'] = type_cnt[2]
    group['delcart_num'] = type_cnt[3]
    group['buy_num'] = type_cnt[4]
    group['favor_num'] = type_cnt[5]
    group['click_num'] = type_cnt[6]
    group = group.drop('type', axis=1)
    return group

#统计每个用户的行为数据
def statistic_count_action(fname,chunksize=100000):
    reader=pd.read_csv(fname,iterator=True)
    chunks=[]
    loop=True
    while loop:
        try:
            chunk=reader.get_chunk(chunksize)[['user_id','sku_id','type','cate']]
            chunks.append(chunk)
        except StopIteration:
            loop=False
            print('Iteration is stopped!')

    df_ac=pd.concat(chunks,ignore_index=True)

    df_ac1 = df_ac.groupby(['user_id'], as_index=False).apply(counter_type)

    df_ac1=df_ac1.drop_duplicates()
    return df_ac1

#合并月份数据。
def all_active_data():
    lst=[]
    lst.append(statistic_count_action(action_2016_02_file))
    lst.append(statistic_count_action(action_2016_03_file))
    lst.append(statistic_count_action(action_2016_04_file))

    df_ac=pd.concat(lst,ignore_index=True)

    df_ac=df_ac.groupby(['user_id'],as_index=False).sum()


    df_ac['buy_browse_rate']=df_ac['buy_num']/df_ac['browse_num']
    df_ac['buy_addcart_rate'] = df_ac['buy_num'] / df_ac['addcart_num']
    df_ac['buy_favor_rate'] = df_ac['buy_num'] / df_ac['favor_num']
    df_ac['buy_click_rate'] = df_ac['buy_num'] / df_ac['click_num']


    df_ac.ix[df_ac['buy_browse_rate']>1.0,'buy_browse_rate']=1
    df_ac.ix[df_ac['buy_addcart_rate'] > 1.0, 'buy_addcart_rate'] = 1
    df_ac.ix[df_ac['buy_favor_rate'] > 1.0, 'buy_favor_rate'] = 1
    df_ac.ix[df_ac['buy_click_rate'] > 1.0, 'buy_click_rate'] = 1

    return df_ac


#获取用户基本属性
def get_user_basic_feature():
    df_user=pd.read_csv(user_file,encoding='gbk')
    df_user=df_user[['user_id','age','sex','user_lv_cd','user_reg_tm']]
    df_user['age'] = df_user['age'].map(convert_age)
    return df_user


#对年龄这一列进行处理。
def convert_age(age_str):
    if age_str == u'-1':
        return -1
    elif age_str == u'15岁以下':
        return 0
    elif age_str == u'16-25岁':
        return 1
    elif age_str == u'26-35岁':
        return 2
    elif age_str == u'36-45岁':
        return 3
    elif age_str == u'46-55岁':
        return 4
    elif age_str == u'56岁以上':
        return 5
    else:
        return -1



if __name__=="__main__":
    user_basic=get_user_basic_feature()
    user_active=all_active_data()

    all_user_feature=pd.merge(user_basic,user_active,on=['user_id'],how='left')
    all_user_feature =all_user_feature.dropna()
    all_user_feature.drop(all_user_feature[(all_user_feature['buy_num'] < 1) & (all_user_feature['browse_num'] > 1000)], axis=1)
    all_user_feature.to_csv(user_feature1,index=False)













