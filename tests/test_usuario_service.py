
import unittest

from aplicacao.usuario_service import UsuarioService
from infraestrutura.repositorio_usuarios import RepositorioUsuarios

# A classe TestUsuarioService é uma subclasse de unittest.TestCase, que fornece métodos para criar e executar testes unitários para a classe UsuarioService.
class TestUsuarioService(unittest.TestCase):
# O método setUp é chamado antes de cada teste e é usado para configurar o ambiente de teste, criando instâncias do repositório de usuários e do serviço UsuarioService.
    def setUp(self):
        self.repositorio = RepositorioUsuarios()
        self.service = UsuarioService(self.repositorio)
# O método test_cadastrar_usuario é um teste unitário que verifica se o cadastro de um usuário funciona corretamente, validando se o usuário foi criado com sucesso e possui os atributos esperados.
    def test_cadastrar_usuario(self):
        usuario = self.service.cadastrar_usuario(
            "João",
            "joao@email.com"
        )

        self.assertEqual(usuario.id, 1)
        self.assertEqual(usuario.nome, "João")

    def test_buscar_usuario(self):
        usuario = self.service.cadastrar_usuario(
            "Maria",
            "maria@email.com"
        )

        resultado = self.service.buscar_usuario(usuario.id)

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nome, "Maria")

    def test_listar_usuarios(self):
        self.service.cadastrar_usuario("João", "joao@email.com")
        self.service.cadastrar_usuario("Maria", "maria@email.com")

        resultado = self.service.listar_usuarios()

        self.assertEqual(len(resultado), 2)


if __name__ == "__main__":
    unittest.main()
