

import os
os.system('clear')

class Usuario:
	def __init__(self, nome, email, idade):
		self.nome = nome
		self.email = email
		self.idade = idade

	def maior_de_idade(self):
		if self.idade > 17:
			return True
		return False

class Cadastrador:

	def cadastrar_usuario(self):

		nome  = input('Digite seu Nome : ')
		email = input('Digite o E-mail : ')
		idade = int(input('Digite a Idade  : '))

		return Usuario(nome, email, idade)

cadastrador = Cadastrador()

usuario = cadastrador.cadastrar_usuario()
l
if not usuario.maior_de_idade():
	print('Requer mais de 18 anos')
else:
	print('Permitido')