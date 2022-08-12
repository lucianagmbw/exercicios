from typing import List
class Carro:
    def __init__(self, placa) -> None:

        self.placa = placa
        self.estacionado = False

    def estacionar(self, Vaga):
        if self.estacionado:
            return
        self.estacionado = True

    def sair_da_vaga(self, Vaga):
        if self.estacionado:
            self.estacionado = False


class Moto:
    def __init__(self, placa) -> None:

        self.placa = placa
        self.estacionado = False

    def estacionar(self, Vaga):
        if self.estacionado:
            return

        self.estacionado = True

    def sair_da_vaga(self, Vaga):
        if self.estacionado:
            self.estacionado = False

            


class Vaga:
    
    def __init__(self, id, tipo) -> None:
        self.id = id
        self.tipo = tipo  # vaga-de_carro ou vaga_de_moto
        self.livre = True
        self.placa = None
        self.vagas = [] 
    
    def ocupar(self, placa):
        self.placa = placa
        self.livre = False

    def desocupar(self, placa):
        self.placa = placa
        self.livre = True

   # def adicionar_na_vaga(self,object):
        
      #  self.vagas.append (object)
      #
      #   print (f'veículo estacionado com sucesso!')



class Estacionamento:
    def __init__(self,Vaga,Carro,Moto) -> None: 
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5
        self.vagas =[]
   # def estacionar_carro(self,placa ):
      #  if self.total_vagas_livres_carro > 0 :
          
            
    
    def adicionar_na_vaga(self,object):
        if self.total_vagas_livres_carro > 0 :
           self.vagas.append (object)
           self.total_vagas_livres_carro-=1
        print (f'carro estacionado com sucesso!')        

         



v = Vaga('1','Carro')
carro = Carro('LHL3256')
carro2 = Carro('LHL3256')
moto = Moto ('MMM9090')
#v.adicionar_na_vaga(vars (carro) )
e1 = Estacionamento(v,carro,moto)
e1.adicionar_na_vaga(vars(carro2))
print(e1.vagas)
print('----------------------------------------')
