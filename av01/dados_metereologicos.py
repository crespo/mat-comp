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
        
contador = 0
indice_atual = 0
precipitacao_por_mes = []
precipitacao_para_soma = []
     
for precipitacao in dados_precipitacao:
    verificacoes = verificacoesPorMes[indice_atual]
    contador += 1
    if contador < verificacoes:
        if not math.isnan(precipitacao):
            precipitacao_para_soma.append(precipitacao)
    else:
        if precipitacao_para_soma ==[]:
            precipitacao_por_mes.append(0)
        else:
            precipitacao_para_soma = pd.Series(precipitacao_para_soma)
            precipitacao_por_mes.append(round(precipitacao_para_soma.sum(), 1))
            
        precipitacao_para_soma = []
        contador = 0
        indice_atual += 1

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']


plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.bar(meses[:len(temperaturas_por_mes)], temperaturas_por_mes)
plt.xlabel('Meses')
plt.ylabel('Temperatura Média (°C)')
plt.title('Temperatura Média Mensal')

plt.subplot(1, 2, 2)
plt.bar(meses[:len(precipitacao_por_mes)], precipitacao_por_mes, color='blue')
plt.xlabel('Meses')
plt.ylabel('Precipitação Total (mm)')
plt.title('Precipitação Total Mensal')

plt.tight_layout()
plt.show()

# média, mediana e moda de temperaturaa.
temperaturas_series = pd.Series(temperaturas_por_mes)
media_historica = temperaturas_series.mean()
mediana_historica = temperaturas_series.median()
moda_historica = temperaturas_series.mode()



estatisticas = {
    'Média': media_historica,
    'Mediana': mediana_historica,
    'Moda': moda_historica[0] if not moda_historica.empty else float('nan')  # Usa o primeiro valor da moda se existir
}
plt.figure(figsize=(8, 5))



barras = plt.bar(estatisticas.keys(), estatisticas.values(), color=['orange', 'green', 'blue'])
plt.xlabel('Estatísticas')
plt.ylabel('Valor')
plt.title('Estatísticas Históricas da Temperatura')

for barra in barras:
    altura = barra.get_height()  
    plt.text(barra.get_x() + barra.get_width() / 2, altura + 0.5, f'{altura:.2f}', #calcula a posição x que 
             ha='center', va='bottom')

plt.tight_layout()
plt.show()
