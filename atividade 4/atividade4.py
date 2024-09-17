import pandas as pd

df = pd.read_csv('ideb_2023.csv', encoding='latin1', sep=';')
#print(df.head())
ideb = df.dropna(axis=0, subset=None, inplace=False)

sp = ideb[ideb['Sigla da UF'] == 'SP']
sp['Língua Portuguesa'] = pd.to_numeric(sp['Língua Portuguesa'], errors='coerce')
sp['Matemática'] = pd.to_numeric(sp['Matemática'], errors='coerce')
sp['Nota Média Padronizada (N)'] = pd.to_numeric(sp['Nota Média Padronizada (N)'], errors='coerce')
#print(sp.head())

# Dividindo o dataframe sp em dois novos: um contém somente as etecs e outro somente as demais escolas estaduais
etec = sp[sp['Nome da Escola'].str.contains('ETEC')]
#print(etec.head())
municipais = sp[~sp['Nome da Escola'].str.contains('ETEC')]
#print(municipais.head())


#Português
print('\nMaior nota de português do estado de SP:\n', municipais[municipais['Língua Portuguesa'] == municipais['Língua Portuguesa'].max()], '\n')
print('Menor nota de português do estado de SP:\n', municipais[municipais['Língua Portuguesa'] == municipais['Língua Portuguesa'].min()], '\n')
print('Maior nota de português de ETEC:\n', etec[etec['Língua Portuguesa'] == etec['Língua Portuguesa'].max()], '\n')
print('Menor nota de português de ETEC:\n', etec[etec['Língua Portuguesa'] == etec['Língua Portuguesa'].min()], '\n')
# Nota-se que a rede estadual possui uma nota máxima maior do que a rede das etecs, porém, também possui uma nota mínima menor. Pode-se notar também que a diferença entre a maior nota estual e da etec não é tão grande, enquanto a diferença nas notas mínimas é maior.
print('Média de notas de português do estado de SP:\n', municipais[['Língua Portuguesa']].mean(), '\n')
print('Média de notas de português de ETEC:\n', etec[['Língua Portuguesa']].mean(), '\n')
# Entretanto, ao comparar as médias de notas da rede estadual com as etecs, pode-se observar que a etec possui uma média maior, o que leva a entender que, embora a rede estadual possua a maior nota, as demais notas não seguem esse padrão, enquanto as etecs possuem notas mais consistentes e elevadas.
print('Moda das notas de português do estado de SP:\n', municipais[['Língua Portuguesa']].mode(), '\n')
print('Moda das notas de português de ETEC:\n', etec[['Língua Portuguesa']].mode(), '\n')
# Comparando as modas das notas (valores que mais aparecem), percebe-se que as notas que mais aparecem para as etecs são maiores e em mais quantidade.


#Matemática
print('\nMaior nota de matemática do estado de SP:\n', municipais[municipais['Matemática'] == municipais['Matemática'].max()], '\n')
print('Menor nota de matemática do estado de SP:\n', municipais[municipais['Matemática'] == municipais['Matemática'].min()], '\n')
print('Maior nota de matemática de ETEC:\n', etec[etec['Matemática'] == etec['Matemática'].max()], '\n')
print('Menor nota de matemática de ETEC:\n', etec[etec['Matemática'] == etec['Matemática'].min()], '\n')
# Conforme ocorreu com as notas de português, novamente a rede estadual possui nota máxima maior do que a rede de etec, porém, a diferença entre a nota máxima da rede estadual para as etec é maior. Novamente, a etec tem uma nota mínima superior à rede estadual.
print('Média de notas de matemática do estado de SP:\n', municipais[['Matemática']].mean(), '\n')
print('Média de notas de matemática de ETEC:\n', etec[['Matemática']].mean(), '\n')
# Novamente pode-se observar que a média das notas das etec é superior à média da rede municipal, o que reforça o entendimento de que a etec possui notas mais consistentes e próximas da média.
print('Moda das notas de matemática do estado de SP:\n', municipais[['Matemática']].mode(), '\n')
print('Moda das notas de matemática de ETEC:\n', etec[['Matemática']].mode(), '\n')
# Comparando as modas das notas, percebe-se uma grande diferença entre as notas que mais aparecem nas etecs e na rede estadual, destando-se as etecs.


