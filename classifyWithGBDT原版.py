
# coding: utf-8

#导入训练集

import pandas as pd
import numpy as np

train_set=pd.read_csv( 'ui_feature_and_flag/offline_train_set.csv')

# ## 查看dataframe信息用 .info()

#train_set.info()


#对dataframe的索引，用ix索引字段
# 获得训练特征.X代表feature，Y代表flag。
X_train=train_set.ix[ : , 2:train_set.shape[1]-1]
y_train=train_set['buy_or_not']

#用 ix 直接获得dataframe的某个元素/某些行和列区域

#print(X_train.ix[1,'browse_num'])

#print(X_train.ix[1,'browse_num']==X_train.ix[2,'browse_num'], '\n')

#X_train.ix[1:2 ]

#X_train[:2]


# In[219]:

'''
检查：在训练集中有多少与第0行特征取值相同的样本？
            这些样本又有多少的标记为1？
            
            kk为与第0行特征取值相同的样本数量；
            same_feature_index存放这些样本的索引；
            same_label_1_index存放这些样本中标记为1的索引
'''

#tic()

'''
'''
kk=0
same_feature_index=[]
same_label_1_index=[]

for i in range(X_train.shape[0]):
    if (X_train.ix[0]==X_train.ix[i]).all():
        kk+=1
        same_feature_index.append(i)
        
        if y_train[i]==1:
            same_label_1_index.append(i)
        
#toc()
print(kk)
print(i)
print(same_feature_index)
print(same_label_1_index)

'''

# In[252]:

#X_train.ix[0]


# ## 获得训练集标记 y_train

# In[218]:




# In[43]:

'''
'''# 训练集中 不买的是买的 63倍
print(len(y_train[y_train==0]))
print(len(y_train[y_train==1]))

# In[210]:

#y_train.values


# In[214]:

#y_train[18610]


# # 导入测试集的特征 X_test

# In[22]:

test_set_feature=pd.read_csv( 'D:/Jupyter/python数据分析和京东竞赛/京东竞赛/20170426_test/test_set_feature_2.csv')
#test_set_feature


# In[53]:

#test_set_feature.info()


# In[97]:

X_test=test_set_feature.ix[:, 2: test_set_feature.shape[1]]
#X_test


# In[160]:

#X_t1=X_test.ix[ [2,4,6], [1,3,5] ]
#X_t1


# # 导入测试集的label y_test

# In[34]:

test_set_flag=pd.read_csv( 'D:/Jupyter/python数据分析和京东竞赛/京东竞赛/20170426_test/test_set_flag_2.csv')
#test_set_flag


# ## 用Series的map方法实现类型转换

# In[68]:

#y_test=test_set_flag['buy_or_not'].map(lambda x:int(x))
#y_test


# ## 用Series/DataFrame的astype方法

# In[92]:

y_test=test_set_flag[ 'buy_or_not'  ].astype(np.int64)
#y_test


# In[94]:

print(len(y_test[ y_test==0]))
print(len(y_test[y_test==1]))


# # 决策树模型

# In[98]:

import time


# ## t1为开始时刻

# In[99]:

t1=time.clock()


# ## 使用训练数据进行模型学习

# In[111]:

from sklearn.tree import DecisionTreeClassifier

dtc=DecisionTreeClassifier() #初始化决策树分类器
dtc.fit(X_train, y_train)


# ## 输出预测的准确性

# In[124]:

print(  dtc.score( X_test, y_test  )   )
print(  dtc.score( X_train, y_train  )   )


# In[123]:

X_train


# ## 预测结果 y_predict

# In[257]:

y_predict=dtc.predict(X_test)
#y_predict=dtc.predict(X_train)


# In[258]:

y_predict


# In[259]:

print(y_predict[y_predict==0].shape)
print(y_predict[y_predict==1].shape)


# In[260]:

#np.savetxt('y_predict.csv', y_predict,fmt='%d', delimiter=','  )

len(y_predict[y_predict==1])


# ## 输出更详细的分类报告

# In[144]:

from sklearn.metrics import classification_report
print(  classification_report( y_test, y_predict,  target_names=['not_buy',  'buy' ]   )   )

#print(  classification_report( y_train, y_predict,  target_names=['not_buy',  'buy' ]   )   )print(  classification_report( y_train, y_predict,  target_names=['not_buy',  'buy' ]   )   )


# ## 打印程序运行时长

# In[117]:

print( 'time is %.8f' %(time.clock()-t1) )


# # 随机森林分类器

# In[145]:

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier()
rfc.fit( X_train, y_train )
rfc_y_pred=rfc.predict(  X_test  )


# In[146]:

rfc.score( X_test, y_test  )


# In[149]:

print(classification_report(  y_test,rfc_y_pred   ))


# # 梯度提升分类器

# In[150]:

from sklearn.ensemble import GradientBoostingClassifier

gbc =GradientBoostingClassifier()
gbc.fit( X_train, y_train)

gbc_y_pred=gbc.predict(X_test)


# In[151]:

gbc.score( X_test, y_test  )


# In[152]:

print(classification_report(  y_test,gbc_y_pred   ))'''

