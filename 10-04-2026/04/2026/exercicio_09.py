from sklearn.preprocessing import MinMaxScaler


valor_manual = (200 - 100) / (500 - 100)
print(f"Cálculo manual para 200 psi: {valor_manual:.4f}  (esperado: 0.25)\n")


pressao = [[100], [200], [500]]

scaler = MinMaxScaler()
pressao_normalizada = scaler.fit_transform(pressao)

print("Resultado do MinMaxScaler:")
for original, normalizado in zip(pressao, pressao_normalizada):
    print(f"  {original[0]} psi -> {normalizado[0]:.4f}")

print()
leitura_200 = pressao_normalizada[1][0]
if abs(leitura_200 - valor_manual) < 1e-9:
    print("Verificação: o resultado do MinMaxScaler BATE com o cálculo manual. OK!")
else:
    print(f"Divergência encontrada: manual={valor_manual:.4f}, scaler={leitura_200:.4f}")
