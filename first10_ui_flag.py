import pandas as pd
from collections import Counter


first10_active_record_file='jdata_sam/first10_active_record.csv'
day10_15_active_record_file='jdata_sam/day10_15_active_record.csv'
ui_pair_flag_file='jdata_sam/ui_pair_flag.csv'

#每个用户六种行为统计
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


def get_first10_ui_pair():
    df_ac=pd.read_csv(first10_active_record_file)
    df_ac=df_ac[['user_id','sku_id']]
    return df_ac


def ui_pair_day10_15_record():
    ui_pair=get_first10_ui_pair()
    df_ac=pd.read_csv(day10_15_active_record_file)
    df = []
    for index, row in ui_pair.iterrows():
        usr_id = row["user_id"]
        sku_id = row["sku_id"]

        # find U-I related record
        df.append(df_ac[(df_ac["user_id"] == usr_id) &
                        (df_ac["sku_id"] == sku_id)])

    df = pd.concat(df, ignore_index=True)

    df = df.groupby(['user_id', 'sku_id'], as_index=False).apply(counter_type)

    return df




def ui_pair_flag():
    df=ui_pair_day10_15_record()
    #买设为标志1，不买为0.
    if df['buy_num']>0:
        df['buy_or_not']=1
    else:
        df['buy_or_not']=0
    return df[['user_id','sku_id','buy_or_not']]


if __name__=="__main__":
    ui_pair_flag=ui_pair_flag()
    ui_pair_flag.to_csv(ui_pair_flag_file,index=False)




