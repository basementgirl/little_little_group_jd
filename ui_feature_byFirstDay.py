from datetime import timedelta
from datetime import date
from ui_feature import get_ui_feature_each_time
import sys


#控制得到60次训练集特征的总循环
#注意：运行整体代码时应为61.为了避免耗时，先算一次的。

i = sys.argv[1]
i = int(i)

firstDay = date(2016, 1, 31)
firstDay = firstDay + timedelta(1)*i

ui_feature=get_ui_feature_each_time(firstDay)

print('di %d ge training set is done!'%i)

ui_feature.to_csv('ui_feature_and_flag/train_set_%d_ui_feature.csv' % i,index=False)
