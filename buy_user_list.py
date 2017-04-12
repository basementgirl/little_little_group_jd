import pandas as pd


action_2016_02_file='jdata_sam/JData_Action_201602.csv'
action_2016_03_file='jdata_sam/JData_Action_201603.csv'
action_2016_04_file='jdata_sam/JData_Action_201604.csv'
comment_file='jdata_ori/JData_Comment.csv'
product_file='jdata_ori/JData_Product.csv'

user_feature='jdata_sam/user_feature.csv'

#comment_file='jdata_ori/JData_Comment.csv'
product_feature_file='jdata_sam/product_feature.csv'
buy_user_list_file='jdata_sam/buy_user_list.csv'


#　在一个文件中寻找有购买记录的用户－商品对
def buy_user_in_batch_data(fname, chunk_size=100000):
    reader = pd.read_csv(fname, header=0, iterator=True)
    chunks = []
    loop = True
    while loop:
        try:
            chunk = reader.get_chunk(chunk_size)[
                ["user_id", "sku_id", "type"]]
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped")

    df_ac = pd.concat(chunks, ignore_index=True)

    # type = 4, 购买
    df_ac = df_ac[df_ac['type'] == 4]

    return df_ac[['user_id','type']]



# 找出有购买记录的用户.
def find_buy_user():
    df_ac = []
    df_ac.append(buy_user_in_batch_data(fname=action_2016_02_file))
    df_ac.append(buy_user_in_batch_data(fname=action_2016_03_file))
    df_ac.append(buy_user_in_batch_data(fname=action_2016_04_file))

    # 将多个子记录合并成一个dataframe
    df_ac = pd.concat(df_ac, ignore_index=True)
    # 将重复的用户丢弃
    df_ac = df_ac.drop_duplicates()
    # 写入文件
    return df_ac


def get_user_feature():
    buy_user_feature=pd.read_csv(user_feature)
    return buy_user_feature

if __name__=="__main__":

    user_list=find_buy_user()
    buy_user_features=get_user_feature()

    user_who_buy=pd.merge(user_list, buy_user_features, on=['user_id'], how='left')
    user_who_buy=user_who_buy.drop_duplicates()
    user_who_buy.to_csv(buy_user_list_file,index=False)












