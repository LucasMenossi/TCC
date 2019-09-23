import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('PDFpg1.xlsx')
df = pd.read_excel(xlsx, 'Planilha1')
df = df.drop(['Exerc..1', 'Tipo', 'Serie', 'Nr.', 'Lcto', 'Exerc.'], axis = 1)
#cols = df.columns.tolist()
df = df.rename(columns={"Exerc. Empenho" : "Exeric", "Unnamed: 9" : "Empenho", "Tipo.1" : "Tipo"})
df['Nr Litros'] = df['Nr Litros'] / 100
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})

df.plot(kind='scatter', x='Valor', y='Nr Litros', title='Revenue (millions) vs Rating')