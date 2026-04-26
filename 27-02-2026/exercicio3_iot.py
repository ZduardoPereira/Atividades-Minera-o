import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(3)
np.random.seed(3)

df_ambientes = pd.DataFrame({
    'id_ambiente': [1, 2, 3, 4],
    'nome_setor': ['Fundição', 'Montagem', 'Almoxarifado', 'Escritório'],
    'area_m2': [500, 300, 200, 150]
})

df_dispositivos = pd.DataFrame({
    'id_dispositivo': range(1, 9),
    'modelo': ['RPI 4B', 'RPI 4B', 'Orange Pi 5', 'Orange Pi 5',
               'ESP32', 'ESP32', 'RPI 3B', 'ESP32'],
    'id_ambiente': [1, 1, 2, 2, 3, 3, 4, 4]
})

telemetria_rows = []
base = datetime(2026, 3, 1, 8, 0)
for i in range(1, 81):
    disp = random.randint(1, 8)
    amb = df_dispositivos.loc[df_dispositivos['id_dispositivo'] == disp, 'id_ambiente'].values[0]
    base_temp = {1: 38, 2: 28, 3: 22, 4: 20}[amb]
    telemetria_rows.append({
        'id_leitura': i,
        'id_dispositivo': disp,
        'data_hora': base + timedelta(minutes=15 * i),
        'temperatura_c': round(base_temp + np.random.normal(0, 1.5), 1),
        'umidade_pct': round(random.uniform(40, 80), 1)
    })
df_telemetria = pd.DataFrame(telemetria_rows)

print("=== df_ambientes ===")
print(df_ambientes)
print("\n=== df_dispositivos ===")
print(df_dispositivos)
print("\n=== df_telemetria (primeiras linhas) ===")
print(df_telemetria.head(10))

# Ambiente mais quente
merged = (df_telemetria
          .merge(df_dispositivos, on='id_dispositivo')
          .merge(df_ambientes, on='id_ambiente'))
mais_quente = merged.groupby('nome_setor')['temperatura_c'].mean().idxmax()
print(f"\nAmbiente mais quente: {mais_quente}")
