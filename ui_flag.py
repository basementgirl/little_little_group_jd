import pandas as pd
from collections import Counter
from datetime import timedelta


#每个用户六种行为统计.
def counter_type(group):
    type_cnt=Counter(group['type'])
    group['browse_num']=type_cnt[1]
    group['addcart_num'] = type_cnt[2]
    group['delcart_num'] = type_cnt[3]
    group['buy_num'] = type_cnt[4]
    group['favor_num'] = type_cnt[5]
    group['click_num'] = type_cnt[6]
    group = group.drop('type', axis=1)
    return group


#每个训练集的初始targe日期区间内所有的记录。
def init_flag_records(firstDay):
    lst=[]
    for i in range(5):
        current_date=firstDay + timedelta(1) * i
        current_date=current_date.strftime('%Y-%m-%d')
        df=pd.read_csv('actionSplitByDay/JData_Action_'+current_date+'.csv')
        df=df[['user_id','sku_id','type']]
        lst.append(df)
        print('done 1 times!')
    df_ac = pd.concat(lst, ignore_index=True)
    return df_ac


# 得到每个训练集的特征记录中的用户商品对。
def ui_pair_feature_records(j):
    df_ac=pd.read_csv('ui_feature_and_flag/train_set_%d_ui_feature.csv'%j)
    df_ac=df_ac[['user_id','sku_id']]
    return df_ac


#得到每个训练集中有特征的用户商品在未来5天内flag。
def ui_pair_flag_records(j,firstDay):
    ui_pair=ui_pair_feature_records(j)
    df_ac=init_flag_records(firstDay)
    df = []
    for index, row in ui_pair.iterrows():
        usr_id = row["user_id"]
        sku_id = row["sku_id"]
        # find U-I related record
        df.append(df_ac[(df_ac["user_id"] == usr_id) &
                        (df_ac["sku_id"] == sku_id)])
    df = pd.concat(df, ignore_index=True)
    df = df.groupby(['user_id', 'sku_id'], as_index=False).apply(counter_type)
    df = df.drop_duplicates()
    print('iteration done!')
    return df


#得到flag。
def get_ui_flag_each_time(j,firstDay):
    df=ui_pair_flag_records(j,firstDay)

    #买设为标志1，不买为0.
    df.ix[df['buy_num']>0,'buy_or_not']=1
    df.ix[df['buy_num'] == 0, 'buy_or_not'] = 0

    return df[['user_id','sku_id','buy_or_not']]







