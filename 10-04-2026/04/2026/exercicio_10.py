import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    'Cliente': ['A', 'B'],
    'Saldo':   [1_000_000, 1_000_010],
    'Risco':   [0.1,       0.9],
})

print("=== Dados originais ===")
print(df)
print()
print("Explicação sem normalização:")
print("  O Saldo varia apenas R$10 entre os clientes (1.000.000 vs 1.000.010).")
print("  O Risco varia 0.8 (0.1 vs 0.9), mas como número absoluto parece insignificante")
print("  perto de 1.000.000. Algoritmos baseados em distância (ex.: KNN, K-Means)")
print("  darão peso enorme ao Saldo e quase ignorarão o Risco, concluindo erroneamente")
print("  que os dois clientes são quase idênticos. O cliente B, porém, tem risco 9x maior!")
print()

# --- Normalização ---
scaler = MinMaxScaler()
colunas = ['Saldo', 'Risco']
df_norm = df.copy()
df_norm[colunas] = scaler.fit_transform(df[colunas])

print("=== Dados normalizados ===")
print(df_norm)
print()
print("Após a normalização:")
print("  Saldo: A=0.0, B=1.0  -> os R$10 agora ocupam toda a escala [0,1].")
print("  Risco: A=0.0, B=1.0  -> a diferença de 0.8 também ocupa toda a escala [0,1].")
print("  Ambas as colunas têm peso igual. O modelo agora enxerga que A e B são")
print("  completamente opostos tanto em Saldo (relativo) quanto em Risco.")
