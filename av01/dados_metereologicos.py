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
            linhasPorMeses.append([mes_atual, linhas])
            mes_atual = mes_loop
            linhas = 1
        else:
            linhas += 1

    linhasPorMeses.append([mes_atual, linhas])
    return linhasPorMeses


verificacoesPorMes = verificacoesPorMes(dados_data)

total_mes = 0
contador = 0
indice_atual = 0
temperaturas_por_mes = []
verificacoes_invalidas = 0
for temperatura_media in temperaturas_medias:
    mes_atual = verificacoesPorMes[indice_atual]
    contador += 1
    if contador < mes_atual[1]:
        if not math.isnan(temperatura_media):
            total_mes += temperatura_media
        else:
            verificacoes_invalidas += 1
    else:
        temperaturas_por_mes.append([mes_atual[0], round(total_mes / (mes_atual[1] - verificacoes_invalidas), 1)])
        verificacoes_invalidas = 0
        contador = 0
        indice_atual += 1
        total_mes = 0
    
print(temperaturas_por_mes)
legendas = []
valores = []

for temperatura_por_mes in temperaturas_por_mes:
    legendas.append(temperatura_por_mes[0])
    valores.append(temperatura_por_mes[1])

plt.bar(legendas, valores)
plt.show()











