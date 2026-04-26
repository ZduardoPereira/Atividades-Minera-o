import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# ─────────────────────────────────────────────
# BASE A: Empresa.xlsx  (apenas IDs cruzados)
# ─────────────────────────────────────────────
clientes = pd.DataFrame({
    'id_cliente': range(1, 11),
    'nome_cliente': ['Ana Silva', 'Bruno Costa', 'Carla Dias', 'Diego Ramos',
                     'Elisa Faro', 'Felipe Neto', 'Gabi Lopes', 'Hugo Melo',
                     'Iris Pinto', 'João Sá'],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'RS', 'BA', 'SP', 'RJ', 'MG', 'PR']
})

produtos = pd.DataFrame({
    'id_produto': range(1, 8),
    'nome_produto': ['Teclado Mecânico', 'Mouse Gamer', 'Monitor 24"',
                     'SSD 1TB', 'Headset USB', 'Webcam HD', 'Hub USB-C'],
})

vendas_rows = []
for i in range(1, 31):
    vendas_rows.append({
        'id_venda': i,
        'id_cliente': random.randint(1, 10),
        'id_produto': random.randint(1, 7),
    })
vendas = pd.DataFrame(vendas_rows)

with pd.ExcelWriter('Empresa.xlsx', engine='openpyxl') as writer:
    clientes.to_excel(writer, sheet_name='Clientes', index=False)
    produtos.to_excel(writer, sheet_name='Produtos', index=False)
    vendas.to_excel(writer, sheet_name='Vendas', index=False)

print("Empresa.xlsx gerado.")

# ─────────────────────────────────────────────
# BASE B: Empresa_Completa.xlsx (datas + quantidades + preços)
# ─────────────────────────────────────────────
precos = [199.90, 89.90, 1299.00, 349.00, 159.90, 219.00, 79.90]
produtos_completo = produtos.copy()
produtos_completo['valor_produto'] = precos

data_base = datetime(2026, 1, 1)
vendas_completo = vendas.copy()
vendas_completo['data_venda'] = [data_base + timedelta(days=random.randint(0, 30)) for _ in range(30)]
vendas_completo['quantidade'] = [random.randint(1, 5) for _ in range(30)]

with pd.ExcelWriter('Empresa_Completa.xlsx', engine='openpyxl') as writer:
    clientes.to_excel(writer, sheet_name='Clientes', index=False)
    produtos_completo.to_excel(writer, sheet_name='Produtos', index=False)
    vendas_completo.to_excel(writer, sheet_name='Vendas', index=False)

print("Empresa_Completa.xlsx gerado.")

# ─────────────────────────────────────────────
# BASE C: Gestao_Chamados_TI.xlsx
# ─────────────────────────────────────────────
usuarios = pd.DataFrame({
    'id_usuario': range(1, 11),
    'nome_usuario': ['Alice Borges', 'Carlos Lima', 'Daniela Souza', 'Eduardo Pires',
                     'Fernanda Cruz', 'Gabriel Azev', 'Helena Rocha', 'Igor Santos',
                     'Juliana Mota', 'Klaus Ferreira'],
    'departamento': ['RH', 'TI', 'Financeiro', 'Logística', 'RH',
                     'Financeiro', 'TI', 'Logística', 'RH', 'TI']
})

servicos = pd.DataFrame({
    'id_servico': range(1, 6),
    'categoria_servico': ['Suporte Hardware', 'Rede/Conectividade', 'Software/Sistema',
                          'Segurança', 'Backup/Recuperação'],
    'custo_hora': [120.0, 150.0, 100.0, 200.0, 130.0]
})

chamados_rows = []
for i in range(1, 21):
    horas = round(random.uniform(0.5, 8.0), 1)
    chamados_rows.append({
        'id_ticket': i,
        'id_usuario': random.randint(1, 10),
        'id_servico': random.randint(1, 5),
        'horas_trabalhadas': horas,
        'status': random.choice(['Resolvido', 'Resolvido', 'Em Aberto'])
    })
chamados = pd.DataFrame(chamados_rows)

with pd.ExcelWriter('Gestao_Chamados_TI.xlsx', engine='openpyxl') as writer:
    usuarios.to_excel(writer, sheet_name='Usuarios', index=False)
    servicos.to_excel(writer, sheet_name='Servicos', index=False)
    chamados.to_excel(writer, sheet_name='Chamados', index=False)

print("Gestao_Chamados_TI.xlsx gerado.")
print("\nTodos os arquivos Excel foram gerados com sucesso!")
print("Importe-os no Power BI Desktop via: Obter Dados > Excel.")
