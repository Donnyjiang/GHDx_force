import csv
import pandas as pd
import numpy as np

if __name__ == "__main__":
    with open("DC_liasons.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        DC_matrix = np.zeros([169, 204], int)
        for row in reader:
            if (DC_matrix[int(row['start_id']) - 1][int(row['end_id']) - 171] != 1) and (sum(DC_matrix[int(row['start_id']) - 1]) < 29):
                DC_matrix[int(row['start_id']) - 1][int(row['end_id']) - 171] = 1
        df = pd.DataFrame(DC_matrix)
        df.to_csv('/home/jiangdingyi/jdy/force/find_top/data.csv')