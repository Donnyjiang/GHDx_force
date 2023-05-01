import csv

if __name__ == '__main__':
    with open('/home/jiangdingyi/jdy/force/DCD/result/result.csv', 'r') as f:
        with open('/home/jiangdingyi/jdy/force/DCD/result/norel.txt','w') as w:
            count = [[0 for i in range(169)] for j in range(169)]
            data = csv.reader(f)
            rows = 0
            non = []
            m = 0
            for row in data:
                # print(row)
                for tmp in row:
                    m += int(tmp)
                if m == 0:
                    non.append(rows)
                m = 0
                rows += 1
            print(non)
                #for col in range(169):





