from banco import banco_delas, conta_corrente_comum, conta_corrente_especial

print ('------------------------------------------------------------')
print (' *******     Bem vindo ao BANCO DELAS        ***************')
print ('Clientes mulheres possuem acesso cheque especial!!!')
print ('------------------------------------------------------------\n')  


cliente = conta_corrente_especial('Isadora', '3923-9000', 5000, 2)
print ('Nova cliente feminina :')

print ('Depósito:----------------------------------------------') 
cliente.deposito(1000)
print ('\n\nSaque com saldo:----------------------------------------------') 
cliente.saque(900,2)
print ('\n\nSaque com saldo especial:----------------------------------------------') 
cliente.saque(5000,2)


cliente2 = conta_corrente_comum('Igor', '3000-9000', 5000, 1)
print ('Novo cliente masculino :')
print ('Depósito:----------------------------------------------') 
cliente2.deposito(1000)
print ('\n\nSaque com saldo:----------------------------------------------') 
cliente2.saque(900,1)
print ('\n\nSaque com saldo especial:----------------------------------------------') 
cliente2.saque(5000,1)
