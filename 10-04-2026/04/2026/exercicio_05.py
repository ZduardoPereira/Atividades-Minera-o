from sklearn.ensemble import IsolationForest


servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

modelo = IsolationForest(random_state=42)
modelo.fit(servidores)

predicoes = modelo.predict(servidores)

print("Servidor       | Predição | Status")
print("-" * 45)
for servidor, pred in zip(servidores, predicoes):
    status = "ANOMALIA" if pred == -1 else "Normal"
    print(f"  CPU={servidor[0]}%, RAM={servidor[1]}%  |   {pred:2d}    | {status}")

print()
print("Legenda:")
print("   1 -> Ponto NORMAL (dentro do padrão esperado)")
print("  -1 -> ANOMALIA (comportamento isolado/suspeito)")
print()
print("O servidor [99, 95] foi detectado pois combina CPU e RAM extremamente altos,")
print("o que o isola das demais observações na floresta de árvores de decisão.")
