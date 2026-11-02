
import unittest

from dominio.usuario import Usuario
from dominio.tecnico import Tecnico


class TestTecnico(unittest.TestCase):

    def test_tecnico_herda_usuario(self):
        tecnico = Tecnico(
            1,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )

        self.assertIsInstance(tecnico, Usuario)

    def test_tecnico_possui_dados_de_usuario(self):
        tecnico = Tecnico(
            1,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )

        self.assertEqual(tecnico.id, 1)
        self.assertEqual(tecnico.nome, "Carlos")
        self.assertEqual(tecnico.email, "carlos@email.com")

    def test_tecnico_possui_especialidade(self):
        tecnico = Tecnico(
            1,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )

        self.assertEqual(
            tecnico.especialidade,
            "Suporte de Hardware"
        )


if __name__ == "__main__":
    unittest.main()
