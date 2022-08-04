class Carro:
    def __init__(self):
        self.ligado = True
        self.cor = 'branco'
        self.modelo ='chevrolet'
        self.velocidade= 0
        self.velocidade_maxima=200
        self.velocidade_minima=0
    
    def ligar_carro(self):        
        self.ligado = True
        print ('Ligando carro: ', {self.ligado})
        

    def desligar_carro(self):
        if not self.ligado:
            print('O carro já está desligado...')
            return
        if self.ligado:
            self.ligado = False
            print ('O carro foi desligado', self.ligado)    
    
    def acelerar_carro(self):
        print ('velocidade do carro:',self.velocidade,'km/h')
        
        if self.velocidade < self.velocidade_maxima:
            if self.velocidade < self.velocidade_maxima - 5:
                self.velocidade += 5
                print('Aumentando em mais 5km/h ', ' velocidade:',{self.velocidade},'km/h') 
            else:
                if self.velocidade < self.velocidade_maxima -1:
                    self.velocidade +=1
                    print('Aumentando em mais 1km/h ', {self.velocidade},'km/h') 

    def desacelerar_carro(self):
        print ('velocidade do carro:',{self.velocidade},'km/h')
        if self.velocidade > self.velocidade_minima :
            if self.velocidade >= self.velocidade_minima + 5:
                self.velocidade -= 5
                print('Diminuindo em  5km/h ','velocidade:',self.velocidade,'km/h')
            else:
                if self.velocidade != self.velocidade_minima:
                    self.velocidade -=1    
                    print('Diminuindo em 1km/h ', 'velocidade:',self.velocidade,'km/h') 
          
    def __str__(self) -> str:
        
        f'Carro: - ligado {self.ligado} - cor {self.cor} - modelo{self.modelo} - velocidade{self.velocidade}km/h - velocidade_max {self.velocidade_maxima} - velocidade_min{self.velocidade_minima}'

       

#criando carro
novo_carro = Carro()

#ligando o carro e acelerando 
print ('LIGANDO O CARRO E ACELERANDO ')
novo_carro.ligar_carro()
print('------------------------------')
novo_carro.acelerar_carro()   
   
print('------------------------------')
#fazendo o carro desacelerar 
print ('FAZENDO O CARRO DESACELERAR')
novo_carro.desacelerar_carro()
print('------------------------------')

print  ('DESLIGANDO O CARRO')
novo_carro.desligar_carro()

