
import os
os.system('clear')

try:
	idade = int(input('Digite sua Idade: '))
	print('Sua idade é {}'.format(idade))
except:
	print('Idade Invalida')

print('Sempre será executado')

exit()

variavel = 5

variavel = 5 + 5


def soma (a , b):
	 return a + b

variavel = soma(5, 5)

apelido=soma
variavel = apelido(2,2)

resultado_boll = variavel < 10

if resultado_boll < 10:
	print('True')
elif variavel < 5:
	print('Menor que 5')
else:
	print('Maior que 5')

lista_de_numeros = [ 1,2,3,4,5 ]
for numero in lista_de_numeros:
	if numero % 2 == 0:
		print('Par')
	else:
		print('Impar')

for letra in 'Roberto Eulogio Pinto':
	if letra == 'o' or letra == 'r':
		print(letra)

x = 0
while x < 10:
	print('Helo, World de novo')
	x += 1 # ou x = x +1

try:
	idade = int(input('Digite sua Idade: '))
	print('Sua idade é {}'.format(idade))
except:
	print('Idade Invalida')
finally:
	print('Sempre será executado')

