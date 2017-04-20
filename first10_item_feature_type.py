import pandas as pd
from collections import Counter

first10_active_record='jdata_sam/first10_active_record.csv'


product_file='jdata_ori/JData_Product.csv'
first10_item_feature_type='jdata_sam/first10_item_feature_type.csv'


def counter_type(group):
    behavior_type = group.type.astype(int)
    type_cnt=Counter(behavior_type)
    group['browse_num']=type_cnt[1]
    group['addcart_num'] = type_cnt[2]
    group['delcart_num'] = type_cnt[3]
    group['buy_num'] = type_cnt[4]
    group['favor_num'] = type_cnt[5]
    group['click_num'] = type_cnt[6]

    return group[['sku_id', 'browse_num', 'addcart_num',
                  'delcart_num', 'buy_num', 'favor_num',
                  'click_num']]


def statistic_count_action(fname,chunksize=100000):
    reader=pd.read_csv(fname,iterator=True)
    chunks=[]
    loop=True
    while loop:
        try:
            chunk=reader.get_chunk(chunksize)[['sku_id','type']]
            chunks.append(chunk)
        except StopIteration:
            loop=False
            print('Iteration is stopped!')

    df_ac = pd.concat(chunks, ignore_index=True)

    df_ac = df_ac.groupby(['sku_id'], as_index=False).apply(counter_type)
    df_ac = df_ac.drop_duplicates()
    return df_ac


def all_active_data():

    df_ac=statistic_count_action(first10_active_record)

    df_ac['buy_browse_rate']=df_ac['buy_num']/df_ac['browse_num']
    df_ac['buy_addcart_rate'] = df_ac['buy_num'] / df_ac['addcart_num']
    df_ac['buy_favor_rate'] = df_ac['buy_num'] / df_ac['favor_num']
    df_ac['buy_click_rate'] = df_ac['buy_num'] / df_ac['click_num']


    df_ac.ix[df_ac['buy_browse_rate'] > 1.0, 'buy_browse_rate'] = 1
    df_ac.ix[df_ac['buy_addcart_rate'] > 1.0, 'buy_addcart_rate'] = 1
    df_ac.ix[df_ac['buy_favor_rate'] > 1.0, 'buy_favor_rate'] = 1
    df_ac.ix[df_ac['buy_click_rate'] > 1.0, 'buy_click_rate'] = 1

    return df_ac


def get_item_basic_feature():
    df_product=pd.read_csv(product_file)
    return df_product




if __name__ == "__main__":
    product_base=get_item_basic_feature()
    product_act=all_active_data()

    product_feature=pd.merge(product_base,product_act,on=['sku_id'])
    product_feature.to_csv(first10_item_feature_type,index=False)

