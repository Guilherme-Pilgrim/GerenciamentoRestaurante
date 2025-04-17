from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_ragazzo = Restaurante('ragazzo', 'Italiano')
restaurante_ragazzo.receber_avaliacao('Gui', 10)

bebida_suco = Bebida('Suco de Maracujá', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão francês', 2.00, 'O melhor pão do mundo')
prato_pao.aplicar_desconto()
restaurante_ragazzo.adicionar_no_cardapo(bebida_suco)
restaurante_ragazzo.adicionar_no_cardapo(prato_pao)

def main():
    restaurante_ragazzo.exibir_cardapio

if __name__ == '__main__':
    main()