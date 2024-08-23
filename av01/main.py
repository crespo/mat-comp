import matplotlib.pyplot as plt
import pandas as pd
import ezodf

legendas = [5, 6, 7, 8]
valores = [1, 2, 3, 4]
arquivo = "./tabela_limpa.CSV.ods"

planilha = ezodf.opendoc(arquivo).sheets[0]
df_dicionario = {}

for i, linha in enumerate(planilha.rows()):
    if i==0:
        df_dicionario = {celula.value:[] for celula in linha}
        coluna_indice = {j:celula.value for j, celula in enumerate(linha)}
    for j, celula in enumerate(linha):
        df_dicionario[coluna_indice[j]].append(celula.value)

df = pd.DataFrame(df_dicionario)

print(df.columns)

# plt.bar(valores, legendas)
# plt.show()
