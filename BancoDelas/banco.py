
# 1 para sexo M  -  2 para sexo F
class banco_delas:
    def __init__(self, nome, telefone, renda_mensal,sexo):
        self.__nome = nome
        self.__telefone = telefone
        self.__renda_mensal = renda_mensal 
        self.__sexo = sexo    
        self.__saldo = 0
   
    
    def saque(self,valor_de_saque,sexo):
        if self.__sexo == 1:
            if self.__saldo > valor_de_saque:
                self.__saldo = self.__saldo - valor_de_saque
            else:
                print('Operação não realizada.')
                print(f'Seu saldo é : {self.__saldo}')
                print(f'O valor solicitado : {valor_de_saque} é superior ao saldo.')

        else:
           
           if self.__saldo > valor_de_saque:
                self.__saldo -= valor_de_saque
                print(f'O Seu saldo atual é de: {self.__saldo}')  
           else:
                
                
                    print(f'Seu saldo atual é de: {self.__saldo}')  
                    self.__saldo -= valor_de_saque 
                    
                    print(f'Operação realizada mediante cheque especial no valor de {self.__renda_mensal}')
                    print(f'Seu novo saldo é de: {self.__saldo}')     
                  
    
    def deposito(self,valor_de_deposito):
        print (f'O saldo atual eh: {self.__saldo} \nValor de deposito:{valor_de_deposito}')
        self.__saldo += valor_de_deposito   
        print(f'O novo saldo da sua conta eh:{self.__saldo}' )

class conta_corrente_comum(banco_delas):
    def __init__(self, nome, telefone, renda_mensal,sexo):
      super().__init__(nome, telefone, renda_mensal,sexo )
      self.titular = nome  
      self.__telefone = telefone
      self.__renda_mensal = renda_mensal

class conta_corrente_especial(banco_delas):
   def __init__(self, nome, telefone, renda_mensal,sexo):
      super().__init__(nome, telefone, renda_mensal,sexo )

      self.titular = nome
      self.__telefone = telefone
      self.__renda_mensal = renda_mensal