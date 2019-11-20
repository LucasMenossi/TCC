import pandas as pd
import matplotlib.pyplot as plt

#Ler o excel e converter para o formato que o Python pode ler
xlsx = pd.ExcelFile('PDFpg1Original.xlsx')
#Converter o excel em um DataFrame
df = pd.read_excel(xlsx, 'Planilha1')
#Renomear as colunas com nomes errados, primeiro o nome que está aparecendo e depois o nome correto
df = df.rename(columns={"Nr. Ordem" : "Nr. Ordem Abast.","Nr." : "Nr. Lcto Fitcard", "Exerc. Empenho" : "Exerc.", "Unnamed: 9" : "Empenho", "Exerc..1" : "Exerc.", "Tipo.1" : "Tipo", "Valor" : "Valor Abast."})
#Exclui as colunas que apresentam valores repetidos ou nomes incorretos
df = df.drop(["Lcto", "Exerc.", "Lançamento", "Nr. Ordem Abast.", "Nr. Lcto Fitcard", "Empenho", "Tipo Nota Fiscal", "Serie", "EQAL", "Liquidação", "Numero"], axis = 1)
#Corrige os valores da coluna "Nr Litros" que estavam 1000x maiores que os valores originais
df["Nr Litros"] = df["Nr Litros"] / 1000

#OPERAÇÕES ESTATÍSTICAS

#Mostra a média do Nr Litros (46.074514285714294)
df["Nr Litros"].mean()
#Mostra o desvio padrão do Nr Litros (21.306901775179394)
df["Nr Litros"].std()
#Mostra a média do Valor Abast. (157.94828571428576)
df["Valor Abast."].mean()
#Mostra o desvio padrão do Valor Abast. (76.78269292144492)
df["Valor Abast."].std()
#Mostra a média do Valor Ajustado (154.85285714285718)
df["Valor Ajustado"].mean()
#Mostra o desvio padrão do Valor Ajustado (74.70985227458796)
df["Valor Ajustado"].std()
#Mostra situação atual do DataFrame

#Ordena as colunas em orden crescente com base na coluna Nr Litros
df.sort_values(by="Nr Litros")

#Mostra apenas as colunas que estão acima da média da coluna Nr Litros
df[df["Nr Litros"] > df["Nr Litros"].mean()]

df