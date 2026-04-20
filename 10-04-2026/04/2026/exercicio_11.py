from sklearn.preprocessing import MinMaxScaler

temps = [[-20], [-10], [0], [20]]

scaler = MinMaxScaler()
temps_normalizados = scaler.fit_transform(temps)

print("Temperatura original | Valor normalizado")
print("-" * 40)
for original, normalizado in zip(temps, temps_normalizados):
    print(f"       {original[0]:5}°C       |       {normalizado[0]:.4f}")

print()
valor_zero = temps_normalizados[2][0]
print(f"O valor 0°C ficou normalizado como: {valor_zero:.4f}")
print()
print("Explicação:")
print("  O MinMaxScaler aplica a fórmula: (x - min) / (max - min)")
print("  Min do conjunto = -20, Max = 20, portanto:")
print("    0°C -> (0 - (-20)) / (20 - (-20)) = 20 / 40 = 0.50")
print()
print("  O '0' original NÃO vira '0.0' normalizado.")
print("  O novo 0.0 representa o menor valor do conjunto (-20°C).")
print("  O MinMaxScaler não preserva o zero matemático; ele apenas reescala")
print("  linearmente para que o mínimo vire 0.0 e o máximo vire 1.0.")
