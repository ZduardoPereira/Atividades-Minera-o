import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    'Nome':         ['Ana', 'Bruno', 'Carla', 'Diego', 'Eva', 'Outlier'],
    'Idade':        [22,     25,      23,      27,      24,    150],
    'Horas_Estudo': [10,     8,       12,      9,       11,    10],
    'Nota_Final':   [8.5,    7.0,     9.0,     7.5,     8.0,   8.2],
})

features = df[['Idade', 'Horas_Estudo', 'Nota_Final']]

modelo = IsolationForest(contamination=0.15, random_state=42)
df['Outlier'] = modelo.fit_predict(features)

print("DataFrame completo com coluna Outlier:")
print(df)
print()

anomalias = df[df['Outlier'] == -1]
print("Linha(s) detectada(s) como anomalia:")
print(anomalias)
