import pandas as pd
import matplotlib.pyplot as plt

#Ler o excel e converter para o formato que o Python pode ler
xlsx = pd.ExcelFile('PDFpg1Original.xlsx')
#Converter o excel em um DataFrame
df = pd.read_excel(xlsx, 'Planilha1')
#Renomear as colunas com nomes errados, primeiro o nome que está aparecendo e depois o nome correto
df = df.rename(columns={"Nr. Ordem" : "Nr. Ordem Abast.","Nr." : "Nr. Lcto Fitcard", "Exerc. Empenho" : "Exerc.", "Unnamed: 9" : "Empenho", "Exerc..1" : "Exerc.", "Tipo.1" : "Tipo", "Valor" : "Valor Abast."})
#Mostra a situação atual do DataFrame
df