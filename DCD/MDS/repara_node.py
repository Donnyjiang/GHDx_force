import csv

if __name__ == '__main__':
    with open('/home/jiangdingyi/jdy/force/DCD/result/diseases.csv', 'r') as f:
        # with open('/home/jiangdingyi/jdy/force/DCD/MDS/node_name.txt','w') as w:
        #     data = csv.DictReader(f)
        #     for row in data:
        #         w.write('''"'''+ row['disease_name'] +'''",''')
                
        with open('/home/jiangdingyi/jdy/force/DCD/MDS/node_cata.txt','w') as w:
            data = csv.DictReader(f)
            for row in data:
                w.write(''''''+ row['cata'] +''',''')



