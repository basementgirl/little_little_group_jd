import pandas as pd
from collections import Counter
from datetime import date


ui_feature_file='ui_feature_and_flag/train_set_i_ui_feature.csv'
train_set_flag_file='ui_feature_and_flag/the_1_ui_pair_flag.csv'


#每个用户六种行为统计git
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


def flag_record():
    firstDay = date(2016,2,11)
    secondDay = date(2016,2,12)
    delta = secondDay - firstDay
    lst=[]
    for i in range(5):
        current_date=firstDay + delta * i
        current_date=current_date.strftime('%Y-%m-%d')
        df=pd.read_csv('actionSplitByDay/JData_Action_'+current_date+'.csv')
        lst.append(df)
        print('done 1 times!')
    df_ac = pd.concat(lst, ignore_index=True)
    return df_ac


def get_first10_ui_pair():
    df_ac=pd.read_csv(the_1_ui_feature_file)
    df_ac=df_ac[['user_id','sku_id']]
    return df_ac


def ui_pair_day10_15_record():
    ui_pair=get_first10_ui_pair()
    df_ac=flag_record()
    df = []
    for index, row in ui_pair.iterrows():
        usr_id = row["user_id"]
        sku_id = row["sku_id"]
        # find U-I related record
        df.append(df_ac[(df_ac["user_id"] == usr_id) &
                        (df_ac["sku_id"] == sku_id)])
    df = pd.concat(df, ignore_index=True)
    df = df.groupby(['user_id', 'sku_id'], as_index=False).apply(counter_type)
    print('iteration done!')
    return df


def ui_pair_flag():
    print("begin ui_pair_day10_15_record()")
    df=ui_pair_day10_15_record()
    print("end ui_pair_day10_15_record()")

    #买设为标志1，不买为0.
    df.ix[df['buy_num']>0,'buy_or_not']=1
    df.ix[df['buy_num'] == 0, 'buy_or_not'] = 0

    return df


if __name__=="__main__":
    print("begin ui_pair_flag()")
    ui_pair_flag=ui_pair_flag()
    print("end ui_pair_flag()")

    ui_pair_flag.to_csv(ui_pair_flag_file,index=False)




