import pandas as pd

lst=[]
for i in range(1,5):
    a=pd.read_csv('ui_feature_and_flag/ui_train_set_%d.csv'%i)
    lst.append(a)
    df=pd.concat(lst,ignore_index=True)
df.to_csv('ui_feature_and_flag/train_set.csv',index=False)


