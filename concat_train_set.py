import pandas as pd
lst=[]
for i in range(57,62):
    df=pd.read_csv('ui_feature_and_flag/train_set_%d.csv'%i)
    lst.append(df)
offline_train=pd.concat(lst,ignore_index=True)
offline_train.to_csv('ui_feature_and_flag/online_train_set.csv',index=False)

