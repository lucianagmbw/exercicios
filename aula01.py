#nome= input('qual é o seu nome?')
#print(nome)
#idade = input('qual é a sua idade')
#print(idade)



class Pessoa: 
    def __init__(self,nome) -> None:
        self.nome = nome

        self.tipo = Pessoa

    def falar_oi(self):
        print ('oi,meu nome é {}'.format(self._nome))

    def falar_tipo(self):
        print ('oi,meu tipo é {}'.format(self._tipo))

pessoa = Pessoa('Maria')
pessoa.falar_tipo()
pessoa.falar_oi()        

class Estudante (Pessoa):
    def __init__(self, nome,curso) -> None:
        super().__init__(nome)
        self._curso = curso
    
    def falar_curso(self):
        print  (f'Eu,{self._nome}, estudo o  cusrso {self._curso}')

    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()

    estudante = ('Yasmin', 'Introdução ao Python') 
    estudante.falar_oi() # o método "falar_oi" é herdado da classe base 
    estudante.falar_tipo() #o método "falar_tipo" é herdado da classe base, e sobreescrito na classe derivada 
    estudante.falar_curso()   


