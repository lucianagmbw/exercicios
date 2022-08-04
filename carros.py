class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'branco'
        self.modelo ='chevrolet'
        self.velocidade='200km/h'
    
    def ligar_carro(self):
        self.ligado = True
        return

    def desligar(self):
        self.ligar = False
    
    def acelera(self):
        self.acelera = True

    def desacelera(self):
        self.acelera = False

#criando carro
novo_carro = Carro()

#fazendo o carro andar 
print ('Ligando carro: ', {novo_carro.ligado})        
print (f'Ligando carro: ', {novo_carro.ligar_carro()})  

#fazendo o carro parar
