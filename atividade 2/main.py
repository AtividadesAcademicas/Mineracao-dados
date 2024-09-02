import pandas as pd

filmes = pd.read_csv("tmdb_5000_movies.csv")
creditos = pd.read_csv("tmdb_5000_credits.csv")

#print(filmes.head())
#print(creditos.head())
#print(filmes[['title']].head(), creditos[['cast']].head())

filmes_full = pd.merge(filmes, creditos, on='title')

print(filmes_full.head())

print(filmes_full[['title','cast']])

import json

def extrair_ator(cast):
    try:
        atores = json.loads(cast)
        if len(atores) > 0:
            return atores[0]['name']
        else:
            return 'No actor listed'
    except json.JSONDecodeError:
        return 'Error parsing cast'

filmes_full['first_actor'] = filmes_full['cast'].apply(extrair_ator)

for _, row in filmes_full[['title', 'first_actor']].head().iterrows():
    print(f"{row['title']} | {row['first_actor']}")