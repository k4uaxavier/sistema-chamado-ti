
import unittest

from aplicacao.usuario_service import UsuarioService
from infraestrutura.repositorio_usuarios import RepositorioUsuarios
from dominio.tecnico import Tecnico


class TestUsuarioService(unittest.TestCase):

    def setUp(self):
        self.repositorio = RepositorioUsuarios()
        self.service = UsuarioService(self.repositorio)

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

    def test_cadastrar_tecnico(self):
        tecnico = self.service.cadastrar_tecnico(
            "Carlos",
            "carlos@email.com",
            "Redes"
        )

        self.assertIsInstance(tecnico, Tecnico)
        self.assertEqual(tecnico.id, 1)
        self.assertEqual(tecnico.nome, "Carlos")
        self.assertEqual(tecnico.especialidade, "Redes")

    def test_listar_tecnicos(self):
        self.service.cadastrar_tecnico(
            "Carlos",
            "carlos@email.com",
            "Redes"
        )

        self.service.cadastrar_tecnico(
            "Ana",
            "ana@email.com",
            "Hardware"
        )

        resultado = self.service.listar_tecnicos()

        self.assertEqual(len(resultado), 2)

    def test_listar_usuarios_nao_inclui_tecnicos(self):
        self.service.cadastrar_usuario(
            "João",
            "joao@email.com"
        )

        self.service.cadastrar_tecnico(
            "Carlos",
            "carlos@email.com",
            "Redes"
        )

        resultado = self.service.listar_usuarios()

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].nome, "João")


if __name__ == "__main__":
    unittest.main()
