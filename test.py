
import pandas as pd
comment_file='jdata_ori/JData_Comment.csv'


def bad_rate_counter(group):
    avg_bad_com=group['bad_comment_rate'].mean()
    group['avg_bad_com']=avg_bad_com
    return group[['sku_id','avg_bad_com']]

def get_item_com_feature():
    df_com=pd.read_csv(comment_file)
    df_com=df_com.groupby(['sku_id'], as_index=False).apply(bad_rate_counter)
    df_com=df_com.drop_duplicates()
    return df_com

print(get_item_com_feature())