import pandas as pd
from sklearn.metrics import classification_report

train_set=pd.read_csv( 'ui_feature_and_flag/test_data_4/train_set.csv')

# 获得训练特征.X代表feature，Y代表flag。
X_train=train_set[['browse_num','addcart_num','delcart_num','buy_num','favor_num','click_num']]
y_train=train_set['buy_or_not']


test_set_feature=pd.read_csv( 'ui_feature_and_flag/test_data_4/test_feature.csv')
X_test=test_set_feature[['browse_num','addcart_num','delcart_num','buy_num','favor_num','click_num']]


#如果是线上测试。则执行15行到26行。
from sklearn.ensemble import GradientBoostingClassifier
gbc =GradientBoostingClassifier()
gbc.fit( X_train, y_train)

gbc_y_predict=gbc.predict(X_test)
gbc_y_predict=pd.DataFrame(gbc_y_predict,columns=['buy_or_not'])
gbc_y_predict['user_id']=test_set_feature['user_id']
gbc_y_predict['sku_id']=test_set_feature['sku_id']
gbc_y_predict=gbc_y_predict[gbc_y_predict['buy_or_not']==1]
gbc_y_predict=gbc_y_predict.drop('buy_or_not',axis=1)

p_subset=pd.read_csv('JData_Product.csv')
gbc_y_predict=pd.merge(gbc_y_predict,p_subset,on=['sku_id'])
gbc_y_predict=gbc_y_predict[['user_id','sku_id']]


gbc_y_predict_grouped=gbc_y_predict.groupby(['user_id'],as_index=False).count()
gbc_y_predict_grouped=gbc_y_predict_grouped[gbc_y_predict_grouped['sku_id']==1]
gbc_y_predict_grouped.columns=['user_id','count']


gbc_y_pred=pd.merge(gbc_y_predict,gbc_y_predict_grouped,on=['user_id'])
gbc_y_pred=gbc_y_pred.drop('count',axis=1)
gbc_y_pred.to_csv('ui_feature_and_flag/predict.csv',encoding='utf-8',index=False)


#如果是线下测试，则执行以下30～72行。
'''
test_set_flag=pd.read_csv( 'ui_feature_and_flag/test_data_3/test_flag.csv')
y_test=test_set_flag[ 'buy_or_not'  ]




from sklearn.tree import DecisionTreeClassifier

dtc=DecisionTreeClassifier() #初始化决策树分类器
dtc.fit(X_train, y_train)
dtc_y_predict=dtc.predict(X_test)



print('Accuracy of DecisionTreeClassifier ',dtc.score(X_test,y_test))
print(classification_report( y_test, dtc_y_predict,  target_names=['not_buy',  'buy' ]))




from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier()
rfc.fit( X_train, y_train )
rfc_y_predict=rfc.predict(  X_test  )



print('Accuracy of RandomForestClassifier ',rfc.score( X_test, y_test  ))
print(classification_report(  y_test,rfc_y_predict ,target_names=['not_buy',  'buy' ]))



from sklearn.ensemble import GradientBoostingClassifier

gbc =GradientBoostingClassifier()
gbc.fit( X_train, y_train)

gbc_y_predict=gbc.predict(X_test)

print('Accuracy of GradientBoostingClassifier ',gbc.score( X_test, y_test  ))
print(classification_report(  y_test,gbc_y_predict ,target_names=['not_buy',  'buy' ]))'''

