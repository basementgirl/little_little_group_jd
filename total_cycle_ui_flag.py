from datetime import timedelta
from datetime import date
from ui_flag import get_ui_flag_each_time


#控制得到60次训练集flag的总循环
j = 1
firstDay = date(2016, 3, 11)
while j < 2:
    ui_flag = get_ui_flag_each_time(j,firstDay)
    firstDay = firstDay + timedelta(1)
    print('di %d ge training set is done!' % j)
    ui_flag.to_csv('ui_feature_and_flag/train_set_%d_ui_flag.csv' % j)
    j+=1

