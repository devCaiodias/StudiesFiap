from modulos.avaliacao import Avaliacao

#  class em python
class Restaurante:
    
    restaurantes = []

    #  Todos atributos obrigatorio
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        # lista de avalicao
        self._avalicao = []
        Restaurante.restaurantes.append(self)

    # Para transforma a resposta em texto
    def __str__(self):
        return f'{self._nome} e {self._categoria}'
    
    
    @classmethod
    # Criando meu proprio metado
    def listar_restaurante(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avalicao).ljust(25)} | {restaurante._ativo}')


    @property
    # metado get na teoria
    def ativo(self):
        return True if self._ativo else False
    
    # metado set na teoria
    def alternar_estado(self):
        self._ativo = not self._ativo

    # recebendo avalicao do cliente
    def receber_avaliacao(self, cliente, nota):
        avalicaoo = Avaliacao(cliente, nota)
        self._avalicao.append(avalicaoo)

    # metado property das media da avalicao
    @property
    def media_avalicao(self):
        # se n tiver nem uma avalicao retorna 0
        if not self._avalicao:
            return round(0, 1)
        # soma das notas
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avalicao)
        # quantidade de avalicao
        quantidade_de_avaliacao = len(self._avalicao)
        # media das notas
        media = round(soma_das_notas / quantidade_de_avaliacao, 1)
        return media