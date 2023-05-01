from neo4j import GraphDatabase
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv

driver = GraphDatabase.driver("bolt://211.81.52.14:7687", auth=("neo4j", "123"), encrypted=False)
# file = "/home/jiangdingyi/jdy/neo4j-community-4.4.11/import/diseases.csv"
with driver.session() as session:
    with open("/home/jiangdingyi/jdy/neo4j-community-4.4.11/import/diseases.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            res3 = session.run('''
                    MATCH(d:disease{disease_name:"'''+ row["id"] +'''"}) 
                    SET d.cata='''+ row["cata"] +''' 
                    RETURN d
                    ''')
        # res3 = session.run("""
        #         match (n:disease)-[r1:disease_value]-(c:country)-[r2:disease_value]-(m:disease) where n.disease_name<>m.disease_name and 0.05<toFloat(r1.value)<0.07 and 0.05<toFloat(r2.value)<0.07 RETURN n.disease_name as D1, m.disease_name as D2, toFloat(r1.value)+toFloat(r2.value) as v
        #     """)
    