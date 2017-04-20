import pandas as pd
from collections import Counter


action_2016_02_file='jdata_sam/JData_Action_201602.csv'
action_2016_03_file='jdata_sam/JData_Action_201603.csv'
action_2016_04_file='jdata_sam/JData_Action_201604.csv'
comment_file='jdata_ori/JData_Comment.csv'
user_file='jdata_ori/JData_User.csv'
product_file='jdata_ori/JData_Product.csv'

user_feature='jdata_sam/user_feature.csv'


num_sample=2000000
lst=[action_2016_02_file,action_2016_03_file,action_2016_04_file]
for fname in lst:
    with open('jdata_ori/'+fname[10:],'rb') as fo:
        with open(fname,'wb') as fs:
            for i in range(num_sample):
                fs.write(fo.readline())


