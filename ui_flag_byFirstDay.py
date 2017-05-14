from datetime import timedelta
from datetime import date
from ui_flag import get_ui_flag_each_time
import sys


i = sys.argv[1]
i = int(i)

firstDay = date(2016, 1, 31)
firstDay = firstDay + timedelta(1)*i

ui_flag = get_ui_flag_each_time(i,firstDay)

print('di %d ge training set is done!'%i)

ui_flag.to_csv('ui_feature_and_flag/train_set_%d_ui_flag.csv' % i,index=False)
