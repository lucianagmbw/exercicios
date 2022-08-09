
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

    def ocupar(self, placa):
        self.placa = placa
        self.livre = False

    def desocupar(self, placa):
        self.placa = placa
        self.livre = True


class Estacionamento:
    def __init__(self) -> None:

        self.vagas_de_carro = []
        self.vagas_de_moto = []
        self.carro_para_vaga = 1
        self.moto_para_vaga = 1
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5
        #self.exibir_vagas()

    def exibir_vagas(self):
        tipo = 'carro'
        
        for i in range(self.total_vagas_livres_carro):
            self.vagas_de_carro[i] =  Vaga(i, i, tipo)

        tipo = 'moto'
        for j in range(self.total_vagas_livres_moto):
            self.vagas_de_moto[j] = Vaga(j, j, tipo)

    def estacionar_carro(self, carro: Carro):
        if carro.estacionado is False:
            if self.total_vagas_livres_carro > 0:

                vaga = self.vagas_de_carro[self.total_vagas_livres_carro]
                vaga.ocupar(carro.placa)

                carro.estacionar(vaga)
                self.total_vagas_livres_carro -= 1

    def estacionar_moto(self, moto: Moto):
        if moto.estacionado is False:
            if self.total_vagas_livres_carro < 0:

                vaga = self.vagas_de_carro[self.total_vagas_livres_carro]
                vaga.ocupar(moto.placa)

                moto.estacionar(vaga)
                self.total_vagas_livres_moto -= 1

    def remover_carro(self, carro:Carro):
        if carro.estacionado is True:
               
            vaga = self.vagas_de_carro[self.total_vagas_livres_carro]
            vaga.desocupar(carro.placa)
            carro.sair_da_vaga(vaga)
            self.total_vagas_livres_carro += 1

    def remover_moto(self , moto:Moto):
        if moto.estacionado is True:
               
            vaga = self.vagas_de_moto[self.total_vagas_livres_moto]
            vaga.desocupar(moto.placa)
            moto.sair_da_vaga(vaga)
            self.total_vagas_livres_moto += 1
        

    def estado_do_estacionamento(self):
        num_carros_estacionados = 5 - self.total_vagas_livres_carro 
        num_motos_estacionadas = 5 -  self.total_vagas_livres_moto

        print ( f'  Total de vagas livres de carros: {self.total_vagas_livres_carro}\n')
        print ( f'  Total de vagas livres de motos: {self.total_vagas_livres_moto}\n')
        print ( f'  Num carros estacionados: {num_carros_estacionados}\n')
        print ( f'  Num motos estacionadas: {num_motos_estacionadas}\n')

     
    def __str__(self):

        return self.estado_do_estacionamento()


carro = Carro('LHL3256' )
moto = Moto('MZM' )
e = Estacionamento()
e.estado_do_estacionamento()