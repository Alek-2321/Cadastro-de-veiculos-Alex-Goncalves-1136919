from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano,CapCarga):
        super().__init__(marca, modelo, placa, ano)
        self.__CapCarga = CapCarga
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
    - Cap. Carga:{self.__CapCarga}'''