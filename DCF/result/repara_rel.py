import csv

if __name__ == '__main__':
    with open('/home/jiangdingyi/jdy/force/DCF/result/result.csv', 'r') as f:
        with open('/home/jiangdingyi/jdy/force/DCF/result/rel.txt','w') as w:
            #count = [[0 for i in range(170)] for j in range(170)]
            data = csv.reader(f)
            rows = 0
            m = 0
            for row in data:
                for col in range(199):
                    if int(row[col]) != 0:# and count[rows][col] != 1:
                        # if int(row[col]) > m:
                        #     m = int(row[col])
                        w.write('''{"source": '''+ str(rows) +''', "target": '''+ str(col) +''', "value": '''+ row[col] +'''},''')
                        #count[rows][col] = 1
                        #count[col][rows] = 1
                rows+=1
            print(m)



