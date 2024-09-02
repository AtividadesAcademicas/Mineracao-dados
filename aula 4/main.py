import pandas as pd

df = pd.DataFrame({
    "Nome:":{
        0:"João",
        1:"Maria",
        2:"José"
    },
    "Escolaridade:":{
        0:"Ensino médio",
        1:"Ensino superior",
        2:"Ensino fundamental"
    }
})

print(df)

df.to_csv("dados.csv", index=False)