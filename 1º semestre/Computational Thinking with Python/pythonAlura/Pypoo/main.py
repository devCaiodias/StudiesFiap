class Retaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Retaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Retaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))