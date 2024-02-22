import pandas as pd

chunksize = 10000
df = pd.read_csv("data.csv", chunksize=chunksize)
for chunk in df:
    chunk = chunk[0:500]
    chunk.to_csv('500_data.csv', index=False)
    break