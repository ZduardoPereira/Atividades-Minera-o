import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

print("=" * 55)
print("EXERCÍCIO 1 - Conversão segura + detecção de falhas")
print("=" * 55)
dados_sensor = pd.DataFrame({
    'ID': range(1, 11),
    'Temperatura_C': ['23.5', '24.1', 'falha_sinal', '22.8', '25.0',
                      'falha_sinal', '23.9', '24.7', 'falha_sinal', '22.1']
})
dados_sensor['Temperatura_C'] = pd.to_numeric(dados_sensor['Temperatura_C'], errors='coerce')
falhas = dados_sensor[dados_sensor['Temperatura_C'].isna()]
print("Linhas com falha de conversão:")
print(falhas)

print("\n" + "=" * 55)
print("EXERCÍCIO 2 - Datas de entrega antes do pedido")
print("=" * 55)
compras = pd.DataFrame({
    'ID': range(1, 8),
    'Data_Compra':  pd.to_datetime(['2026-01-05', '2026-01-10', '2026-01-15',
                                    '2026-01-20', '2026-01-08', '2026-01-12', '2026-01-18']),
    'Data_Entrega': pd.to_datetime(['2026-01-10', '2026-01-08', '2026-01-20',
                                    '2026-01-25', '2026-01-07', '2026-01-15', '2026-01-22'])
})
erros = compras[compras['Data_Entrega'] < compras['Data_Compra']]
print("Compras com entrega antes do pedido:")
print(erros)

print("\n" + "=" * 55)
print("EXERCÍCIO 3 - Mapa de calor de NaN")
print("=" * 55)
formulario = pd.DataFrame({
    'nome':       ['Ana', None, 'Carlos', 'Diana', None],
    'email':      ['a@a.com', 'b@b.com', None, 'd@d.com', 'e@e.com'],
    'telefone':   [None, '999', '888', None, '777'],
    'cidade':     ['SP', 'RJ', None, 'MG', 'PR'],
    'nascimento': ['1990-01-01', None, '1985-05-10', '2000-03-20', None]
})
print("Mapa de NaN (True = ausente):")
print(formulario.isna())
plt.figure(figsize=(8, 4))
sns.heatmap(formulario.isna(), cbar=False, cmap='Reds', yticklabels=False)
plt.title('Mapa de Calor – Valores Ausentes')
plt.tight_layout()
plt.savefig('mapa_nan.png', dpi=100)
plt.close()
print("Gráfico salvo em mapa_nan.png")

print("\n" + "=" * 55)
print("EXERCÍCIO 4 - Categorias raras (< 5%)")
print("=" * 55)
so_list = (['Ubuntu'] * 80 + ['Debian'] * 60 + ['Armbian'] * 50 +
           ['UbuntuX'] * 4 + ['Debain'] * 3 + ['armbian'] * 2 + ['RaspOS'] * 1)
random.shuffle(so_list)
df_so = pd.DataFrame({'Sistema_Operacional': so_list})
proporcao = df_so['Sistema_Operacional'].value_counts(normalize=True) * 100
raras = proporcao[proporcao < 5]
print("Categorias que representam menos de 5%:")
print(raras.round(2))

print("\n" + "=" * 55)
print("EXERCÍCIO 5 - Placas com tamanho incorreto")
print("=" * 55)
df_acesso = pd.DataFrame({
    'Placa_Veiculo': ['ABC1D23', 'XY12345', 'DEF-2E34', 'GHI3F45',
                      'JK1G56', 'LMN4H67', 'OPQ 5I78', 'RST6J89']
})
invalidas = df_acesso[df_acesso['Placa_Veiculo'].str.len() != 7]
print("Placas com tamanho incorreto:")
print(invalidas)

print("\n" + "=" * 55)
print("EXERCÍCIO 6 - Idade declarada vs. calculada")
print("=" * 55)
ano_atual = 2026
df_alunos = pd.DataFrame({
    'Nome':            ['Alice', 'Bruno', 'Carla', 'Diego', 'Elisa'],
    'Ano_Nascimento':  [2000, 1998, 2005, 1995, 2003],
    'Idade_Declarada': [26, 28, 20, 31, 22]
})
df_alunos['Idade_Calculada'] = ano_atual - df_alunos['Ano_Nascimento']
contradicoes = df_alunos[df_alunos['Idade_Calculada'] != df_alunos['Idade_Declarada']]
print("Linhas com contradição de idade:")
print(contradicoes)

print("\n" + "=" * 55)
print("EXERCÍCIO 7 - Alturas fisicamente impossíveis")
print("=" * 55)
df_clinica = pd.DataFrame({
    'Paciente': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
    'Altura_Metros': [1.72, 1.65, 175.0, 1.80, 0.30, 1.58]
})
# Altura humana válida: 0.5m a 2.5m
impossiveis = df_clinica[(df_clinica['Altura_Metros'] < 0.5) | (df_clinica['Altura_Metros'] > 2.5)]
print("Pacientes com altura impossível:")
print(impossiveis)

print("\n" + "=" * 55)
print("EXERCÍCIO 8 - Estoque com falha de integridade")
print("=" * 55)
df_estoque = pd.DataFrame({
    'Componente':         ['Resistor', 'Capacitor', 'Transistor', 'LED', 'Diodo', 'CI-555'],
    'Quantidade_Estoque': [500, -10, 300, 1_000_000, -1, 250]
})
# Estoque não pode ser negativo nem absurdamente grande (> 100.000)
invalidos = df_estoque[(df_estoque['Quantidade_Estoque'] < 0) |
                       (df_estoque['Quantidade_Estoque'] > 100_000)]
print("Componentes com falha de integridade:")
print(invalidos)
