import numpy as np
from scipy.stats import zscore

medidas = [10, 12, 11, 10, 10000]

z_scores = zscore(medidas)

media = np.mean(medidas)
desvio_padrao = np.std(medidas)

print(f"Média da lista: {media:.2f}")
print(f"Desvio padrão da lista: {desvio_padrao:.2f}")
print()

z_do_outlier = z_scores[-1]
print(f"Z-Score do valor 10000: {z_do_outlier:.4f}")

if abs(z_do_outlier) > 3:
    print("O valor 10000 ULTRAPASSA a marca de 3 sigmas -> é detectado como anomalia.")
else:
    print("O valor 10000 NÃO ultrapassa a marca de 3 sigmas -> NÃO é detectado como anomalia.")

print()
print("Explicação: o próprio outlier 10000 infla tanto a média e o desvio padrão")
print("que, ao calcular seu próprio Z-Score, o resultado fica abaixo de 3.")
print("Isso mostra que o Z-Score é pouco confiável em listas pequenas com outliers colossal.")
