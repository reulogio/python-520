
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
	pass

class ErroConcessionariaDiferente(Exception):
	pass

class ErroSaldoInsuficiente(Exception):
	pass
	

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
		self.conce = conce
		self.estado = 'travada'

	def esta_liberada(self):
		if self.estado == 'liberada':
			return True
		return False

	def liberar(self, ticket):
		if ticket.validade < datetime.datetime.now():
			raise ErroTicketExpirado

		if ticket.saldo < PRECO_DA_PASSAGEM:
			raise ErroSaldoInsuficiente

		if ticket.conce != self.conce:
			raise ErroConcessionariaDiferente

		ticket.saldo = ticket.saldo - PRECO_DA_PASSAGEM
		self.estado='liberada'
		

###############################################################################################
# Testes - Data Vencida / Concessionaria / Saldo / Catraca Liberada
###############################################################################################

######################
# Teste Data Vencida #
######################
print(' ')
print('---------------------------------------------')
try:

	validade = datetime.datetime.now() - datetime.timedelta(days=2)
	saldo = 300.00
	conce = 'sptrans'

	ticket = Ticket(validade, saldo, conce)

	catraca = Catraca(conce='sptrans')

	catraca.liberar(ticket)

	print(ticket.validade)
	print(ticket.saldo)
	print(ticket.conce)
	print(' >>> Bug Encontrado (Ticket)')

except ErroTicketExpirado:
	print(' >>> Teste de ticket expirado ok')

########################
# Teste Concessionaria #
########################
print('---------------------------------------------')
try:

	validade = datetime.datetime.now() + datetime.timedelta(days=365)
	saldo = 300.00
	conce = 'emtu'

	ticket = Ticket(validade, saldo, conce)

	catraca = Catraca(conce='sptrans')

	catraca.liberar(ticket)

	print(ticket.validade)
	print(ticket.saldo)
	print(ticket.conce)
	print(' >>> Bug Encontrado (Concessionaria)')

except ErroConcessionariaDiferente:
	print(' >>> Teste de Concessionaria diferente ok')

###############
# Teste Saldo #
###############
print('---------------------------------------------')
try:

	validade = datetime.datetime.now() + datetime.timedelta(days=365)
	saldo = PRECO_DA_PASSAGEM - 1.00
	conce = 'sptrans'

	ticket = Ticket(validade, saldo, conce)

	catraca = Catraca(conce='sptrans')

	catraca.liberar(ticket)

	print(ticket.validade)
	print(ticket.saldo)
	print(ticket.conce)
	print(' >>> Bug Encontrado (Saldo)')

except ErroSaldoInsuficiente:
	print(' >>> Teste Saldo Insuficiente ok')

##########################
# Teste Catraca Liberada #
##########################
print('---------------------------------------------')

validade = datetime.datetime.now() + datetime.timedelta(days=365)
saldo = 300.00
conce = 'sptrans'

ticket = Ticket(validade, saldo, conce)

catraca = Catraca(conce='sptrans')

catraca.liberar(ticket)

try:
	assert ticket.saldo == ( saldo - PRECO_DA_PASSAGEM)
	assert catraca.esta_liberada()

	print(' >>> Teste de Fluxo Feliz ok')

except:
	print(ticket.validade)
	print(ticket.saldo)
	print(ticket.conce)
	print(' >>> Bug Encontrado (Catraca)')

print('---------------------------------------------')
print(' ')
print(' ')
print('---------------------------------------------')
print(' ')
print('       [ Resultado Final ]')
print(' ')
print(ticket.validade)
print(ticket.saldo)
print(ticket.conce)
print(' ')
print('---------------------------------------------')
print(' ')
print(' ')
