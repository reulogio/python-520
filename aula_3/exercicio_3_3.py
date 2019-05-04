

import os
os.system('clear')


import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
	user='admin',
	password='4linux',
	host='127.0.0.1',
	database='projeto'
	)

cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

#cursor.execute("INSERT INTO scripts (nome, conteudo) VALUES ('Bom dia', 'Como Vai?)');")

#cursor.execute('SELECT * FROM scripts;')
#for resultado in cursor.fetchall():
#	print(resultado)
#		DELETE FROM users WHERE email = email;

def cadastrar_usuario(nome, email, idade):

	email_nao_existe = True
	cursor.execute('''
		SELECT * FROM users WHERE EMAIL = '{}'
		'''.format(email))

	results = cursor.fetchall()

	print(lenresults)

	if len(results) == 0:
		cursor.execute('''
			INSERT INTO users (nome, email, idade)
			VALUES ( '{}','{}', {});
			'''.format(nome, email, idade))
		conn.commit()

def extrair_usuarios():
	cursor.execute('SELECT * FROM users;')
	return cursor.fetchall

cadastrar_usuario(
	'Roberto Eulogio Pinto',
	'eulogio@terra.com.br',
	54
)

cursor.execute('SELECT * FROM users;')
for resultado in cursor.fetchall():
	print(resultado)