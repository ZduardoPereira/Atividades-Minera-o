import pandas as pd
import random

random.seed(4)

df_usuarios = pd.DataFrame({
    'id_usuario': range(1, 11),
    'nome_usuario': ['Alice Borges', 'Carlos Lima', 'Daniela Souza', 'Eduardo Pires',
                     'Fernanda Cruz', 'Gabriel Azev', 'Helena Rocha', 'Igor Santos',
                     'Juliana Mota', 'Klaus Ferreira'],
    'departamento': ['RH', 'TI', 'Financeiro', 'Logística', 'RH',
                     'Financeiro', 'TI', 'Logística', 'RH', 'TI']
})

sistemas_operacionais = ['Windows 10', 'Windows 11', 'Ubuntu', 'Windows 10', 'Windows 11',
                         'macOS', 'Windows 10', 'Ubuntu', 'Windows 11', 'Windows 10']
df_equipamentos = pd.DataFrame({
    'id_equipamento': range(1, 11),
    'id_usuario': range(1, 11),
    'modelo': [f'Modelo-{chr(65+i)}' for i in range(10)],
    'sistema_operacional': sistemas_operacionais,
    'ram_gb': [8, 16, 8, 32, 8, 16, 16, 8, 32, 8]
})

tickets_rows = []
for i in range(1, 31):
    tickets_rows.append({
        'id_ticket': i,
        'id_usuario': random.randint(1, 10),
        'id_equipamento': random.randint(1, 10),
        'categoria': random.choice(['Hardware', 'Software', 'Rede', 'Acesso']),
        'horas_resolucao': round(random.uniform(0.5, 12.0), 1),
        'status': random.choice(['Resolvido', 'Resolvido', 'Em Aberto'])
    })
df_tickets = pd.DataFrame(tickets_rows)

print("=== df_usuarios ===")
print(df_usuarios)
print("\n=== df_equipamentos ===")
print(df_equipamentos)
print("\n=== df_tickets ===")
print(df_tickets)

# OS com mais chamados
merged = df_tickets.merge(df_equipamentos, on='id_equipamento')
os_problemas = merged['sistema_operacional'].value_counts()
print(f"\nOS com mais chamados: {os_problemas.idxmax()}")
print(os_problemas)

# Usuário que mais consumiu horas de TI
horas_usuario = (df_tickets
                 .merge(df_usuarios, on='id_usuario')
                 .groupby('nome_usuario')['horas_resolucao'].sum()
                 .sort_values(ascending=False))
print(f"\nUsuário que mais consumiu horas de TI: {horas_usuario.idxmax()}")
print(horas_usuario)
