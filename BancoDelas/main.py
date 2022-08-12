from banco import banco_delas, conta_corrente_comum, conta_corrente_especial

print ('------------------------------------------------------------')
print (' *******     Bem vindo ao BANCO DELAS        ***************')
print ('Clientes mulheres possuem acesso cheque especial!!!')
print ('------------------------------------------------------------')  

print ('novo cliente :')
cliente = conta_corrente_especial('Isadora', '3923-9000', 5000, 2)
#print (f'Nome: {cliente.titular}\n , telefone:{cliente.__telefone}\n,renda:{cliente.__renda_mensal}')
print (vars(cliente))