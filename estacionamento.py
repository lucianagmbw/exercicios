
class Estacionamento:
    def __init__(self,Carro, Moto,Vaga) -> None:
       
        self.vagas_de_carro = 25
        self.vagas_de_moto = 25
        self.carro_para_vaga = Carro
        self.moto_para_vaga = Moto
        self.total_vagas_livres_carro = 25
        self.total_vagas_livres_moto = 25

    def estacionar_carro(self,Carro):
        if self.total_vagas_livres_carro == 0:
            print ('não há vagas disponíveis - total:  {}'.format(self.total_vagas_livres_carro))
             
           
        self.total_vagas_livres_carro -= 1
           
        return 
      
          
    

class Vaga:
    def __init__(self,Veiculo) -> None:
        super().__init__(self,Veiculo) 
        self.id = input('Número do id: ')
        self.tipo = Veiculo.tipo
        self.livre = True
        self.placa = Veiculo.placa
#def para ocupar /desocupar
    def ocupar(self):
     
        return super().estacionar()

    def desocupar(self):
        
        return super().sair_da_vaga()
       

class Veiculo: 
    def __init__(self,placa,estacionado) -> None:
        self.placa = placa
        self.estacionado = True

        self.tipo = Veiculo
    
    def estacionar(self):
        print ('Estou estacionado? - {}'.format(self.estacionado))

    def sair_da_vaga(self):
        print ('oi,meu tipo é {}'.format(self.tipo))
        

class Carro (Veiculo):
    def __init__(self, placa,estacionado) -> None:
        super().__init__(placa,estacionado)
        #se tiver mais metodos coloca aqui...
        self.tipo = Carro

    def estacionar(self):
       return super().estacionar()

    def sair_da_vaga(self):
      #  self._tipo = 'sair da vaga'
        return super().sair_da_vaga()



class Moto (Veiculo):
    def __init__(self, placa,estacionado) -> None:
        super().__init__(placa,estacionado)
        #se tiver mais metodos coloca aqui...
        self.tipo = Moto
    
    def estacionar(self):
      
       return super().estacionar()

    def sair_da_vaga(self):
     
        return super().sair_da_vaga()




carro = Carro('LHL3256' , True )
carro.estacionar()
carro.sair_da_vaga()    



moto = Moto('MZM' , True)
moto.estacionar()
moto.sair_da_vaga()


#e = Estacionamento(carro,moto,Vaga)
#e.estacionar_carro(carro)


