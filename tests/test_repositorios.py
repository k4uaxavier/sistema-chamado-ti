
import unittest

from dominio.usuario import Usuario
from dominio.chamado import Chamado
from infraestrutura.repositorio_chamados import RepositorioChamados

#a classe TestRepositorioChamados é uma subclasse de unittest.TestCase, que fornece métodos para criar e executar testes unitários.
class TestRepositorioChamados(unittest.TestCase):
#o método test_salvar_e_buscar_chamado é um teste unitário que verifica se um chamado pode ser salvo e buscado corretamente no repositório.
    def test_salvar_e_buscar_chamado(self):
        usuario = Usuario(1, "João", "joao@email.com")

        chamado = Chamado("Computador não liga", usuario)

        repositorio = RepositorioChamados()

        repositorio.salvar(chamado)

        resultado = repositorio.buscar_por_id(1)
#o método test_salvar_e_buscar_chamado realiza as seguintes verificações:
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.descricao, "Computador não liga")
        self.assertEqual(resultado.solicitante.nome, "João")


if __name__ == "__main__":
    unittest.main()
