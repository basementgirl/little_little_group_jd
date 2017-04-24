from datetime import timedelta
from datetime import date
from ui_feature import get_feature_each_time
from ui_flag import get_flag_each_time


#控制得到60次训练集特征的总循环
def get_60_train_set_feature():
    i=1
    firstDay= date(2016,2,1)
    #注意：运行整体代码时应为61.为了避免耗时，先算一次的。
    while i<2:
        ui_feature=get_feature_each_time(firstDay)
        firstDay=firstDay+timedelta(1)
        print('di %d ge training set is done!'%i)
        ui_feature.to_csv('ui_feature_and_flag/train_set_%d_ui_feature'%i)


#控制得到60次训练集flag的总循环
def get_60_train_set_flag():
    j = 1
    firstDay = date(2016, 2, 11)
    while j < 2:
        ui_flag = get_flag_each_time(j,firstDay)
        firstDay = firstDay + timedelta(1)
        print('di %d ge training set is done!' % j)
        ui_flag.to_csv('ui_feature_and_flag/train_set_%d_ui_flag' % j)


if __name__=="__main__":
    get_60_train_set_feature()
    get_60_train_set_flag()





