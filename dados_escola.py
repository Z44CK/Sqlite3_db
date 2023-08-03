import sqlite3

banco = sqlite3.connect('escola_banco.db')

cursor = banco.cursor()

cursor.execute("""CREATE TABLE Alunos(
                id_alunos INTEGER PRIMARY KEY NOT NULL,
                nome_alunos VARCHAR NOT NULL,
                cpf_alu INTEGER NOT NULL
                )""")

cursor.execute("""CREATE TABLE Professores(
                id_professores INTEGER PRIMARY KEY NOT NULL,
                nome_professores VARCHAR NOT NULL,
                cpf_prof INTEGER NOT NULL
                )""")

cursor.execute("""CREATE TABLE Disci_offer(
                id_disci INTEGER PRIMARY KEY NOT NULL,
                nome_disci VARCHAR NOT NULL,
                carg_horaria TEXT NOT NULL
                )""")

cursor.execute("""CREATE TABLE Turmas(
                id_turma INTEGER PRIMARY KEY NOT NULL,
                titulo VARCHAR NOT NULL,
                ano_disci INTEGER NOT NULL
                )""")

cursor.execute("""CREATE TABLE Disci_turma(
                id_disc_turmas INTEGER PRIMARY KEY NOT NULL,
                id_disc INTEGER KEY NOT NULL,
                id_professor INTEGER NOT NULl,
                id_turma INTEGER NOT NULL,
                horario VARCHAR NOT NULL
                )""")

cursor.execute("""CREATE TABLE Historico(
                id_historico INTEGER PRIMARY KEY NOT NULL,
                id_aluno INTEGER NOT NULL)""")

cursor.execute("""CREATE TABLE Hist_disci(
                id_hist_disci INTEGER PRIMARY KEY NOT NULL,
                id_disci INTEGER NOT NULL,
                nota REAL NOT NULL,
                id_historico INTEGER NOT NULL)""")

banco.commit()
