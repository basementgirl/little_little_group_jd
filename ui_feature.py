import pandas as pd
from datetime import date
from collections import Counter
from datetime import timedelta

the_1_feature_file='ui_feature_and_flag/the_1_feature.csv'


def counter_type(group):
    type_cnt=Counter(group['type'])
    group['browse_num']=type_cnt[1]
    group['addcart_num'] = type_cnt[2]
    group['delcart_num'] = type_cnt[3]
    group['buy_num'] = type_cnt[4]
    group['favor_num'] = type_cnt[5]
    group['click_num'] = type_cnt[6]

    group = group.drop('type', axis=1)
    return group


def get_feature_each_time(firstDay):

    lst=[]
    for i in range(10):
        current_date=firstDay + timedelta(1) * i
        current_date=current_date.strftime('%Y-%m-%d')

        df=pd.read_csv('actionSplitByDay/JData_Action_'+current_date+'.csv')
        lst.append(df)
        print('a file had been load!')

    df_ac = pd.concat(lst, ignore_index=True)
    print('cancat done!')
    df_ac = df_ac.groupby(['user_id','sku_id'], as_index=False).apply(counter_type)
    print('ui feature of a training set had been done!')

    return df_ac


'''
if __name__=="__main__":
    the_1_feature=get_feature_each_time()
    the_1_feature.to_csv(the_1_feature_file,index=False)'''

