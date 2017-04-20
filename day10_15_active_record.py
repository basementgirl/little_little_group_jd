import pandas as pd
import time


action_2016_02_file='jdata_sam/JData_Action_201602.csv'
'''action_2016_03_file='jdata_sam/JData_Action_201603.csv'
action_2016_04_file='jdata_sam/JData_Action_201604.csv'''''
day10_15_active_record_file='jdata_sam/day10_15_active_record.csv'



def statistic_count_action(fname,chunksize=100000):
    reader=pd.read_csv(fname,iterator=True)
    chunks=[]
    loop=True
    while loop:
        try:
            chunk=reader.get_chunk(chunksize)
            chunks.append(chunk)
        except StopIteration:
            loop=False
            print('Iteration is stopped!')

    df_ac=pd.concat(chunks,ignore_index=True)
    a = "2016-2-11 00:00:00"
    b = "2016-2-16 00:00:00"

    # 将其转换为时间数组
    timeArraya = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    timeArrayb = time.strptime(b, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    Stampa = int(time.mktime(timeArraya))
    Stampb = int(time.mktime(timeArrayb))

    ls = []
    for i in df_ac['time'].values:
        timeArray = time.strptime(i, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        ls.append(timeStamp)

    df_ac['timestamp'] = ls

    df_ac = df_ac[Stampa < df_ac['timestamp']]
    df_ac = df_ac[df_ac['timestamp'] < Stampb]
    df_ac=df_ac.drop_duplicates()

    return df_ac



def all_active_data():
    lst=[]
    lst.append(statistic_count_action(action_2016_02_file))
    '''lst.append(statistic_count_action(action_2016_03_file))
    lst.append(statistic_count_action(action_2016_04_file))'''

    df_ac=pd.concat(lst,ignore_index=True)

    return df_ac


if __name__=="__main__":
    day10_15_active_record=all_active_data()
    day10_15_active_record.to_csv(day10_15_active_record_file,index=False)



