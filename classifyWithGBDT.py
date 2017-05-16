import pandas as pd


train_set=pd.read_csv( 'ui_feature_and_flag/test_data_3/train_set.csv')

# 获得训练特征.X代表feature，Y代表flag。
X_train=train_set[['browse_num','addcart_num','delcart_num','buy_num','favor_num','click_num']]
y_train=train_set['buy_or_not']


test_set_feature=pd.read_csv( 'ui_feature_and_flag/test_data_3/test_feature.csv')
X_test=test_set_feature[['browse_num','addcart_num','delcart_num','buy_num','favor_num','click_num']]


test_set_flag=pd.read_csv( 'ui_feature_and_flag/test_data_3/test_flag.csv')
y_test=test_set_flag[ 'buy_or_not'  ]



from sklearn.tree import DecisionTreeClassifier

dtc=DecisionTreeClassifier() #初始化决策树分类器
dtc.fit(X_train, y_train)
y_predict=dtc.predict(X_test)


from sklearn.metrics import classification_report
print('Accuracy of DecisionTreeClassifier ',dtc.score(X_test,y_test))
print(classification_report( y_test, y_predict,  target_names=['not_buy',  'buy' ]))




from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier()
rfc.fit( X_train, y_train )
rfc_y_pred=rfc.predict(  X_test  )



print('Accuracy of RandomForestClassifier ',rfc.score( X_test, y_test  ))
print(classification_report(  y_test,rfc_y_pred ,target_names=['not_buy',  'buy' ]))



from sklearn.ensemble import GradientBoostingClassifier

gbc =GradientBoostingClassifier()
gbc.fit( X_train, y_train)

gbc_y_pred=gbc.predict(X_test)

print('Accuracy of GradientBoostingClassifier ',gbc.score( X_test, y_test  ))
print(classification_report(  y_test,gbc_y_pred ,target_names=['not_buy',  'buy' ]))

