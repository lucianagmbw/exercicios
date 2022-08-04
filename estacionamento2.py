
class Estacionamento:
    def __init__(self) -> None:
       
        self.vagas_de_carro = 5
        self.vagas_de_moto = 5
        self.carro_para_vaga =1
        self.moto_para_vaga =1
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

    def estacionar_carro(self):
        
        return 

    def estacionar_moto(self):

        return

    def remover_carro(self):

        return

    def remover_moto(self):

        return  

    def estado_do_estacionamento(self):

        return

    class Vaga:
        def __init__(self,placa,tipo) -> None:
            self.id = 1 
            self.tipo = tipo #vaga-de_carro ou vaga_de_moto
            self.livre = True
            self.placa = placa

        def ocupar(self):
            self.id = self.id
            self.id += self.id

            return

        def desocupar():
            
            return    


    class Carro:
        def __init__(self,placa) -> None:

            self.placa = placa
            self.estacionado = False

        def estacionar(self,Vaga):
            if self.estacionado:
                return
            
            self.estacionado = True


        def sair_da_vaga(self,Vaga):
            if self.estacionado:
                self.estacionado = False
                
                return                           


    
    class Moto:
        def __init__(self,placa) -> None:

            self.placa = placa
            self.estacionado = False
        
        def estacionar(self,Vaga):
            if self.estacionado:
                return
            
            self.estacionado = True


        def sair_da_vaga(self,Vaga):
            if self.estacionado:
                self.estacionado = False
                
                return        
                                
            



    carro = Carro ('LHL3256' )
    carro.estacionar()
    carro.sair_da_vaga()    



    moto = Moto ('MZM')
    moto.estacionar()
    moto.sair_da_vaga()
