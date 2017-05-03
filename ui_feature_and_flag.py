import pandas as pd
k=3
while k<4:
    ui_feature_file='ui_feature_and_flag/train_set_%d_ui_feature.csv'%k
    ui_flag_file='ui_feature_and_flag/train_set_%d_ui_flag.csv'%k

    ui_feature=pd.read_csv(ui_feature_file)
    ui_flag=pd.read_csv(ui_flag_file)

    ui_train_set=pd.merge(ui_feature,ui_flag,on=['user_id','sku_id'])
    #_ = ui_train_set.fillna(0,inplace=True)
    #ui_train_set=ui_train_set.dropna()
    #ui_train_set=ui_train_set.drop('buy_or_not',axis=1)
    ui_train_set.to_csv('ui_feature_and_flag/ui_train_set_%d.csv'%k,index=False)
    k+=1


