import numpy as np
import pandas as pd
 
# path处填入npy文件具体路径
npfile3 = np.load('/home/jiangdingyi/jdy/force/DCF/data/DD3.npy', allow_pickle=True)
npfile4 = np.load('/home/jiangdingyi/jdy/force/DCF/data/DD4.npy', allow_pickle=True)
npfile5 = np.load('/home/jiangdingyi/jdy/force/DCF/data/DD5.npy', allow_pickle=True)
npfile6 = np.load('/home/jiangdingyi/jdy/force/DCF/data/DD6.npy', allow_pickle=True)
npfile7 = np.load('/home/jiangdingyi/jdy/force/DCF/data/DD7.npy', allow_pickle=True)
# 将npy文件的数据格式转化为csv格式
np_to_csv3 = pd.DataFrame(data = npfile3)
np_to_csv4 = pd.DataFrame(data = npfile4)
np_to_csv5 = pd.DataFrame(data = npfile5)
np_to_csv6 = pd.DataFrame(data = npfile6)
np_to_csv7 = pd.DataFrame(data = npfile7)
 
# 存入具体目录下的np_to_csv.csv 文件  
np_to_csv3.to_csv('/home/jiangdingyi/jdy/force/DCF/data/DD3.csv') 
np_to_csv4.to_csv('/home/jiangdingyi/jdy/force/DCF/data/DD4.csv') 
np_to_csv5.to_csv('/home/jiangdingyi/jdy/force/DCF/data/DD5.csv') 
np_to_csv6.to_csv('/home/jiangdingyi/jdy/force/DCF/data/DD6.csv') 
np_to_csv7.to_csv('/home/jiangdingyi/jdy/force/DCF/data/DD7.csv') 