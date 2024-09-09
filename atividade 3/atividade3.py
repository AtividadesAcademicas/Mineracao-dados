import pandas as pd

frutas = pd.DataFrame([[30, 20]], columns=["Maça", "Banana"])
print(frutas)

vendas_frutas = pd.DataFrame([[1000, 700], [5000, 2000]], columns=["Maça", "Banana"], index=["Vendas 2022", "Vendas 2023"])
print(vendas_frutas)

estatisticas = pd.read_csv("tb_lobby_stats_player.csv")
print(estatisticas.head())
print(estatisticas.info())
print(estatisticas["vlDamage"])
print(estatisticas["qtClutchWon"].max())
print(estatisticas.loc[estatisticas["qtHs"]>=35])