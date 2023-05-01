import pandas as pd
import csv
 
data = pd.read_csv("/home/jiangdingyi/jdy/force/data/DD3.csv")
 
# data_new=data.drop([128,129,130]) #删除128，129，130行数据
 
data_new=data.drop(["3"], axis=1) #删除title这列数据
 
#、、、、对于data进行多次操作，如果想要连续操作，记得都将.号之前的主语改成同一pandas对象，
#比如前来两个操作，第二个主语需要改成data_new对象。如果想要保存新的csv文件，则为：
 
data_new.to_csv("/home/jiangdingyi/jdy/force/data/DD3.csv",index=0)