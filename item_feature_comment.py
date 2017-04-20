import pandas as pd

comment_file='jdata_ori/JData_Comment.csv'
product_file='jdata_ori/JData_Product.csv'
first10_item_feature_comment='jdata_sam/first10_item_feature_comment.csv'


def get_item_com_feature():
    df_com=pd.read_csv(comment_file)
    df_com=df_com[['sku_id','bad_comment_rate']]
    df_com=df_com.groupby(['sku_id'], as_index=False).mean()
    df_com = df_com.drop_duplicates()
    return df_com

def get_item_basic_feature():
    df_product=pd.read_csv(product_file)
    return df_product


if __name__ == "__main__":
    item_base=get_item_basic_feature()
    item_commit=get_item_com_feature()

    product_feature=pd.merge(item_base,item_commit,on=['sku_id'])
    product_feature.to_csv(first10_item_feature_comment,index=False)

