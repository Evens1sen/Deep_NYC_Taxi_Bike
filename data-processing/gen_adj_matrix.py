import numpy as np
import pandas as pd
import csv

adj_matrix = np.zeros((69,69),dtype = np.int)


manhattan_zones_file = open('../data-NYCZones/zones/manhattan_zones.csv', encoding='utf-8')
manhattan_zones_reader = csv.reader(manhattan_zones_file)
manhattan_zones_numbers = []
manhattan_zones_header = []
manhattan_zones = []
for i in manhattan_zones_reader:
    if len(manhattan_zones_header) == 0:
        manhattan_zones_header = i
        continue
    manhattan_zones_numbers.append(i)

edge_file = open('../data-NYCZones/zones/edges.txt')

for edge in edge_file:
    edge = edge.split()
    a = int(edge[0])
    if a == -1:
        break
    b = int(edge[1])
    for i in manhattan_zones_numbers:
        if int(i[0]) == a:
            a = int(i[1])
            break
    for i in manhattan_zones_numbers:
        if int(i[0]) == b:
            b = int(i[1])
            break
    print(a, end=' ')
    print(b)
    adj_matrix[a][b] = 1
    adj_matrix[b][a] = 1

for i in adj_matrix:
    print(i)

df = pd.DataFrame(adj_matrix)
df.to_csv('../data-NYCZones/adjmatrix/W_adj_matrix.csv', index=False)
