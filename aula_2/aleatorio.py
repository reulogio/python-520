
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
		'idade': gerar_idade_aleatorio()
	}
	return novo_usuario

#print(gerar_usuario_aleatorio())

if __name__ == '__main__':
	# Tem que recuar as 3 linhas abaixo para primeira coluna para processar com o main2.py r isolar o if anerior
	usuario = gerar_usuario_aleatorio()
	print('Testando o usuário aleatório')
	print(usuario)

'''	
	print('Rode seus testes sem erro de eles atrapalharem')
	print('Arquivo aleatorio.py: {}'.format(__name__))
'''
'''
for i in range(5):
	print(gerar_usuario_aleatorio())
'''
'''
exit()

for i in range(5):
	print(gerar_nome_aleatorio())
	print(gerar_email_aleatorio())
	print(gerar_idade_aleatorio())
'''
'''
print('-----------------------------------------------------------------')
for i in range(5):
	print('Cadastro No.___: ' +str(i+1))
	print('Nome___________: ' +gerar_nome_aleatorio())
	print('Email__________: ' +gerar_email_aleatorio())
	print('Idade__________: ' +str(gerar_idade_aleatorio()))
	print('-----------------------------------------------------------------')
'''