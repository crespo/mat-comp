import matplotlib.pyplot as plt
import pandas as pd
import math

arquivo = './dados_inmet.csv'
planilha = pd.read_csv(arquivo, sep=',')

dados_data = planilha['Data'].tolist()
dados_precipitacao = planilha['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].tolist()
dados_temperatura_maxima = planilha['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].tolist()
dados_temperatura_minima = planilha['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'].tolist()

temperaturas_medias = []
for i in range(len(dados_temperatura_minima)):
    temperatura_maxima = dados_temperatura_maxima[i]
    temperatura_minima = dados_temperatura_minima[i]
    temperatura_media = (temperatura_maxima + temperatura_minima) / 2
    temperaturas_medias.append(temperatura_media)

def verificacoesPorMes(dados_data):
    linhasPorMeses = []
    mes_atual = ''
    linhas = 0
    for data in dados_data:
        mes_loop = data[5:7]
        if mes_atual == '':
            mes_atual = mes_loop
            linhas += 1
        elif mes_atual != mes_loop:
            linhasPorMeses.append(linhas)
            mes_atual = mes_loop
            linhas = 1
        else:
            linhas += 1

    linhasPorMeses.append(linhas)
    return linhasPorMeses


verificacoesPorMes = verificacoesPorMes(dados_data)

contador = 0
indice_atual = 0
temperaturas_por_mes = []
temperaturas_para_media = []

for temperatura_media in temperaturas_medias:
    verificacoes = verificacoesPorMes[indice_atual]
    contador += 1
    if contador < verificacoes:
        if not math.isnan(temperatura_media):
            temperaturas_para_media.append(temperatura_media)
    else:
        if temperaturas_para_media == []:
            temperaturas_por_mes.append(0)
        else:
            temperaturas_para_media = pd.Series(temperaturas_para_media)
            temperaturas_por_mes.append(round(temperaturas_para_media.mean(), 1))
        
        temperaturas_para_media = []
        contador = 0
        indice_atual += 1

    

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']


plt.bar(meses, temperaturas_por_mes)
plt.show()











