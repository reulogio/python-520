
import os
os.system('clear')

import pymongo

client = pymongo.MongoClient()

db = client.projeto

#db.users.insert({ 'nome': 'Roberto'})

def extrair_usuarios():
	return list(db.users.find())

def cadastrar_usuario(nome, email, idade):
#	for usuario in extrair_usuarios():
#		db.users.remove(usuario)
	usuario = db.users.find_one({ 'email' : email })
	if not usuario:
		db.users.insert({ 'nome': nome, 'email': email, 'idade': idade })

cadastrar_usuario(
	'Roberto Eulogio Pinto',
	'eulogio@terra.com.br',
	54
)

for usuarios in extrair_usuarios():
	print(usuarios)

