import pandas as pd


ui_feature_file='ui_feature_and_flag/train_set_2_ui_feature.csv'
ui_flag_file='ui_feature_and_flag/train_set_2_ui_flag.csv'

ui_feature=pd.read_csv(ui_feature_file)
ui_flag=pd.read_csv(ui_flag_file)

ui_train_set=pd.merge(ui_feature,ui_flag,on=['user_id','sku_id'],how='left')
#_ = ui_train_set.fillna(0,inplace=True)
#ui_train_set=ui_train_set.dropna()
#ui_train_set=ui_train_set.drop('buy_or_not',axis=1)
ui_train_set.to_csv('ui_feature_and_flag/simple_version_ui_train_set_2.csv',index=False)


