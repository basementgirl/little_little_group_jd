import pandas as pd
from collections import Counter
import datetime as dt
import time


first10_active_record_file='jdata_sam/first10_active_record.csv'
first10_ui_type_feature_file='jdata_sam/first10_ui_type_feature.csv'

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


#统计每个用户的行为数据
def statistic_count_action(fname,chunksize=100000):
    reader=pd.read_csv(fname,iterator=True)
    chunks=[]
    loop=True
    while loop:
        try:
            chunk=reader.get_chunk(chunksize)[['user_id','sku_id','type']]
            chunks.append(chunk)
        except StopIteration:
            loop=False
            print('Iteration is stopped!')

    df_ac=pd.concat(chunks,ignore_index=True)

    df_ac = df_ac.groupby(['user_id','sku_id'], as_index=False).apply(counter_type)

    df_ac=df_ac.drop_duplicates()

    return df_ac


if __name__=="__main__":
    user_item_feature=statistic_count_action(first10_active_record_file)
    user_item_feature.to_csv(first10_ui_type_feature_file,index=False)


