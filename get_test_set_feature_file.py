import pandas as pd


ui_feature_file='ui_feature_and_flag/train_set_61_ui_feature.csv'
ui_flag_file='ui_feature_and_flag/train_set_61_ui_flag.csv'

ui_feature=pd.read_csv(ui_feature_file)
ui_flag=pd.read_csv(ui_flag_file)

ui_test_set=pd.merge(ui_feature,ui_flag,on=['user_id','sku_id'])

ui_test_set=ui_test_set.drop('buy_or_not',axis=1)
ui_test_set.to_csv('ui_feature_and_flag/ui_test_set_61.csv',index=False)



