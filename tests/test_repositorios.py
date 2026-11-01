
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

#verifica se o repositório de chamados está funcionando corretamente, permitindo salvar e buscar chamados com sucesso.
from infraestrutura.repositorio_usuarios import RepositorioUsuarios

#classe TestRepositorioUsuarios é uma subclasse de unittest.TestCase, que fornece métodos para criar e executar testes unitários.
class TestRepositorioUsuarios(unittest.TestCase):
#o método test_salvar_usuario é um teste unitário que verifica se um usuário pode ser salvo corretamente no repositório.
    def test_salvar_usuario(self):
        repositorio = RepositorioUsuarios()

        usuario = Usuario(None, "Maria", "maria@email.com")

        repositorio.salvar(usuario)

        self.assertEqual(usuario.id, 1)
#o método test_buscar_usuario_por_id é um teste unitário que verifica se um usuário pode ser buscado corretamente pelo seu ID no repositório.
    def test_buscar_usuario_por_id(self):
        repositorio = RepositorioUsuarios()

        usuario = Usuario(None, "João", "joao@email.com")

        repositorio.salvar(usuario)

        resultado = repositorio.buscar_por_id(1)
#o método test_buscar_usuario_por_id realiza as seguintes verificações:
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nome, "João")
#o método test_listar_usuarios é um teste unitário que verifica se todos os usuários podem ser listados corretamente no repositório.
    def test_listar_usuarios(self):
        repositorio = RepositorioUsuarios()
#o método test_listar_usuarios realiza as seguintes verificações:
        usuario1 = Usuario(None, "João", "joao@email.com")
        usuario2 = Usuario(None, "Maria", "maria@email.com")

        repositorio.salvar(usuario1)
        repositorio.salvar(usuario2)

        resultado = repositorio.listar_todos()

        self.assertEqual(len(resultado), 2)
