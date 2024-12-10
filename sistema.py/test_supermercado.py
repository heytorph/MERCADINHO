import unittest
from io import StringIO
from unittest.mock import patch
from sistema import Supermercado

class TestSupermercado(unittest.TestCase):

    def setUp(self):
        self.supermercado = Supermercado()

    def test_adicionar_produto(self):
        # vai estar testandoo a adição de um produto ao carrinho
        with patch('builtins.input', side_effect=['arroz', '2', 'sair']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.supermercado.comprar()

                # verifica se o produto realmente foi adicionado ao carrinho
                self.assertIn('2 unidades de Arroz adicionadas ao carrinho.', mock_stdout.getvalue())

    def test_cancelar_compra(self):
        # Testando o cancelamento da compra
        with patch('builtins.input', side_effect=['cancelar']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.supermercado.pagar()

                # Verifica se a mensagem de compra cancelada é exibida
                self.assertIn('Compra cancelada.', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()