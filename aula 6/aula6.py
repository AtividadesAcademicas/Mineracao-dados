import pandas as pd

df = pd.read_csv('ideb_2023.csv', encoding='latin1', sep=';')

print(df.head())

print(df.count())

ideb = df.dropna(axis=0, subset=None, inplace=False)

print(ideb.count())

print(ideb.head(50))

print(ideb[ideb['Língua Portuguesa'] == ideb['Língua Portuguesa'].max()])

print(ideb[ideb['Língua Portuguesa'] == ideb['Língua Portuguesa'].min()])

print(ideb[ideb['Matemática'] == ideb['Matemática'].max()])

print(ideb[ideb['Matemática'] == ideb['Matemática'].min()])

print(ideb[ideb['Nota Média Padronizada (N)'] == ideb['Nota Média Padronizada (N)'].max()])

print(ideb[ideb['Nota Média Padronizada (N)'] == ideb['Nota Média Padronizada (N)'].min()])

sp = ideb[ideb['Sigla da UF'] == 'SP']

print(sp.head())

print(sp[sp['Língua Portuguesa'] == sp['Língua Portuguesa'].min()])

print(sp[sp['Língua Portuguesa'] == sp['Língua Portuguesa'].max()])

print(sp[sp['Matemática'] == sp['Matemática'].min()])

print(sp[sp['Matemática'] == sp['Matemática'].max()])

print(sp[sp['Nota Média Padronizada (N)'] == sp['Nota Média Padronizada (N)'].min()])

print(sp[sp['Nota Média Padronizada (N)'] == sp['Nota Média Padronizada (N)'].max()])

etec = sp[sp['Nome da Escola'].str.contains('ETEC')]

print(etec.head())

print(etec[etec['Língua Portuguesa'] == etec['Língua Portuguesa'].min()])

print(etec[etec['Língua Portuguesa'] == etec['Língua Portuguesa'].max()])

print(etec[etec['Matemática'] == etec['Matemática'].min()])

print(etec[etec['Matemática'] == etec['Matemática'].max()])

print(etec[etec['Nota Média Padronizada (N)'] == etec['Nota Média Padronizada (N)'].min()])

print(etec[etec['Nota Média Padronizada (N)'] == etec['Nota Média Padronizada (N)'].max()])

etec['Nota Média Padronizada (N)'] = pd.to_numeric(etec['Nota Média Padronizada (N)'], errors = 'coerce')

total = etec[(etec['Nota Média Padronizada (N)'] > 6)]

print(total.count())