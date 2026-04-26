import pandas as pd
import numpy as np

print("=" * 55)
print("EXERCÍCIO 1 - Percentis 25, 50 e 75")
print("=" * 55)
dados = np.array([12, 15, 14, 13, 16, 12, 14, 150, 13, 15])
p25, p50, p75 = np.percentile(dados, [25, 50, 75])
print(f"P25 = {p25}  |  P50 = {p50}  |  P75 = {p75}")

print("\n" + "=" * 55)
print("EXERCÍCIO 2 - IQR e limites com constante 1.5")
print("=" * 55)
IQR = p75 - p25
lim_inf = p25 - 1.5 * IQR
lim_sup = p75 + 1.5 * IQR
print(f"IQR = {IQR}")
print(f"Limite Inferior = {lim_inf}")
print(f"Limite Superior = {lim_sup}")

print("\n" + "=" * 55)
print("EXERCÍCIO 3 - Q1 e Q3 manual (sem np.percentile)")
print("=" * 55)
lista = [100, 150, 200, 250, 300, 350]
lista_ord = sorted(lista)
n = len(lista_ord)
meio = n // 2
metade_inf = lista_ord[:meio]
metade_sup = lista_ord[meio:]
if len(metade_inf) % 2 == 0:
    Q1 = (metade_inf[len(metade_inf)//2 - 1] + metade_inf[len(metade_inf)//2]) / 2
    Q3 = (metade_sup[len(metade_sup)//2 - 1] + metade_sup[len(metade_sup)//2]) / 2
else:
    Q1 = metade_inf[len(metade_inf)//2]
    Q3 = metade_sup[len(metade_sup)//2]
print(f"Q1 = {Q1}  |  Q3 = {Q3}")

print("\n" + "=" * 55)
print("EXERCÍCIO 4 - Outliers de tensão elétrica")
print("=" * 55)
tensao = np.array([110, 115, 120, 118, 112, 220, 116, 114, 119, 12])
q1_t, q3_t = np.percentile(tensao, [25, 75])
iqr_t = q3_t - q1_t
li_t = q1_t - 1.5 * iqr_t
ls_t = q3_t + 1.5 * iqr_t
anomalos = [v for v in tensao if v < li_t or v > ls_t]
print(f"Limites: [{li_t:.1f}, {ls_t:.1f}]")
print(f"Valores anômalos: {anomalos}")

print("\n" + "=" * 55)
print("EXERCÍCIO 5 - Função detectar_anomalias(dados, multiplicador)")
print("=" * 55)
def detectar_anomalias(dados, multiplicador):
    arr = np.array(dados)
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = q3 - q1
    li = q1 - multiplicador * iqr
    ls = q3 + multiplicador * iqr
    return [v for v in arr if v < li or v > ls]

print("Função criada: detectar_anomalias(dados, multiplicador)")

print("\n" + "=" * 55)
print("EXERCÍCIO 6 - Testar função com vetor [45,50,55,60,48,52,51,98,49,53]")
print("=" * 55)
vetor6 = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]
resultado6 = detectar_anomalias(vetor6, 1.5)
print(f"Outliers detectados: {resultado6}")

print("\n" + "=" * 55)
print("EXERCÍCIO 7 - DataFrame Pandas + .quantile()")
print("=" * 55)
df7 = pd.DataFrame({
    'ID_Maquina':     [1, 2, 3, 4, 5],
    'Uso_Memoria_MB': [2048, 2100, 2050, 8192, 2080]
})
q1_m = df7['Uso_Memoria_MB'].quantile(0.25)
q3_m = df7['Uso_Memoria_MB'].quantile(0.75)
iqr_m = q3_m - q1_m
print(f"Q1={q1_m}  Q3={q3_m}  IQR={iqr_m}")

print("\n" + "=" * 55)
print("EXERCÍCIO 8 - Máscara booleana: hardware dentro da normalidade")
print("=" * 55)
li_m = q1_m - 1.5 * iqr_m
ls_m = q3_m + 1.5 * iqr_m
df8 = df7[(df7['Uso_Memoria_MB'] >= li_m) & (df7['Uso_Memoria_MB'] <= ls_m)]
print(f"Limites: [{li_m:.1f}, {ls_m:.1f}]")
print("Hardware normal:")
print(df8)

print("\n" + "=" * 55)
print("EXERCÍCIO 9 - Substituir outlier pela mediana com np.where()")
print("=" * 55)
df9 = pd.DataFrame({'temperatura': [80, 82, 85, 81, 300, 83]})
mediana = df9['temperatura'].median()
q1_9, q3_9 = np.percentile(df9['temperatura'], [25, 75])
iqr_9 = q3_9 - q1_9
li_9 = q1_9 - 1.5 * iqr_9
ls_9 = q3_9 + 1.5 * iqr_9
df9['temperatura_corrigida'] = np.where(
    (df9['temperatura'] < li_9) | (df9['temperatura'] > ls_9),
    mediana,
    df9['temperatura']
)
print(f"Mediana (Q2) = {mediana}")
print(df9)

print("\n" + "=" * 55)
print("EXERCÍCIO 10 - IQR por grupo (Sensor A e B)")
print("=" * 55)
df10 = pd.DataFrame({
    'Sensor_ID':    ['A','A','A','A','A','B','B','B','B','B'],
    'Valor_Leitura': [10, 11, 12, 10, 100, 50, 51, 49, 52, 200]
})
def anomalias_grupo(grupo):
    q1, q3 = np.percentile(grupo['Valor_Leitura'], [25, 75])
    iqr = q3 - q1
    li = q1 - 1.5 * iqr
    ls = q3 + 1.5 * iqr
    return grupo[(grupo['Valor_Leitura'] < li) | (grupo['Valor_Leitura'] > ls)]

resultado10 = df10.groupby('Sensor_ID', group_keys=False).apply(anomalias_grupo)
print("Anomalias por sensor:")
print(resultado10)

print("\n" + "=" * 55)
print("EXERCÍCIO 11 - Carregar dados_sensores.csv + tratar NaN")
print("=" * 55)
df11 = pd.read_csv('dados_sensores.csv')
print("NaN por coluna:")
print(df11.isna().sum())
for col in ['temperatura_celsius', 'pressao_psi']:
    df11[col] = df11[col].fillna(df11[col].median())
print("\nApós fillna com mediana – NaN restantes:")
print(df11.isna().sum())

print("\n" + "=" * 55)
print("EXERCÍCIO 12 - Remover outliers e exportar dados_validados.csv")
print("=" * 55)
df12 = df11.copy()
for col in ['temperatura_celsius', 'pressao_psi']:
    col_data = df12[col].dropna()
    q1, q3 = np.percentile(col_data, [25, 75])
    iqr = q3 - q1
    li = q1 - 1.5 * iqr
    ls = q3 + 1.5 * iqr
    df12 = df12[(df12[col] >= li) & (df12[col] <= ls)]
df12.to_csv('dados_validados.csv', index=False)
print(f"Linhas originais: {len(df11)}  |  Após remoção: {len(df12)}")
print("dados_validados.csv exportado.")

print("\n" + "=" * 55)
print("EXERCÍCIO 13 - Instruções para Power BI")
print("=" * 55)
print("1. Abra o Power BI Desktop.")
print("2. Obter Dados > Texto/CSV > selecione dados_validados.csv")
print("3. Crie um Gráfico de Linhas: Eixo X = id_leitura, Eixo Y = temperatura_celsius")
print("4. Crie um Card: arraste pressao_psi e mude agregação para Média (ou Mediana)")
print("5. Salve como dashboard_sensores.pbix")
