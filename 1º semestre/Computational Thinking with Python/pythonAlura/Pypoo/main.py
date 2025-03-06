from modulos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexicano', 'Fast Food')
restaurante_chines = Restaurante('Chines', 'Fast Food')

restaurante_chines.alternar_estado()

restaurante_chines.receber_avaliacao('Lucas', 5)
restaurante_chines.receber_avaliacao('Jonata', 4)


def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()