import pandas as pd

comment_file='jdata_ori/JData_Comment.csv'
product_file='jdata_ori/JData_Product.csv'
item_feature_commit='jdata_sam/item_feature_commit.csv'


def bad_rate_counter(group):
    avg_bad_com=group['bad_comment_rate'].mean()
    group['avg_bad_com']=avg_bad_com
    return group[['sku_id','avg_bad_com']]


def get_item_com_feature():
    df_com=pd.read_csv(comment_file)
    df_com=df_com.groupby(['sku_id'], as_index=False).apply(bad_rate_counter)
    df_com = df_com.drop_duplicates()
    return df_com


def get_item_basic_feature():
    df_product=pd.read_csv(product_file)
    return df_product


if __name__ == "__main__":
    item_base=get_item_basic_feature()
    item_commit=get_item_com_feature()

    product_feature=pd.merge(item_base,item_commit,on=['sku_id'])
    product_feature.to_csv(item_feature_commit,index=False)

