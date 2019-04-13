
# Link : http://dontpad.com/python-520

import os
import random
import string

os.system('clear')

#print('string.asciiletters')

ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gerar_nome_aleatorio():
	string=''
	for n in range(random.randint(5, 15)):
		string += random.choice(ASCII_LETTERS)
	return string

def gerar_email_aleatorio():
	return gerar_nome_aleatorio() + '@4linus.com'

def gerar_idade_aleatorio():
	return random.randint(24, 55)

def gerar_usuario_aleatorio():
	novo_usuario = {
		'nome': gerar_nome_aleatorio(),
		'email': gerar_email_aleatorio(),
		'idade': gerar_idade_aleatorio(),
	}
	return novo_usuario

for i in range(10):
	print('Nome___: ' +gerar_nome_aleatorio())
	print('Email__: ' +gerar_email_aleatorio())
	print('Idade__: ' +str(gerar_idade_aleatorio()))
	print('-------------------------------------------')
