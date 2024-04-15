import os
import pandas as pd

current_dir = os.path.dirname(__file__)
csv_file = os.path.join(current_dir, 'QueryResults_python_442.csv')

df = pd.read_csv(csv_file)
print(df.head())

# contar quantas linhas tem o csv
print(df.shape[0])

# printar as ultimas linhas
print(df.tail())