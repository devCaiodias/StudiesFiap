#  class em python
class Retaurante:
    
    restaurantes = []

    #  Todos atributos obrigatorio
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Retaurante.restaurantes.append(self)

    # Para transforma a resposta em texto
    def __str__(self):
        return f'{self.nome} e {self.categoria}'
    
    # Criando meu proprio metado
    def listar_restaurante():
        for restaurante in Retaurante.restaurantes:
            print(f'{restaurante.nome} & {restaurante.categoria} & {restaurante.ativo}')



# Chamando a class com os atributos
restaurante_praca = Retaurante('Praça', 'Gourmet')
restaurante_pizza = Retaurante('Pizza', 'Italiana')

Retaurante.listar_restaurante()