from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_lefrance = Restaurante('LeFrance', 'Francês')
restaurante_ragazzo = Restaurante('ragazzo', 'Italiano')
restaurante_ragazzo.receber_avaliacao('Gui', 10)
restaurante_ragazzo.receber_avaliacao('Ni', 8)

restaurante_lefrance.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()