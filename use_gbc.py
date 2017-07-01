# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:51:46 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:09:28 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:10:34 2017

@author: Administrator

使用 randomforest 预测结果
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from pandas import Series,DataFrame
#%%
train_set=pd.read_csv('ui_feature_and_flag/test_data_4/train_set.csv')

X_train=train_set.ix[:,2:train_set.shape[1]-1]
y_train=train_set['buy_or_not']

test_set=pd.read_csv('ui_feature_and_flag/test_data_4/test_set_feature.csv')

X_test=test_set.ix[:,2:train_set.shape[1]]


#%%
gbc=GradientBoostingClassifier()
gbc.fit(X_train,y_train)

#%%
#得到预测结果，只有2385个1
gbc_y_pred=gbc.predict(X_test)




#%%
d_gbc_y_pred=DataFrame(gbc_y_pred)

#%%

#%%

us_pair=test_set[['user_id','sku_id']]

#横向拼接
us_pred=pd.concat([us_pair, d_gbc_y_pred],axis=1)

#%%
us_select=us_pred[us_pred[0]==1]
#%%
#下面对user去重
us_select = us_select.drop_duplicates('user_id')


#%%
    #最后得到去重后的结果 us3
us3=us_select.astype(np.int)

del us3[0]

p_subset=pd.read_csv('JData_Product.csv')
gbc_y_predict=pd.merge(us3,p_subset,on=['sku_id'])
gbc_y_predict=gbc_y_predict[['user_id','sku_id']]

#%% 输出结果为 csv 文件
gbc_y_predict.to_csv('result_gbc.csv',index=None)


