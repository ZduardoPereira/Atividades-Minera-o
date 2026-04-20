import numpy as np
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest

# Dados: [Nota, Faltas]
alunos = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

# --- Z-Score univariado nas notas ---
notas = [a[0] for a in alunos]
z_notas = zscore(notas)

print("=== Z-Score individual (apenas Notas) ===")
for aluno, z in zip(alunos, z_notas):
    flag = "<-- anomalia?" if abs(z) > 2 else ""
    print(f"  Nota={aluno[0]}, Faltas={aluno[1]} -> Z-Score nota: {z:.4f} {flag}")

print()
print("O aluno [9, 25] tem nota ALTA, então seu Z-Score de nota é positivo e não ultrapassa 2.")
print("Ele passa despercebido na análise univariada.\n")

# --- Isolation Forest multivariado ---
modelo = IsolationForest(contamination=0.2, random_state=42)
predicoes = modelo.fit_predict(alunos)

print("=== Isolation Forest (Nota + Faltas) ===")
for aluno, pred in zip(alunos, predicoes):
    status = "ANOMALIA (-1)" if pred == -1 else "Normal  ( 1)"
    print(f"  Nota={aluno[0]}, Faltas={aluno[1]} -> {status}")

print()
print("A combinação nota alta + muitas faltas é incomum no conjunto.")
print("O Isolation Forest detecta isso porque analisa as duas dimensões juntas.")
