import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('MentalHealthDataset.csv')

# Criando a tabela de contingência
ct = pd.crosstab(df['family_history'], df['treatment'])

# Imprimindo a tabela de contingência
print(ct)