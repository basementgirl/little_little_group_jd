import pandas as pd
for i in range(57,61):
    df_feature=pd.read_csv('ui_feature_and_flag/train_set_%d_ui_feature.csv'%i)
    df_flag=pd.read_csv('ui_feature_and_flag/train_set_%d_ui_flag.csv'%i)
    df=pd.merge(df_feature,df_flag,on=['user_id','sku_id'],how='inner')
    df.to_csv('ui_feature_and_flag/train_set_%d.csv'%i,index=False)

