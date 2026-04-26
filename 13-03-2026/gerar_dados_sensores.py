import pandas as pd
import numpy as np

np.random.seed(42)

n = 50
df = pd.DataFrame({
    'id_leitura':       range(1, n + 1),
    'temperatura_celsius': np.round(np.random.normal(75, 5, n), 2),
    'pressao_psi':      np.round(np.random.normal(100, 10, n), 2),
})

# Inserir outliers
df.loc[10, 'temperatura_celsius'] = 300.0
df.loc[25, 'pressao_psi'] = 500.0

# Inserir NaN
nan_idx_temp = [5, 15, 30]
nan_idx_pres = [8, 20, 40]
df.loc[nan_idx_temp, 'temperatura_celsius'] = np.nan
df.loc[nan_idx_pres, 'pressao_psi'] = np.nan

df.to_csv('dados_sensores.csv', index=False)
print("dados_sensores.csv gerado com sucesso.")
print(df.head(10))
