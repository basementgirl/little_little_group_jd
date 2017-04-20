import pandas as pd
from collections import Counter


first10_active_record='jdata_sam/first10_active_record.csv'
user_file='jdata_ori/JData_User.csv'

first10_user_feature_cate='jdata_sam/first10_user_feature_cate.csv'


def counter_cate(group):
    cate_cnt = Counter(group['cate'])
    for i in cate_cnt:
        group['num_of_cate_%u' % int(i)] = cate_cnt[i]
    group = group.drop('cate', axis=1)
    return group

#统计每个用户的行为数据
def statistic_count_action(fname,chunksize=100000):
    reader=pd.read_csv(fname,iterator=True)
    chunks=[]
    loop=True
    while loop:
        try:
            chunk=reader.get_chunk(chunksize)[['user_id','cate']]
            chunks.append(chunk)
        except StopIteration:
            loop=False
            print('Iteration is stopped!')

    df_ac=pd.concat(chunks,ignore_index=True)

    df_ac = df_ac.groupby(['user_id'], as_index=False).apply(counter_cate)

    df_ac=df_ac.drop_duplicates()
    return df_ac

 #合并月份数据。
def all_active_data():
    df_ac = statistic_count_action(first10_active_record)

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
    all_user_feature=pd.merge(user_basic,user_active,on=['user_id'])
    all_user_feature.to_csv(first10_user_feature_cate,index=False)













