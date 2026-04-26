import pandas as pd
import random

random.seed(1)

df_clientes = pd.DataFrame({
    'id_cliente': range(1, 11),
    'nome_cliente': ['Ana Lima', 'Bruno Reis', 'Carla Neves', 'Diego Prado',
                     'Elisa Barros', 'Felipe Gomes', 'Gabi Torres', 'Hugo Duarte',
                     'Iris Cunha', 'João Melo'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo',
               'Porto Alegre', 'Salvador', 'São Paulo', 'Rio de Janeiro',
               'Curitiba', 'Manaus'],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'RS', 'BA', 'SP', 'RJ', 'PR', 'AM']
})

df_produtos = pd.DataFrame({
    'id_produto': range(1, 8),
    'nome_produto': ['Teclado Mecânico', 'Mouse Gamer', 'Monitor 24"',
                     'SSD 1TB', 'Headset USB', 'Webcam HD', 'Hub USB-C'],
    'preco_unitario': [199.90, 89.90, 1299.00, 349.00, 159.90, 219.00, 79.90],
    'categoria': ['Periférico', 'Periférico', 'Monitor', 'Armazenamento',
                  'Periférico', 'Periférico', 'Acessório']
})

vendas_rows = []
for i in range(1, 41):
    vendas_rows.append({
        'id_venda': i,
        'id_cliente': random.randint(1, 10),
        'id_produto': random.randint(1, 7),
        'quantidade_comprada': random.randint(1, 5),
        'data_venda': f'2026-01-{random.randint(1,28):02d}'
    })
df_vendas = pd.DataFrame(vendas_rows)

print("=== df_clientes ===")
print(df_clientes)
print("\n=== df_produtos ===")
print(df_produtos)
print("\n=== df_vendas ===")
print(df_vendas)

# Hardware mais vendido
merged = df_vendas.merge(df_produtos, on='id_produto')
mais_vendido = merged.groupby('nome_produto')['quantidade_comprada'].sum().idxmax()
print(f"\nHardware mais vendido: {mais_vendido}")

# Vendas por estado
por_estado = df_vendas.merge(df_clientes, on='id_cliente')['estado'].value_counts()
print("\nVendas por estado:")
print(por_estado)
