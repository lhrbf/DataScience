import pandas as pd

# Carregue seu conjunto de dados
df = pd.read_csv('MentalHealthDataset.csv')

# Filtrando apenas as colunas relevantes para simplificar a visualização
subset_df = df[['Occupation', 'treatment', 'Growing_Stress']]

# Criando uma tabela cruzada
ct = pd.crosstab(index=[subset_df['Occupation'], subset_df['treatment']],
                 columns=subset_df['Growing_Stress'],
                 margins=True)  # 'All' adiciona uma linha/coluna de totais

# Exibindo a tabela cruzada
print(ct)