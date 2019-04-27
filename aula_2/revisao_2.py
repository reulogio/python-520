
import os
os.system('clear')

lista_de_gatos = [
	{
	   'nome': 'gato' ,
	   'peso': 5000,
	   'idade': 6,
	   'apelido': 'sedoso',
	} 
	, 
	{
	   'nome': 'fernando' ,
	   'peso': 3750,
	   'idade': 3,
	   'apelido': 'brilhoso',
	}
]

'''
def get_input_as_int(mensagem):
	print('>>>> '+mensagem+'<<<<')
	user_input = input(mensagem)
	for token in user_input:
		print('Caracter Atual: {}'.format(token))
		if token not in '0123456789':
			print('>>>> Encerrando o algoritimo com ERRO !!!!! ( '+mensagem+' )')
			return -1
	print('>>>> Algoritimo executado com SUCESSO !!!!! ( '+mensagem+' )')
	return int(user_input)
	# Solução
	#if user_input.isdigit():
'''

def get_input_as_int(mensagem, erro):
	user_input=input(mensagem)
	try:
		return int(user_input)
	except ValueError:
		raise ValueError(erro)

def tratamento_de_tentativas(numero_tentativas, mensagem, erro):
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
os.system('clear')
valor_retorno = tratamento_de_tentativas(
	3,
	'Caso de Teste: ',
	'Deve ser um Numero !!!! >.<'
	)

print('>>>> Foi Executado com SUCESSO !!!!! ===> {}'.format(valor_retorno))


exit()
'''

#get_input_as_int('Caso de Teste: ', 'Deve ser um Numero !!!! >.<' )

#exit()		


novo_gato = {
	   'nome': input('Digite seu Nome: '),
	   'peso': tratamento_de_tentativas( 5, 'Digite o Peso: ', 'O Peso deve ser numero maior que 0'),
	   'idade': tratamento_de_tentativas( 3, 'Digite a Idade: ', 'A Idade deve ser um numero maior que 10'),
	   'apelido': input('Digite o Apelido: ') ,
}

lista_de_gatos.append(novo_gato)


for gato in lista_de_gatos:
	print('Peso do Gato: {}'.format(gato['peso']))
	if gato['peso'] >  4000:
		print('Esse é o gato')
	else:
		print('Ela é Malawi')



exit()

import os
os.system('clear')

print('helo.world')

