import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('MentalHealthDataset.csv')

print(df.head())  # Mostra as primeiras 5 linhas

# Salvando o novo DataFrame
df.to_csv('MentalHealthDataset.csv', index=False)