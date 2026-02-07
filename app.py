import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#aula 01

renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_da_empresa'
}

df.rename(columns=renomear_colunas, inplace=True)
colunas = df.columns

traducao_senioridade = {
    'SE': 'Sênior',
    'MI': 'Médio',
    'EN': 'Júnior',
    'EX': 'Executivo'
}
df['senioridade'] = df['senioridade'].replace(traducao_senioridade)

traducao_tamanho_da_empresa = {
    'S': 'Pequeno',
    'M': 'Médio',
    'L': 'Grande'
}
df['tamanho_da_empresa'] = df['tamanho_da_empresa'].replace(traducao_tamanho_da_empresa)

traducao_remoto = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
df['remoto'] = df['remoto'].replace(traducao_remoto)

traducao_contrato = {
    'FT': 'tempo integral',
    'CT': 'contrato',
    'PT': 'tempo parcial',
    'FL': 'freelance'
}
df['contrato'] = df['contrato'].replace(traducao_contrato)

numero_linhas, numero_colunas = df.shape[0], df.shape[1]

print(f"\nlinhas: {numero_linhas}\ncolunas: {numero_colunas}\n")


print(df.head())
print(df.info())
print(df.describe(include=["object", "string"]), '\n')
print(df.describe(), '\n')

for coluna in colunas:
    print(f'{df[coluna].value_counts().head(10)}\n')


#aula 02
import numpy as np

print(F'\nNULOS:\n{df.isnull().sum()}')
print(df['ano'].unique()) 
print(df[df.isnull().any(axis=1)])

df_salarios = pd.DataFrame({
    'nome': ['João', 'Lucas', 'Maria', 'Carlos', 'Val'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})
#substitui os nulos 
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
print(df_salarios, '\n')

df_temperaturas = pd.DataFrame({
    'Dia': ['segunda', 'terça', 'quarta', 'quinta', 'sexta'],
    'Temperatura': [30, np.nan, 29, 31, np.nan]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['Temperatura'].ffill()
df_temperaturas['Preenchido_bfill'] = df_temperaturas['Temperatura'].bfill()
print(df_temperaturas, '\n')

df_cidades = pd.DataFrame({
    'nomes': ['João', 'Lucas', 'Maria', 'Carlos', 'Val'],
    'cidades': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
})

df_cidades['cidade_preenchida'] = df_cidades['cidades'].fillna("Não informado")
print(df_cidades, '\n')

df_limpo = df.dropna()
print(f'\nNULOS:\n{df_limpo.isnull().sum()}')
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.info())

#aula 03
import matplotlib.pyplot as plt
import seaborn as sns


grafico_senioridade = (
    df_limpo['senioridade']
    .value_counts()
    .plot(kind='bar', title='distribuição de seniorade')
)

ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
plt.title("Salário médio por nível se senioridade")
plt.xlabel("nível de senioridade")
plt.ylabel("média do salário anual salário (USD)")

plt.figure(figsize=(8,4))
sns.histplot(df_limpo["usd"], bins = 50, kde=True)
plt.title("Distribuição dos salários anuais")
plt.xlabel("salário em usd")
plt.ylabel("frequência")

plt.show()