import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('MentalHealthDataset.csv')

# Visualização rápida das colunas
print(df.columns)

# Análise de dados faltantes
print(df.isnull().sum())

# Visualização de distribuição de gênero
sns.countplot(x='Gender', data=df)
plt.title('Distribuição de Gênero')
plt.show()

# Análise de correlação
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Matriz de Correlação')
plt.show()