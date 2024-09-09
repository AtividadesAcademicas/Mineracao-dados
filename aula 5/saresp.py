import pandas as pd

saresp = pd.read_csv("Saresp 2023.csv", sep=';')

#print(saresp.head())

#print(saresp.shape)

#print(saresp.dtypes)

resultado_saresp = pd.to_numeric(saresp["MEDPROF"], errors='coerce')

#print(resultado_saresp.head())

total_resultados = saresp.loc[resultado_saresp>200.00]

print(total_resultados.count())

print(total_resultados.head(18))

print(total_resultados.max())

print(total_resultados.loc[total_resultados["NOMEDEPBOL"] == "Rede Municipal"])
print(total_resultados.loc[total_resultados["NOMEDEPBOL"] == "Rede Estadual"])

print(total_resultados.loc[total_resultados["REGIAOMETROPOLITANA"] == "Interior"])
print(total_resultados.loc[total_resultados["REGIAOMETROPOLITANA"] == "Região Metropolitana de São Paulo"])
print(total_resultados.loc[total_resultados["REGIAOMETROPOLITANA"] == "Região Metropolitana de Campinas"])