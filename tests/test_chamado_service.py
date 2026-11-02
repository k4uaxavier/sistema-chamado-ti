
# Testes do ChamadoService

import unittest

from aplicacao.chamado_service import ChamadoService

from dominio.usuario import Usuario
from dominio.tecnico import Tecnico
from dominio.status_chamado import StatusChamado

from dominio.excecoes import (
    OperacaoInvalidaError,
    ChamadoInvalidoError
)

from infraestrutura.repositorio_chamados import RepositorioChamados
from infraestrutura.repositorio_usuarios import RepositorioUsuarios


class TestChamadoService(unittest.TestCase):

    # Configura os objetos necessários antes de cada teste.
    def setUp(self):
        self.repositorio_chamados = RepositorioChamados()
        self.repositorio_usuarios = RepositorioUsuarios()

        self.usuario = Usuario(None, "João", "joao@email.com")
        self.repositorio_usuarios.salvar(self.usuario)

        self.service = ChamadoService(
            self.repositorio_chamados,
            self.repositorio_usuarios
        )

    # Verifica se um chamado pode ser aberto com sucesso.
    def test_abrir_chamado_com_sucesso(self):
        chamado = self.service.abrir_chamado(
            self.usuario.id,
            "Computador não liga"
        )

        self.assertIsNotNone(chamado.id)
        self.assertEqual(chamado.descricao, "Computador não liga")
        self.assertEqual(chamado.status, StatusChamado.ABERTO)

    # Verifica se a abertura falha quando o usuário não existe.
    def test_abrir_chamado_com_usuario_inexistente(self):
        with self.assertRaises(OperacaoInvalidaError):
            self.service.abrir_chamado(
                999,
                "Computador não liga"
            )

    # Verifica se uma descrição vazia gera uma exceção.
    def test_abrir_chamado_com_descricao_vazia(self):
        with self.assertRaises(ChamadoInvalidoError):
            self.service.abrir_chamado(
                self.usuario.id,
                "   "
            )

    # Verifica se o serviço consegue atribuir um técnico ao chamado.
    def test_atribuir_tecnico_ao_chamado(self):
        chamado = self.service.abrir_chamado(
            self.usuario.id,
            "Computador não liga"
        )

        tecnico = Tecnico(
            None,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )

        self.service.atribuir_tecnico(chamado, tecnico)

        self.assertEqual(chamado.tecnico, tecnico)

    # Verifica se o serviço consegue atualizar o status do chamado.
    def test_atualizar_status_para_em_atendimento(self):
        chamado = self.service.abrir_chamado(
            self.usuario.id,
            "Computador não liga"
        )

        tecnico = Tecnico(
            None,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )

        self.service.atribuir_tecnico(chamado, tecnico)

        self.service.atualizar_status(
            chamado,
            StatusChamado.EM_ATENDIMENTO
        )

        self.assertEqual(
            chamado.status,
            StatusChamado.EM_ATENDIMENTO
        )

    # Verifica se o serviço consegue encerrar um chamado com solução.
    def test_encerrar_chamado_com_sucesso(self):
        chamado = self.service.abrir_chamado(
            self.usuario.id,
            "Computador não liga"
        )

        tecnico = Tecnico(
            None,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )

        self.service.atribuir_tecnico(chamado, tecnico)

        self.service.atualizar_status(
            chamado,
            StatusChamado.EM_ATENDIMENTO
        )

        self.service.encerrar_chamado(
            chamado,
            "Fonte do computador substituída."
        )

        self.assertEqual(
            chamado.status,
            StatusChamado.ENCERRADO
        )

        self.assertEqual(
            chamado.solucao,
            "Fonte do computador substituída."
        )


if __name__ == "__main__":
    unittest.main()