#Nota média padronizada
print('\nMaior nota média padronizada do estado de SP:\n', municipais[municipais['Nota Média Padronizada (N)'] == municipais['Nota Média Padronizada (N)'].max()], '\n')
print('Menor nota média padronizada do estado de SP:\n', municipais[municipais['Nota Média Padronizada (N)'] == municipais['Nota Média Padronizada (N)'].min()], '\n')
print('Maior nota média padronizada de ETEC:\n', etec[etec['Nota Média Padronizada (N)'] == etec['Nota Média Padronizada (N)'].max()], '\n')
print('Menor nota média padronizada de ETEC:\n', etec[etec['Nota Média Padronizada (N)'] == etec['Nota Média Padronizada (N)'].min()], '\n')
# Conforme ocorreu com as notas de português e matemática, a rede estadual se sobressai na nota máxima mas também possui a nota mínima, enquanto as etecs ficam atrás da nota máxima mas possuem a mínima maior.
print('Média de notas média padronizada do estado de SP:\n', municipais[['Nota Média Padronizada (N)']].mean(), '\n')
print('Média de notas média padronizada de ETEC:\n', etec[['Nota Média Padronizada (N)']].mean(), '\n')
# Novamente pode-se observar que a média das notas parciais das etec é superior à média da rede municipal, sendo mais de um ponto de diferença.
print('Moda das notas média padronizada do estado de SP:\n', municipais[['Nota Média Padronizada (N)']].mode(), '\n')
print('Moda das notas média padronizada de ETEC:\n', etec[['Nota Média Padronizada (N)']].mode(), '\n')
# Comparando as modas das notas, percebe-se que as notas que mais aparecem na rede estadual são baixas, o que leva ao entendimento de que a rede estadual tenha notas parciais altas, porém, com muitas notas baixas, o que faz com que a média seja menor, diferentemente das etec que possuem notas mais consistentes e distribuidas.


municipais_100 = municipais.sort_values(by='Nota Média Padronizada (N)', ascending=False)
#print(municipais_100)
etec_100 = etec.sort_values(by='Nota Média Padronizada (N)', ascending=False)
#print(etec_100)


municipais_100 = municipais_100.nlargest(100, 'Nota Média Padronizada (N)')
print('\n100 melhores escolas do estado de SP em relação às notas médias padronizadas\n',municipais_100)
etec_100 = etec_100.nlargest(100, 'Nota Média Padronizada (N)')
print('100 melhores ETECs em relação às notas médias padronizadas\n', etec_100)
# Comparando as cem melhores escolas estaduais e etecs, pode-se concluir que há muitas escolas estaduais com melhores resultados que etecs, porém, há mais escolas municipais do que etecs e, muitas com notas baixas, o que faz com que a média de notas da rede estadual caia muito.

print('\nMédia de notas de português das cem melhores escolas do estado de SP:\n', municipais_100[['Língua Portuguesa']].mean(), '\n')
print('Média de notas de português das cem melhores ETECs:\n', etec_100[['Língua Portuguesa']].mean(), '\n')

print('Média de notas de matemática das cem melhores escolas do estado de SP:\n', municipais_100[['Matemática']].mean(), '\n')
print('Média de notas de matemática das cem melhores ETECs:\n', etec_100[['Matemática']].mean(), '\n')

print('Média de notas média padronizada das cem melhores escolas do estado de SP:\n', municipais_100[['Nota Média Padronizada (N)']].mean(), '\n')
print('Média de notas média padronizada das cem melhores ETECs:\n', etec_100[['Nota Média Padronizada (N)']].mean())
# Portanto, conclui-se que as ETECs, no geral, possuem resultados melhores que as escolas da rede estadual