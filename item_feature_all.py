import pandas as pd

item_feature_type='jdata_sam/item_feature_type.csv'
item_feature_comment='jdata_sam/item_feature_comment.csv'
item_feature_all='jdata_sam/item_feature_all.csv'

df_item_feature_type=pd.read_csv(item_feature_type)
df_item_feature_comment=pd.read_csv(item_feature_comment)
df_item_feature_comment=df_item_feature_comment.drop(['a1','a2','a3','cate','brand'],axis=1)

df_item_feature=pd.merge(df_item_feature_type,df_item_feature_comment,on='sku_id')
df_item_feature.to_csv(item_feature_all,index=False)
