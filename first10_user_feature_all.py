import pandas as pd

user_feature_type='jdata_sam/first10_user_feature_type.csv'
user_feature_cate='jdata_sam/first10_user_feature_cate.csv'
user_feature_all='jdata_sam/first10_user_feature_all.csv'

df_user_feature_type=pd.read_csv(user_feature_type)
df_user_feature_cate=pd.read_csv(user_feature_cate)
df_user_feature_cate=df_user_feature_cate.drop(['age','sex','user_lv_cd','user_reg_tm'],axis=1)

df_user_feature=pd.merge(df_user_feature_type,df_user_feature_cate,on='user_id')
df_user_feature.to_csv(user_feature_all,index=False)

