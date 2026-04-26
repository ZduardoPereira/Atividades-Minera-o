import pandas as pd
import random

random.seed(2)

df_cursos = pd.DataFrame({
    'id_curso': [1, 2, 3],
    'nome_curso': ['Redes de Computadores', 'Ciência de Dados', 'Segurança da Informação'],
    'duracao_horas': [360, 480, 400]
})

df_disciplinas = pd.DataFrame({
    'id_disciplina': range(1, 10),
    'nome_disciplina': ['Fundamentos de Redes', 'TCP/IP', 'Cabeamento Estruturado',
                        'Python para Dados', 'Machine Learning', 'Visualização de Dados',
                        'Criptografia', 'Ethical Hacking', 'Forense Digital'],
    'id_curso': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'carga_horaria': [60, 80, 60, 80, 100, 80, 80, 100, 80]
})

df_professores = pd.DataFrame({
    'id_professor': range(1, 7),
    'nome_professor': ['Prof. Almeida', 'Prof. Beatriz', 'Prof. Carlos',
                       'Prof. Diana', 'Prof. Eduardo', 'Prof. Fernanda'],
    'especialidade': ['Redes', 'Redes', 'Data Science', 'Data Science', 'Segurança', 'Segurança']
})

df_alunos = pd.DataFrame({
    'id_aluno': range(1, 21),
    'nome_aluno': [f'Aluno {i:02d}' for i in range(1, 21)],
    'id_curso': [random.randint(1, 3) for _ in range(20)]
})

matriculas_rows = []
for m in range(1, 41):
    aluno = random.randint(1, 20)
    id_curso = df_alunos.loc[df_alunos['id_aluno'] == aluno, 'id_curso'].values[0]
    discs = df_disciplinas[df_disciplinas['id_curso'] == id_curso]['id_disciplina'].tolist()
    matriculas_rows.append({
        'id_matricula': m,
        'id_aluno': aluno,
        'id_disciplina': random.choice(discs),
        'id_professor': random.randint(1, 6),
        'nota': round(random.uniform(5.0, 10.0), 1)
    })
df_matriculas = pd.DataFrame(matriculas_rows)

print("=== df_cursos ===")
print(df_cursos)
print("\n=== df_disciplinas ===")
print(df_disciplinas)
print("\n=== df_professores ===")
print(df_professores)
print("\n=== df_alunos ===")
print(df_alunos)
print("\n=== df_matriculas ===")
print(df_matriculas)

# Curso com mais alunos
mais_alunos = df_alunos['id_curso'].value_counts().idxmax()
nome = df_cursos.loc[df_cursos['id_curso'] == mais_alunos, 'nome_curso'].values[0]
print(f"\nCurso com mais alunos: {nome}")
