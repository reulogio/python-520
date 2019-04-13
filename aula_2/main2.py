import os
os.system('clear')

import json

import aleatorio as foo

def imprimir_bonito(obj):
	print(json.dumps(obj, indent=2))

def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u = foo.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

#foo.ASCII_LETTERS
lista_de_usuarios = gerar_lista_usuarios(100)

#print('Arquivo main2.py: {}'.format(__name__))

'''
print(len(lista_de_usuarios))

for usuario in lista_de_usuarios:
   if int(usuario['idade']) > 30:
		 imprimir_bonito(usuario)
'''

lista_1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
lista_2 = [ x * 2 for x in lista_1 if x % 2 == 0 ]

print(lista_2)

def gerar_csv(lista):
		TEMPLATE = '{};{};{};'
		CABECALHO = TEMPLATE.format('NOME', 'EMAIL' , 'IDADE')
		print(CABECALHO)
		for usuario in lista:
			usuario_formatado = TEMPLATE.format(
				usuario['nome'],
				usuario['email'],
				usuario['idade']
			)
			print(usuario_formatado)

def filtrar_usuarios(usuario):
	usuario_email=usuario['email'].lower()
	if 'a' in usuario_email or 'd' in usuario_email:
		return True
	return False

gerar_csv( u for u in lista_de_usuarios if filtrar_usuarios(u))


