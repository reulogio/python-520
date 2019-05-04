
import datetime
import unittest

import execercicio_1_4 as scooby

'''
print(' ')
print(' ')
print(scooby.Ticket)
print(' ')
print(' ')

class TestCase:
	pass
'''

class CatracaTeste(unittest.TestCase):
	
	def test_0_ticket_vencido(self):
		validade = datetime.datetime.now() - datetime.timedelta(days=2)
		saldo = scooby.PRECO_DA_PASSAGEM + 300.00
		conce = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, conce)

		catraca = scooby.Catraca(conce='sptrans')

		with self.assertRaises(scooby.ErroTicketExpirado):
			catraca.liberar(ticket)
		print(' ')
		print('-----------------------------------------------------')
		print('[ Resultado Final - test_0_ticket_vencido ]')
		print(' ')
		print('* Validade__________: ' + str(ticket.validade))
		print('  Saldo_____________: ' + str(ticket.saldo))
		print('  Concessionaria____: ' + str(ticket.conce))
		print('-----------------------------------------------------')

	def test_1_saldo_insuficiente(self):
		validade = datetime.datetime.now() + datetime.timedelta(days=365)
		saldo = scooby.PRECO_DA_PASSAGEM - 2.00
		conce = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, conce)

		catraca = scooby.Catraca(conce='sptrans')

		with self.assertRaises(scooby.ErroSaldoInsuficiente):
			catraca.liberar(ticket)
		print(' ')
		print('-----------------------------------------------------')
		print('[ Resultado Final - test_1_saldo_insuficiente ]')
		print(' ')
		print('  Validade__________: ' + str(ticket.validade))
		print('* Saldo_____________: ' + str(ticket.saldo))
		print('  Concessionaria____: ' + str(ticket.conce))
		print('-----------------------------------------------------')

	def test_2_Concessionaria_Diferente(self):
		validade = datetime.datetime.now() + datetime.timedelta(days=365)
		saldo = 300.00
		conce = 'emtu'

		ticket = scooby.Ticket(validade, saldo, conce)

		catraca = scooby.Catraca(conce='sptrans')

		with self.assertRaises(scooby.ErroConcessionariaDiferente):
			catraca.liberar(ticket)
		print(' ')
		print('-----------------------------------------------------')
		print('[ Resultado Final - test_2_Concessionaria_Diferente ]')
		print(' ')
		print('  Validade__________: ' + str(ticket.validade))
		print('  Saldo_____________: ' + str(ticket.saldo))
		print('* Concessionaria____: ' + str(ticket.conce))
		print('-----------------------------------------------------')

	def test_3_Fluxo_Feliz(self):
		validade = datetime.datetime.now() + datetime.timedelta(days=365)
		saldo = 300.00
		conce = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, conce)

		catraca = scooby.Catraca(conce='sptrans')

		catraca.liberar(ticket)

		cond_1 = ticket.saldo == ( saldo - scooby.PRECO_DA_PASSAGEM) 
		self.assertTrue(cond_1 , 'Saldo não foi descontado')
		cond_2 = catraca.esta_liberada() 
		self.assertTrue(cond_2 , 'Catraca não foi liberada')
		print(' ')
		print('-----------------------------------------------------')
		print('[ Resultado Final - test_3_Fluxo_Feliz ]')
		print(' ')
		print('  Validade__________: ' + str(ticket.validade))
		print('  Saldo_____________: ' + str(ticket.saldo))
		print('  Concessionaria____: ' + str(ticket.conce))
		print('-----------------------------------------------------')

if __name__ == "__main__":
	unittest.main()
