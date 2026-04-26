import pandas as pd
import random

random.seed(5)

df_motoristas = pd.DataFrame({
    'id_motorista': range(1, 7),
    'nome_motorista': ['Pedro Alves', 'Marina Costa', 'Roberto Faria',
                       'Sandra Leite', 'Tiago Vaz', 'Ursula Nobre'],
    'cnh_categoria': ['E', 'B', 'D', 'E', 'B', 'D']
})

df_veiculos = pd.DataFrame({
    'id_veiculo': range(1, 7),
    'placa': ['ABC1A23', 'DEF2B34', 'GHI3C45', 'JKL4D56', 'MNO5E67', 'PQR6F78'],
    'tipo_veiculo': ['Caminhão', 'Van', 'Van', 'Caminhão', 'Moto', 'Van'],
    'capacidade_kg': [10000, 1500, 1500, 8000, 50, 1500]
})

entregas_rows = []
for i in range(1, 41):
    entregas_rows.append({
        'id_entrega': i,
        'id_motorista': random.randint(1, 6),
        'id_veiculo': random.randint(1, 6),
        'distancia_km': round(random.uniform(20, 500), 1),
        'status_entrega': random.choice(['Entregue', 'Entregue', 'Em Rota', 'Atrasado']),
        'data_entrega': f'2026-01-{random.randint(1,28):02d}'
    })
df_entregas = pd.DataFrame(entregas_rows)

print("=== df_motoristas ===")
print(df_motoristas)
print("\n=== df_veiculos ===")
print(df_veiculos)
print("\n=== df_entregas ===")
print(df_entregas)

# Total de km
total_km = df_entregas['distancia_km'].sum()
print(f"\nTotal absoluto de km rodados: {total_km:.1f} km")

# Motorista que mais rodou de Van
merged = df_entregas.merge(df_motoristas, on='id_motorista').merge(df_veiculos, on='id_veiculo')
van_km = merged[merged['tipo_veiculo'] == 'Van'].groupby('nome_motorista')['distancia_km'].sum()
if not van_km.empty:
    print(f"Motorista que mais rodou de Van: {van_km.idxmax()} ({van_km.max():.1f} km)")
