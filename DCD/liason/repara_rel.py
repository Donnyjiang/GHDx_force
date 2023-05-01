import csv

# countries neighbor
# if __name__ == '__main__':
#     with open('/home/jiangdingyi/jdy/force/liason/CC_liasions.csv', 'r') as f:
#         with open('/home/jiangdingyi/jdy/force/liason/cc.txt','w') as w:
#             count = set()
#             data = csv.DictReader(f)
#             for row in data:
#                 tmp1 = (row['C_id1'],row['C_id2'])
#                 tmp2 = (row['C_id2'],row['C_id1'])
#                 if tmp1 not in count and tmp2 not in count:
#                     w.write('''{"source": '''+ str(row['C_id1']) +''', "target": '''+ str(row['C_id2']) +''', "value": 10},''')
#                     count.add(tmp1)
#                     count.add(tmp2)
#             print(count)

# DC   
# if __name__ == '__main__':
#     with open('/home/jiangdingyi/jdy/force/liason/DC_liasons.csv', 'r') as f:
#         with open('/home/jiangdingyi/jdy/force/liason/DC.txt','w') as w:
#             count = set()
#             data = csv.DictReader(f)
#             for row in data:
#                 tmp1 = (row['start_id'],row['end_id'])
#                 tmp2 = (row['end_id'],row['start_id'])
#                 if tmp1 not in count and tmp2 not in count:
#                     w.write('''{"source": '''+ str(row['start_id']) +''', "target": '''+ str(row['end_id']) +''', "value": 10},''')
#                     count.add(tmp1)
#                     count.add(tmp2)
#             print(count)

#FC
if __name__ == '__main__':
    with open('/home/jiangdingyi/jdy/force/liason/FC_liasons.csv', 'r') as f:
        with open('/home/jiangdingyi/jdy/force/liason/FC.txt','w') as w:
            count = set()
            data = csv.DictReader(f)
            for row in data:
                tmp1 = (row['F_id'],row['C_id'])
                tmp2 = (row['C_id'],row['F_id'])
                if tmp1 not in count and tmp2 not in count:
                    w.write('''{"source": '''+ str(row['F_id']) +''', "target": '''+ str(row['C_id']) +''', "value": 10},''')
                    count.add(tmp1)
                    count.add(tmp2)
            print(count)
