import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/i-eng-dados-26/refs/heads/main/dados.csv")

print(df.head(10))
print(df.info())
print(df.isnull().sum())


df['id_usuario'] = df['id_usuario'].fillna("USER_DESCONHECIDO")

print(df[df["id_usuario"] == 'USER_DESCONHECIDO'])

print(df.isnull().sum())