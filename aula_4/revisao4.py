


import os
os.system('clear')

#################################################################################
# 03 - Somente numeros pares
def par(x):
	if x % 2 == 0:
 		return True
	return False

def incrementar(x):
	return x + 1

def gerar_lista_numeros_pares(numero):
	return [ (i + 1) for i in range(numero) if par(i + 1) ]

print(' ')
print(' ')
print(' <<< Número(s) Par(es) >>>')
print(' ')
lista_de_numeros_pares = gerar_lista_numeros_pares(10)
for numero in lista_de_numeros_pares:
	if not par(numero):
		raise Exception('{} não é um número par'.format(numero))

print(lista_de_numeros_pares)
print(' ')
print(' ')

exit()
#################################################################################
#################################################################################



#################################################################################
# 01
def gerar_lista(numero):
	lista, x = [], 1
	while x <= numero:
		lista.append(x)
		x = x +1
	return lista

#################################################################################
# 02
def gerar_lista(numero):
	lista = []
	for i in range(numero):
		lista.append(i +1)
	return lista

#################################################################################
# 03
def gerar_lista(numero):
	return [ i +1 for i in range(numero)]

gerar_lista = lambda n: [ i + 1 for i in range(n)]

