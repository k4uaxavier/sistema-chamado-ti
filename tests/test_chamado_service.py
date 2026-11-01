# Chamado Service
import unittest
#o módulo unittest é importado para permitir a criação e execução de testes unitários.
from aplicacao.chamado_service import ChamadoService
from dominio.usuario import Usuario
from dominio.status_chamado import StatusChamado
from dominio.excecoes import (
    OperacaoInvalidaError,
    ChamadoInvalidoError
)
from infraestrutura.repositorio_chamados import RepositorioChamados
from infraestrutura.repositorio_usuarios import RepositorioUsuarios

#classe TestChamadoService é uma subclasse de unittest.TestCase, que fornece métodos para criar e executar testes unitários para a classe ChamadoService.
class TestChamadoService(unittest.TestCase):
#o método setUp é chamado antes de cada teste e é usado para configurar o ambiente de teste, criando instâncias dos repositórios e do serviço ChamadoService, além de criar um usuário de teste.
    def setUp(self):
        self.repositorio_chamados = RepositorioChamados()
        self.repositorio_usuarios = RepositorioUsuarios()

        self.usuario = Usuario(None, "João", "joao@email.com")
        self.repositorio_usuarios.salvar(self.usuario)

        self.service = ChamadoService(
            self.repositorio_chamados,
            self.repositorio_usuarios
        )
#o método test_abrir_chamado_com_sucesso é um teste unitário que verifica se a abertura de um chamado com um usuário existente e uma descrição válida funciona corretamente, validando se o chamado foi criado com sucesso e possui os atributos esperados.
    def test_abrir_chamado_com_sucesso(self):
        chamado = self.service.abrir_chamado(
            self.usuario.id,
            "Computador não liga"
        )

        self.assertIsNotNone(chamado.id)
        self.assertEqual(chamado.descricao, "Computador não liga")
        self.assertEqual(chamado.status, StatusChamado.ABERTO)

    def test_abrir_chamado_com_usuario_inexistente(self):
        with self.assertRaises(OperacaoInvalidaError):
            self.service.abrir_chamado(
                999,
                "Computador não liga"
            )

    def test_abrir_chamado_com_descricao_vazia(self):
        with self.assertRaises(ChamadoInvalidoError):
            self.service.abrir_chamado(
                self.usuario.id,
                "   "
            )

#logica de negócios para abrir um chamado, incluindo a validação do usuário e a criação do objeto Chamado.
if __name__ == "__main__":
    unittest.main()
