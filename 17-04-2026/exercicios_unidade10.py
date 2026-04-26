import pandas as pd
import numpy as np
from datetime import datetime, date

print("=" * 55)
print("EXERCÍCIO 1 - Domínio de e-mail + Flag empresarial")
print("=" * 55)
emails = [
    'joao@gmail.com', 'maria@empresa.com.br', 'pedro@yahoo.com',
    'ana@techcorp.com.br', 'lucas@hotmail.com', 'julia@mineracao.com.br'
]
df1 = pd.DataFrame({'email': emails})
df1['dominio'] = df1['email'].str.split('@').str[1]
df1['flag_empresarial'] = df1['dominio'].str.endswith('.com.br').astype(int)
print(df1)

print("\n" + "=" * 55)
print("EXERCÍCIO 2 - Timestamp: mês, dia da semana, Flag final de semana")
print("=" * 55)
timestamps = pd.to_datetime([
    '2026-04-06 09:00', '2026-04-11 14:30', '2026-04-12 08:00',
    '2026-04-13 20:00', '2026-04-14 10:00', '2026-04-17 16:00'
])
df2 = pd.DataFrame({'timestamp': timestamps})
df2['mes']           = df2['timestamp'].dt.month
df2['dia_semana']    = df2['timestamp'].dt.day_name()
df2['flag_fim_semana'] = (df2['timestamp'].dt.dayofweek >= 5).astype(int)
print(df2)

print("\n" + "=" * 55)
print("EXERCÍCIO 3 - Flag de feriado/evento comercial")
print("=" * 55)
FERIADOS_EVENTOS = {
    date(2026, 12, 25): 'Natal',
    date(2026, 11, 27): 'Black Friday',
    date(2026,  1,  1): 'Ano Novo',
    date(2026,  4, 21): 'Tiradentes',
}
transacoes = pd.DataFrame({'data_transacao': pd.to_datetime([
    '2026-12-25', '2026-11-27', '2026-04-15', '2026-01-01', '2026-06-10'
])})
transacoes['flag_evento'] = transacoes['data_transacao'].dt.date.map(
    lambda d: 1 if d in FERIADOS_EVENTOS else 0
)
transacoes['nome_evento'] = transacoes['data_transacao'].dt.date.map(
    lambda d: FERIADOS_EVENTOS.get(d, 'Normal')
)
print(transacoes)

print("\n" + "=" * 55)
print("EXERCÍCIO 4 - Modelo RFM (Recência, Frequência, Valor Monetário)")
print("=" * 55)
historico = pd.DataFrame({
    'id_cliente': [1, 1, 2, 2, 2, 3, 1, 3],
    'data':       pd.to_datetime(['2026-03-01','2026-03-15','2026-02-10',
                                  '2026-03-20','2026-04-01','2026-01-05',
                                  '2026-04-10','2026-03-25']),
    'valor':      [150.0, 200.0, 80.0, 120.0, 300.0, 90.0, 250.0, 175.0]
})
data_ref = pd.Timestamp('2026-04-26')
rfm = historico.groupby('id_cliente').agg(
    Recencia   = ('data', lambda x: (data_ref - x.max()).days),
    Frequencia = ('data', 'count'),
    Monetario  = ('valor', 'sum')
).reset_index()
print(rfm)

print("\n" + "=" * 55)
print("EXERCÍCIO 5 - Delta e Evolução Percentual de sensor")
print("=" * 55)
leitura_t1 = 45.2
leitura_t2 = 52.8
delta = leitura_t2 - leitura_t1
evolucao_pct = (delta / leitura_t1) * 100
tendencia = 'CRESCIMENTO' if delta > 0 else 'QUEDA'
print(f"Leitura T1: {leitura_t1}  |  Leitura T2: {leitura_t2}")
print(f"Delta: {delta:.2f}")
print(f"Evolução %: {evolucao_pct:.2f}%")
print(f"Tendência: {tendencia}")

print("\n" + "=" * 55)
print("EXERCÍCIO 6 - Razão de Comprometimento (Dívida / Renda)")
print("=" * 55)
credito = pd.DataFrame({
    'cliente':      ['A', 'B', 'C', 'D'],
    'divida_total': [3000, 8000, 1500, 15000],
    'renda_mensal': [5000, 6000, 4000, 7000]
})
credito['razao_comprometimento'] = credito['divida_total'] / credito['renda_mensal']
credito['risco'] = pd.cut(credito['razao_comprometimento'],
                          bins=[0, 0.3, 0.6, float('inf')],
                          labels=['Baixo', 'Médio', 'Alto'])
print(credito)
print("\nJustificativa: a razão captura a pressão financeira relativa.")
print("Um cliente com dívida de R$8.000 e renda de R$6.000 é mais arriscado")
print("que um com dívida de R$15.000 e renda de R$50.000.")

print("\n" + "=" * 55)
print("EXERCÍCIO 7 - Indicador de Omissão (Flag NaN) antes do fillna")
print("=" * 55)
df7 = pd.DataFrame({
    'id':    [1, 2, 3, 4, 5],
    'valor': [10.0, np.nan, 15.0, np.nan, 12.0]
})
df7['flag_omissao'] = df7['valor'].isna().astype(int)
df7['valor'] = df7['valor'].fillna(df7['valor'].median())
print(df7)

print("\n" + "=" * 55)
print("EXERCÍCIO 8 - Ranking Interno de volume de vendas")
print("=" * 55)
df8 = pd.DataFrame({
    'produto': ['Mouse', 'Teclado', 'Monitor', 'SSD', 'Headset'],
    'volume':  [320, 180, 95, 260, 140]
})
df8['ranking'] = df8['volume'].rank(ascending=False).astype(int)
df8 = df8.sort_values('ranking')
print(df8)

print("\n" + "=" * 55)
print("EXERCÍCIO 9 - Categorizar horário em Turnos")
print("=" * 55)
logs = pd.DataFrame({'horario': [0, 3, 6, 9, 12, 14, 18, 20, 22, 23]})
def classificar_turno(h):
    if 0 <= h < 6:
        return 'Madrugada'
    elif 6 <= h < 18:
        return 'Comercial'
    else:
        return 'Noite'

logs['turno'] = logs['horario'].apply(classificar_turno)
print(logs)

print("\n" + "=" * 55)
print("EXERCÍCIO 10 - Delta do Delta (aceleração) + alerta binário")
print("=" * 55)
leituras = [10, 12, 15, 19, 24, 31, 40, 52, 67, 87]
df10 = pd.DataFrame({'leitura': leituras})
df10['delta1'] = df10['leitura'].diff()
df10['delta2'] = df10['delta1'].diff()
# Alerta: aceleração crescente (delta2 > 0 e delta1 crescendo)
df10['alerta_exponencial'] = ((df10['delta2'] > 0) & (df10['delta1'] > 0)).astype(int)
print(df10)
print("\nLinhas com alerta de crescimento exponencial:")
print(df10[df10['alerta_exponencial'] == 1])
