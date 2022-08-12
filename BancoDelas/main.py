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

