import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(42)

dados_normais = rng.normal(loc=0, scale=1, size=(1000, 2))
dados_anomalos = rng.uniform(low=10, high=20, size=(50, 2))

dataset = np.vstack([dados_normais, dados_anomalos])

# --- Contamination = 0.05 (espera 5% de anomalias) ---
modelo_005 = IsolationForest(contamination=0.05, random_state=42)
pred_005 = modelo_005.fit_predict(dataset)
anomalias_005 = (pred_005 == -1).sum()

# --- Contamination = 0.20 (espera 20% de anomalias) ---
modelo_020 = IsolationForest(contamination=0.20, random_state=42)
pred_020 = modelo_020.fit_predict(dataset)
anomalias_020 = (pred_020 == -1).sum()

print(f"Total de pontos no dataset: {len(dataset)} (1000 normais + 50 anômalos)")
print()
print(f"contamination=0.05 -> Anomalias detectadas: {anomalias_005}")
print(f"contamination=0.20 -> Anomalias detectadas: {anomalias_020}")
print()
print("Conclusão:")
print("  Com contamination=0.05, o modelo é mais conservador e detecta menos pontos.")
print("  Com contamination=0.20, o modelo é mais agressivo e marca mais pontos como anomalia.")
print("  O parâmetro contamination define o limiar de decisão da floresta,")
print("  não treina o modelo em si — ele só ajusta onde o corte é feito.")
