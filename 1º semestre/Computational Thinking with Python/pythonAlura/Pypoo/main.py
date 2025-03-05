#  class em python
class Retaurante:
    
    restaurantes = []

    #  Todos atributos obrigatorio
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Retaurante.restaurantes.append(self)

    # Para transforma a resposta em texto
    def __str__(self):
        return f'{self._nome} e {self._categoria}'
    
    
    @classmethod
    # Criando meu proprio metado
    def listar_restaurante(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')


    @property
    # metado get na teoria
    def ativo(self):
        return True if self._ativo else False
    
    # metado set na teoria
    def alternar_estado(self):
        self._ativo = not self._ativo



# Chamando a class com os atributos
restaurante_praca = Retaurante('praça', 'Gourmet')
# alterando o estado do ativo
restaurante_praca.alternar_estado()
restaurante_pizza = Retaurante('pizza', 'Italiana')

Retaurante.listar_restaurante()
