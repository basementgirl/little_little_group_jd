# _*_ coding=utf-8 _*_

import pandas as pd
from collections import Counter


action_2016_02_file='jdata_sam/JData_Action_201602.csv'
action_2016_03_file='jdata_sam/JData_Action_201603.csv'
action_2016_04_file='jdata_sam/JData_Action_201604.csv'
user_feature='jdata_sam/user_feature.csv'
not_buy_user_list_file='jdata_sam/not_buy_user_list.csv'


def judgeBuy(group):
    behavior_type = group.type.astype(int)
    type_cnt = Counter(behavior_type)

    group['count4'] = type_cnt[4]
    return group


def buy_user_in_batch_data(fname, chunk_size=100000):
    reader = pd.read_csv(fname, header=0, iterator=True)
    chunks = []
    loop = True
    while loop:
        try:
            chunk = reader.get_chunk(chunk_size)[
                ["user_id", "type"]]
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped")

    df_ac = pd.concat(chunks, ignore_index=True)

    return df_ac



# 找出有购买记录的用户.
def find_not_buy_user():
    df_ac = []
    df_ac.append(buy_user_in_batch_data(fname=action_2016_02_file))
    df_ac.append(buy_user_in_batch_data(fname=action_2016_03_file))
    df_ac.append(buy_user_in_batch_data(fname=action_2016_04_file))

    # 将多个子记录合并成一个dataframe
    df_ac = pd.concat(df_ac, ignore_index=True)

    df_ac = df_ac.groupby(['user_id'], as_index=False).apply(judgeBuy)
    df_ac = df_ac[df_ac['count4']==0]

    #df_ac = df_ac['user_id',]

    # 将重复的用户－商品对丢弃
    df_ac = df_ac.drop_duplicates()

    # 写入文件
    return df_ac

def get_user_feature():
    buy_user_feature=pd.read_csv(user_feature)
    return buy_user_feature



if __name__=="__main__":
    user_list = find_not_buy_user()
    not_buy_user_features = get_user_feature()

    user_who_not_buy = pd.merge(user_list, not_buy_user_features, on=['user_id'], how='left')
    user_who_not_buy = user_who_not_buy.drop_duplicates()
    user_who_not_buy.to_csv(not_buy_user_list_file, index=False)