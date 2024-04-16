import pandas as pd

# Carregando o dataset
df = pd.read_csv('MentalHealthDataset.csv')

# Verificando e tratando valores nulos se necessário
df['treatment'] = df['treatment'].fillna('No')

# Agrupando por país e contabilizando respostas para tratamento
treatment_counts = df.groupby('Country')['treatment'].value_counts(normalize=True).unstack()

# Multiplicando por 100 para obter porcentagens
treatment_counts['Yes'] = treatment_counts['Yes'] * 100

# Ordenando os países pela maior taxa de tratamento
sorted_treatment_rates = treatment_counts['Yes'].sort_values(ascending=False)

# Mostrando os 10 primeiros resultados
print(sorted_treatment_rates.head(10))

print("\n\n")


# Criar uma tabela cruzada com contagens de tratamento por país
treatment_counts = pd.crosstab(df['Country'], df['treatment'])

# Calcular a porcentagem de respostas 'Yes' para cada país
treatment_counts['Treatment_Rate'] = (treatment_counts['Yes'] / (treatment_counts['Yes'] + treatment_counts['No'])) * 100

# Ordenar os países pela taxa de tratamento em ordem ascendente
lowest_treatment_countries = treatment_counts.sort_values('Treatment_Rate')

# Mostrar os países com as menores taxas de tratamento
print(lowest_treatment_countries.head(10))