import pandas as pd
from collections import Counter
from datetime import timedelta
from datetime import date
from ui_feature import get_feature_each_time



def get_66_times():
    i=1
    firstDay= date(2016,2,1)
    while i<67:
        ui_feature=get_feature_each_time(firstDay)
        firstDay=firstDay+timedelta(1)
        print('di %d ge training set is done!'%i)
        ui_feature.to_csv('ui_feature_and_flag/train_set_%d_ui_feature'%i)


if __name__=="__main__":
    get_66_times()





