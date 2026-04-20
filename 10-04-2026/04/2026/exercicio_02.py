from scipy.stats import zscore

voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]

z_scores = zscore(voltagem)

print("Voltagem | Z-Score")
for v, z in zip(voltagem, z_scores):
    print(f"  {v}V -> Z: {z:.4f}")
    if z < -2.0:
        print(f"  *** ALERTA: Falha de Energia! Voltagem {v}V detectada como anômala! ***")
