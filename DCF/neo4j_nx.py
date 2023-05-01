from neo4j import GraphDatabase
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

driver = GraphDatabase.driver("bolt://211.81.52.14:7687", auth=("neo4j", "123"), encrypted=False)
with driver.session() as session:
    # match (n:disease)-[r1:disease_value]-(c:country)-[r2:factor]-(m:reason) RETURN n.disease_name as D, m.reason_name as F, toFloat(r1.value)+toFloat(r2.value) as value limit 5000
    # res = session.run("""
    #         match (n:disease)-[r1:disease_value]-(c:country)-[r3:neighbor]-(c2:country)-[r2:factor]-(m:reason) RETURN n.disease_name as D, c.country_name as C,m.reason_name as F
    #     """)
    # res1 = session.run("""
    #         match (n:disease)-[r1:disease_value]-(c:country)-[r3:neighbor]-(c2:country)-[r2:disease_value]-(m:disease) where n.disease_name<>m.disease_name and toFloat(r1.value)<0.03 and toFloat(r2.value)>0.01 and toFloat(r1.value)<0.03 and toFloat(r2.value)<0.03 RETURN n.disease_name as D1, m.disease_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
    #     """)
    # res2 = session.run("""
    #         match (n:disease)-[r1:disease_value]-(c:country)-[r3:neighbor]-(c2:country)-[r2:disease_value]-(m:disease) where n.disease_name<>m.disease_name and 0.04<toFloat(r1.value)<0.05 and toFloat(r2.value)>0.03 and toFloat(r1.value)<0.05 and toFloat(r2.value)<0.05 RETURN n.disease_name as D1, m.disease_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
    #     """)
    res3 = session.run("""
            match (n:disease)-[r1:disease_value]-(c:country)-[r2:factor]-(m:reason) where 0.007<toFloat(r1.value)<0.07 and 0.007<toFloat(r2.value)<0.07 RETURN n.disease_name as D1, m.reason_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
        """)
    res4 = session.run("""
            match (n:disease)-[r1:disease_value]-(c:country)-[r2:factor]-(m:reason) where 0.07<toFloat(r1.value)<0.1 and 0.07<toFloat(r2.value)<0.1 RETURN n.disease_name as D1, m.reason_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
        """)
    res5 = session.run("""
            match (n:disease)-[r1:disease_value]-(c:country)-[r2:factor]-(m:reason) where 0.1<toFloat(r1.value)<0.2 and 0.1<toFloat(r2.value)<0.2 RETURN n.disease_name as D1, m.reason_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
        """)
    res6 = session.run("""
            match (n:disease)-[r1:disease_value]-(c:country)-[r2:factor]-(m:reason) where 0.2<toFloat(r1.value)<0.3 and 0.2<toFloat(r2.value)<0.3 RETURN n.disease_name as D1, m.reason_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
        """)
    res7 = session.run("""
            match (n:disease)-[r1:disease_value]-(c:country)-[r2:factor]-(m:reason) where 0.3<toFloat(r1.value) and 0.3<toFloat(r2.value) RETURN n.disease_name as D1, m.reason_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
        """)

    # data1 = pd.DataFrame.from_records(res1.data())
    # data2 = pd.DataFrame.from_records(res2.data())
    data3 = pd.DataFrame.from_records(res3.data())
    data4 = pd.DataFrame.from_records(res4.data())
    data5 = pd.DataFrame.from_records(res5.data())
    data6 = pd.DataFrame.from_records(res6.data())
    data7 = pd.DataFrame.from_records(res7.data())
    # res = session.run("""
    #         match (n:disease)-[r1:disease_value]-(c:country) where toFloat(r1.value)>0.01 RETURN n.disease_name as D, c.country_name as C
    #     """)
    # data = pd.DataFrame.from_records(res.data())

# np.save("/home/jiangdingyi/jdy/force/DCCD/data/DD1", data1)
# np.save("/home/jiangdingyi/jdy/force/DCCD/data/DD2", data2)
np.save("/home/jiangdingyi/jdy/force/DCF/data/DD3", data3)
np.save("/home/jiangdingyi/jdy/force/DCF/data/DD4", data4)
np.save("/home/jiangdingyi/jdy/force/DCF/data/DD5", data5)
np.save("/home/jiangdingyi/jdy/force/DCF/data/DD6", data6)
np.save("/home/jiangdingyi/jdy/force/DCF/data/DD7", data7)
# np.save("DCF.npy", data)
# G = nx.path_graph(4)
# nx.write_adjlist(G, "test.adjlist")
# G = nx.from_pandas_edgelist(data)
# G1 = nx.from_pandas_edgelist(data, source="D1", target="D2")
# print(G1)
# docu = nx.generate_adjlist(G1)
# nx.write_adjlist(G1, "/home/jiangdingyi/jdy/MAGNN-master/DCCD.adjlist", comments='#', delimiter='*', encoding='utf-8')
# with open("DF_adjlist", "w") as f:
#     for line in nx.generate_adjlist(G):
#         print(line)
#         # f.write(line+"\n")
# G2 = nx.read_adjlist("/home/jiangdingyi/jdy/MAGNN-master/DCCD.adjlist", comments='#', delimiter='*', create_using=None, nodetype=None, encoding='utf-8')
# print(G2)
# print(G)
# nx.draw(G)
# plt.tight_layout()
# plt.savefig("DF.png", format="PNG")