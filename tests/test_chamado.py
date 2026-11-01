
import unittest

from dominio.usuario import Usuario
from dominio.chamado import Chamado
from dominio.status_chamado import StatusChamado
from dominio.excecoes import ChamadoInvalidoError

#a classe TestChamado é uma subclasse de unittest.TestCase, que fornece métodos para criar e executar testes unitários.
class TestChamado(unittest.TestCase):
#o método test_chamado_inicia_com_status_aberto é um teste unitário que verifica se um chamado recém-criado possui o status inicial definido como "ABERTO".
    def test_chamado_inicia_com_status_aberto(self):
        usuario = Usuario(1, "João", "joao@email.com")

        chamado = Chamado("Computador não liga", usuario)

        self.assertEqual(chamado.status, StatusChamado.ABERTO)
#o método test_descricao_vazia_deve_gerar_erro é um teste unitário que verifica se a criação de um chamado com uma descrição vazia gera a exceção ChamadoInvalidoError.
    def test_descricao_vazia_deve_gerar_erro(self):
        usuario = Usuario(1, "João", "joao@email.com")

        chamado = Chamado("   ", usuario)

        with self.assertRaises(ChamadoInvalidoError):
            chamado.validar()


if __name__ == "__main__":
    unittest.main()
