import csv
import numpy as np

np.set_printoptions(suppress=True)
# with open("/home/jiangdingyi/jdy/force/diseases.csv","r") as f:
#     data = csv.reader(f)
#     txt = open("/home/jiangdingyi/jdy/force/D.txt","w")
#     for row in data:
#         txt.write('''{name:"'''+row[2]+'''"},''')

count = [[0 for i in range(170)] for j in range(170)]
# count = np.zeros([170,170], dtype = int, order = 'C')
# print(len(b))
# {source:0,target:4,relation:"籍贯",value:1.3}

# with open("/home/jiangdingyi/jdy/force/data/DD2.csv","r") as f:
#     data = csv.reader(f)
#     txt = open("/home/jiangdingyi/jdy/force/data/DD2.txt","w")
#     for row in data:
#         if b[int(row[0])][int(row[1])] == 0 and b[int(row[1])][int(row[0])] == 0:
#             txt.write('''{source:'''+ row[0] +''',target:'''+ row[1] +''',value:'''+ row[2] +'''},''')
#             b[int(row[0])][int(row[1])] == 1
#             b[int(row[1])][int(row[0])] == 1

# with open("/home/jiangdingyi/jdy/force/data/DD3.csv","r") as f:
#     data = csv.reader(f)
#     txt = open("/home/jiangdingyi/jdy/force/data/DD3.txt","w")
#     for row in data:
#         if b[int(row[0])][int(row[1])] == 0 and b[int(row[1])][int(row[0])] == 0:
#             txt.write('''{source:'''+ row[0] +''',target:'''+ row[1] +''',value:'''+ row[2] +'''},''')
#             b[int(row[0])][int(row[1])] == 1
#             b[int(row[1])][int(row[0])] == 1

with open("/home/jiangdingyi/jdy/force/DCCD/data/DD3.csv","r") as f:
    data = csv.reader(f)
    #txt = open("/home/jiangdingyi/jdy/force/data/DD6.txt","w")
    for row in data:
        #if b[int(row[0])][int(row[1])] == 0 and b[int(row[1])][int(row[0])] == 0:
            # txt.write('''{source:'''+ row[0] +''',target:'''+ row[1] +''',value:'''+ row[2] +'''},''')
        count[int(row[0])][int(row[1])] += 1


with open("/home/jiangdingyi/jdy/force/DCCD/data/DD4.csv","r") as f:
    data = csv.reader(f)
    #txt = open("/home/jiangdingyi/jdy/force/data/DD6.txt","w")
    for row in data:
        #if b[int(row[0])][int(row[1])] == 0 and b[int(row[1])][int(row[0])] == 0:
            # txt.write('''{source:'''+ row[0] +''',target:'''+ row[1] +''',value:'''+ row[2] +'''},''')
        count[int(row[0])][int(row[1])] += 1


with open("/home/jiangdingyi/jdy/force/DCCD/data/DD5.csv","r") as f:
    data = csv.reader(f)

    #txt = open("/home/jiangdingyi/jdy/force/data/DD6.txt","w")
    for row in data:
        #print(row[0],",",row[1])
        #if b[int(row[0])][int(row[1])] == 0 and b[int(row[1])][int(row[0])] == 0:
            # txt.write('''{source:'''+ row[0] +''',target:'''+ row[1] +''',value:'''+ row[2] +'''},''')
        count[int(row[0])][int(row[1])] += 1

print(count)
with open("/home/jiangdingyi/jdy/force/DCCD/result/result.csv", 'w') as f:
    write = csv.writer(f)
    write.writerows(count)



