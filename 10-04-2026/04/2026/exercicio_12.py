import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

producao = [100, 102, 98, 105, 500, 101]

# --- Passo 1: remover outlier com Z-Score ---
z_scores = zscore(producao)

dados_limpos = [v for v, z in zip(producao, z_scores) if abs(z) <= 2.5]

print("=== Passo 1: Z-Score ===")
print(f"Produção original: {producao}")
for v, z in zip(producao, z_scores):
    flag = " <- OUTLIER REMOVIDO" if abs(z) > 2.5 else ""
    print(f"  {v} peças -> Z-Score: {z:.4f}{flag}")

print(f"\nDados limpos (sem outlier): {dados_limpos}")

# --- Passo 2: normalização Min-Max ---
dados_array = np.array(dados_limpos).reshape(-1, 1)

scaler = MinMaxScaler()
dados_normalizados = scaler.fit_transform(dados_array).flatten()

print("\n=== Passo 2: Normalização Min-Max ===")
print("Peças/hora | Normalizado")
for original, normalizado in zip(dados_limpos, dados_normalizados):
    print(f"   {original}     |   {normalizado:.4f}")

print(f"\nLista final normalizada: {[round(v, 4) for v in dados_normalizados]}")

print()
print("=== Explicação: por que normalizar DEPOIS de remover outliers? ===")
print()
print("  Se o 500 ainda estivesse na lista, o MinMaxScaler usaria:")
print("    min=98, max=500 -> a escala seria dominada pelo outlier.")
print("  Todos os valores normais (98~105) ficariam comprimidos entre 0.00 e 0.014,")
print("  ou seja, sem variação útil. A informação real seria perdida.")
print()
print("  Removendo o 500 antes, o min=98 e max=105, e a normalização")
print("  distribui os valores normais por toda a escala [0, 1], preservando")
print("  as variações pequenas que são justamente o sinal que importa.")
