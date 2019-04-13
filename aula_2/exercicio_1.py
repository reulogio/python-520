
import os
os.system('clear')

import datetime
import subprocess
import time
import random


def get_input_as_int(mensagem, erro):
	user_input=input(mensagem)
	try:
		return int(user_input)
	except ValueError:
		raise ValueError(erro)

def tratamento_de_idade(numero_tentativas, mensagem, erro):
	for tentativa in range(numero_tentativas):
		try:
			return get_input_as_int(mensagem, erro)
		except ValueError as err:
			restantes=numero_tentativas-(tentativa+1)
			print('Um error aconteceu, Você ainda tem {}'.format(restantes)+' tentativa(s)')
			print(err)
	print('Você errou o input {} vezes.'.format(numero_tentativas))
	print('Vou encerrar o programa')			
	exit()

'''
def tratamento_de_email(numero_tentativas, mensagem, erro):
	for tentativa in range(numero_tentativas):
		if '@' not in usuario['email'].lower():  
'''

# limpa tela
subprocess.run([ 'clear'])

# Sleep aguardar 10 segundos
#time.sleep(10.0)

def cadastrar_usuario():
	usuario = {
		   'data_cadastro': datetime.datetime.now(),
		   'nome': input('Digite seu Nome: '),
		   'email': input('Digite o E-mail: '),
	   	   'idade': tratamento_de_idade( 3, 'Digite a Idade: ', 'A Idade deve ser um numero maior que 10'),
	}
	return usuario

#novo_usuario=cadastrar_usuario()

probabilidade = random.random()
if probabilidade < 0.8:
	cadastrar_usuario()
else:
	print('Opa, não deu sorte......')

exit()


# Calcula o Tempo de Processo (PRODUÇÃO)
start_time = time.clock()
time.sleep(10.0)
print('Tempo gato = {}'.format(time.clock() - start_time))


d = novo_usuario['data_cadastro']
print(d.strftime('%B %d, %Y'))
print(d.strftime('São Paulo, %d de %B de %Y'))

print(novo_usuario)

