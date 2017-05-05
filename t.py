import pandas as pd

df=pd.read_csv('ui_feature_and_flag/ui_train_set_5.csv')
df[['user_id','sku_id','buy_or_not']].to_csv('ui_feature_and_flag/test_flag.csv',index=False)
df=df.drop('buy_or_not',axis=1)
df.to_csv('ui_feature_and_flag/test_feature.csv',index=False)
