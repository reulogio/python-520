
import datetime

import os
os.system('clear')

###############################################################################################
'''

   Quando usuario passar ticket validar [ valor (saldo) / validade (data) / valido (região) ]

'''

###############################################################################################
# Constantes
###############################################################################################

PRECO_DA_PASSAGEM = 4.00

###############################################################################################
# Erros
###############################################################################################

class ErroTicketExpirado(Exception):
	

###############################################################################################
# Classes
###############################################################################################

class Ticket:

	def __init__(self, validade, saldo, conce):
		self.validade = validade
		self.saldo = saldo
		self.conce = conce

class Catraca:

	def __init__(self, conce):
		self.estado = 'travada'
		self.conce = conce

	def liberar(self, ticket):
		pass	
		

###############################################################################################
# Testes
###############################################################################################

validade = datetime.datetime.now()
saldo = 300.00
conce = 'sptrans'

try:

	validade = datetime.datetime.now() - datetime.timedelta(days=2)
	saldo = 300.00
	conce = 'sptrans'

	ticket = Ticket(validade, saldo, conce)

	catraca = Catraca(conce='sptrans')

	catraca.liberar(ticket)

except ErroTicketExpirado:
	print('Teste de ticket expirado ok')


try:

	validade = datetime.datetime.now() - datetime.timedelta(days=2)
	saldo = 0.00
	conce = 'sptrans'

	ticket = Ticket(validade, saldo, conce)

	catraca = Catraca(conce='sptrans')

	catraca.liberar(ticket)

except ErroTicketExpirado:
	print('Teste de ticket expirado ok')