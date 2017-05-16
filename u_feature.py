import pandas as pd
from collections import Counter
from datetime import timedelta


user_file='jdata_ori/JData_User.csv'


def counter_type(group):
    #behavior_type = group.type.astype(int)
    type_cnt=Counter(group['type'])
    group['browse_num']=type_cnt[1]
    group['addcart_num'] = type_cnt[2]
    group['delcart_num'] = type_cnt[3]
    group['buy_num'] = type_cnt[4]
    group['favor_num'] = type_cnt[5]
    group['click_num'] = type_cnt[6]
    group.drop('type', axis=1)
    return group



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


#获取用户基本属性
def get_user_basic_feature():
    df_user=pd.read_csv(user_file,encoding='gbk')
    df_user=df_user[['user_id','age','sex','user_lv_cd','user_reg_tm']]
    df_user['age'] = df_user['age'].map(convert_age)
    return df_user


def get_feature_each_time(firstDay):
    lst=[]
    for i in range(10):
        current_date=firstDay + timedelta(1) * i
        current_date=current_date.strftime('%Y-%m-%d')

        df=pd.read_csv('actionSplitByDay/JData_Action_'+current_date+'.csv')
        df=df[['user_id','type']]
        lst.append(df)
        print('a file had been load!')

    df_ac = pd.concat(lst, ignore_index=True)
    print('cancat done!')
    df_ac = df_ac.groupby(['user_id'], as_index=False).apply(counter_type)
    df_ac=df_ac.drop_duplicates()
    print('ui feature of a training set had been done!')

    return df_ac


