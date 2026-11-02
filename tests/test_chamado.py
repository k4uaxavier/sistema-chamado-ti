
import unittest

from dominio.usuario import Usuario
from dominio.chamado import Chamado
from dominio.tecnico import Tecnico
from dominio.status_chamado import StatusChamado
from dominio.excecoes import (
    ChamadoInvalidoError,
    OperacaoInvalidaError
)


class TestChamado(unittest.TestCase):

    # Verifica se o chamado começa com status ABERTO.
    def test_chamado_inicia_com_status_aberto(self):
        usuario = Usuario(1, "João", "joao@email.com")
        chamado = Chamado("Computador não liga", usuario)

        self.assertEqual(chamado.status, StatusChamado.ABERTO)

    # Verifica se uma descrição vazia gera uma exceção.
    def test_descricao_vazia_deve_gerar_erro(self):
        usuario = Usuario(1, "João", "joao@email.com")
        chamado = Chamado("   ", usuario)

        with self.assertRaises(ChamadoInvalidoError):
            chamado.validar()

    # Verifica se o chamado começa sem técnico atribuído.
    def test_chamado_inicia_sem_tecnico(self):
        usuario = Usuario(1, "João", "joao@email.com")
        chamado = Chamado("Computador não liga", usuario)

        self.assertIsNone(chamado.tecnico)

    # Verifica se é possível atribuir um técnico ao chamado.
    def test_atribuir_tecnico_ao_chamado(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)

        chamado.atribuir_tecnico(tecnico)

        self.assertEqual(chamado.tecnico, tecnico)

    # Verifica se um usuário comum não pode ser atribuído como técnico.
    def test_nao_permitir_atribuir_usuario_comum(self):
        usuario = Usuario(1, "João", "joao@email.com")
        outro_usuario = Usuario(2, "Maria", "maria@email.com")
        chamado = Chamado("Computador não liga", usuario)

        with self.assertRaises(OperacaoInvalidaError):
            chamado.atribuir_tecnico(outro_usuario)

    # Verifica se um chamado encerrado não recebe outro técnico.
    def test_nao_permitir_atribuir_tecnico_a_chamado_encerrado(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)
        chamado.status = StatusChamado.ENCERRADO

        with self.assertRaises(OperacaoInvalidaError):
            chamado.atribuir_tecnico(tecnico)

    # Verifica se é possível encerrar um chamado com solução.
    def test_encerrar_chamado_com_sucesso(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)

        chamado.atribuir_tecnico(tecnico)
        chamado.atualizar_status(StatusChamado.EM_ATENDIMENTO)
        chamado.encerrar("Fonte do computador substituída.")

        self.assertEqual(chamado.status, StatusChamado.ENCERRADO)
        self.assertEqual(
            chamado.solucao,
            "Fonte do computador substituída."
        )

    # Verifica se não é possível encerrar sem solução.
    def test_nao_encerrar_chamado_sem_solucao(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)

        chamado.atribuir_tecnico(tecnico)
        chamado.atualizar_status(StatusChamado.EM_ATENDIMENTO)

        with self.assertRaises(ChamadoInvalidoError):
            chamado.encerrar("   ")

    # Verifica se não é possível encerrar um chamado ainda aberto.
    def test_nao_encerrar_chamado_aberto(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)

        chamado.atribuir_tecnico(tecnico)

        with self.assertRaises(OperacaoInvalidaError):
            chamado.encerrar("Problema resolvido.")

    # Verifica se não é possível encerrar um chamado duas vezes.
    def test_nao_encerrar_chamado_ja_encerrado(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)

        chamado.atribuir_tecnico(tecnico)
        chamado.atualizar_status(StatusChamado.EM_ATENDIMENTO)
        chamado.encerrar("Fonte substituída.")

        with self.assertRaises(OperacaoInvalidaError):
            chamado.encerrar("Outra solução.")

    # Verifica se a solução não pode ser vazia.
    def test_nao_permitir_solucao_vazia(self):
        usuario = Usuario(1, "João", "joao@email.com")
        tecnico = Tecnico(
            2,
            "Carlos",
            "carlos@email.com",
            "Suporte de Hardware"
        )
        chamado = Chamado("Computador não liga", usuario)

        chamado.atribuir_tecnico(tecnico)
        chamado.atualizar_status(StatusChamado.EM_ATENDIMENTO)

        with self.assertRaises(ChamadoInvalidoError):
            chamado.encerrar("")


if __name__ == "__main__":
    unittest.main()
