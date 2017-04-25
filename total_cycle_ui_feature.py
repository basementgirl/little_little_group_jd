from datetime import timedelta
from datetime import date
from ui_feature import get_ui_feature_each_time


#控制得到60次训练集特征的总循环
#注意：运行整体代码时应为61.为了避免耗时，先算一次的。

i = 1
firstDay = date(2016, 3, 1)
while i<2:
    ui_feature=get_ui_feature_each_time(firstDay)
    firstDay=firstDay+timedelta(1)
    print('di %d ge training set is done!'%i)
    ui_feature.to_csv('ui_feature_and_flag/train_set_%d_ui_feature.csv' % i)
    i+=1

















