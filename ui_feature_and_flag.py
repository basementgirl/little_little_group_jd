import pandas as pd


ui_feature_file='ui_feature_and_flag/train_set_1_ui_feature.csv'
ui_flag_file='ui_feature_and_flag/train_set_1_ui_flag.csv'

ui_feature=pd.read_csv(ui_feature_file)
ui_flag=pd.read_csv(ui_flag_file)

ui_train_set=pd.merge(ui_feature,ui_flag,on=['user_id','sku_id'],how='left')
_ = ui_train_set.fillna(0,inplace=True)
ui_train_set.to_csv('ui_feature_and_flag/ui_train_set_1.csv',index=False)


