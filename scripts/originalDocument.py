import pandas as pd
import matplotlib.pyplot as plt

#Ler o excel e converter para o formato que o Python pode ler
xlsx = pd.ExcelFile('PDFpg1Original.xlsx')
#Converter o excel em um DataFrame
df = pd.read_excel(xlsx, 'Planilha1')
#Mostra as colunas com os nomes iniciais e os valores iniciais
df