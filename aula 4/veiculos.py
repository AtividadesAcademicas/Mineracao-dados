import pandas as pd

veiculos = pd.read_csv("marcas-carros.csv")

print(veiculos.head())
print(veiculos.info())
print(veiculos.columns.to_list())