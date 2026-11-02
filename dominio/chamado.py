
from datetime import datetime

from dominio.status_chamado import StatusChamado
from dominio.excecoes import (
    ChamadoInvalidoError,
    OperacaoInvalidaError
)
from dominio.tecnico import Tecnico


class Chamado:

    def __init__(self, descricao, solicitante):
        self.id = None
        self.descricao = descricao
        self.status = StatusChamado.ABERTO
        self.data_abertura = datetime.now()
        self.solucao = None
        self.solicitante = solicitante
        self.tecnico = None

    def validar(self):
        if not self.descricao or not self.descricao.strip():
            raise ChamadoInvalidoError(
                "A descrição do chamado é obrigatória."
            )

        if self.solicitante is None:
            raise ChamadoInvalidoError(
                "O chamado precisa ter um usuário solicitante."
            )

    def atribuir_tecnico(self, tecnico):
        if not isinstance(tecnico, Tecnico):
            raise OperacaoInvalidaError(
                "O responsável pelo chamado deve ser um técnico."
            )

        if self.status == StatusChamado.ENCERRADO:
            raise OperacaoInvalidaError(
                "Não é possível atribuir técnico a um chamado encerrado."
            )

        self.tecnico = tecnico

    def atualizar_status(self, novo_status):

        if self.status == StatusChamado.ENCERRADO:
            raise OperacaoInvalidaError(
                "Um chamado encerrado não pode ter seu status alterado."
            )

        if self.status == StatusChamado.ABERTO:
            if novo_status != StatusChamado.EM_ATENDIMENTO:
                raise OperacaoInvalidaError(
                    "Um chamado aberto só pode passar para Em atendimento."
                )

            if self.tecnico is None:
                raise OperacaoInvalidaError(
                    "É necessário atribuir um técnico antes de iniciar o atendimento."
                )

            self.status = novo_status
            return

        raise OperacaoInvalidaError(
            "Transição de status não permitida."
        )

    def encerrar(self, solucao):

        if self.status == StatusChamado.ENCERRADO:
            raise OperacaoInvalidaError(
                "Este chamado já está encerrado."
            )

        if self.status != StatusChamado.EM_ATENDIMENTO:
            raise OperacaoInvalidaError(
                "Só é possível encerrar um chamado em atendimento."
            )

        if self.tecnico is None:
            raise OperacaoInvalidaError(
                "É necessário ter um técnico atribuído para encerrar o chamado."
            )

        if not solucao or not solucao.strip():
            raise ChamadoInvalidoError(
                "A solução do chamado é obrigatória."
            )

        self.solucao = solucao
        self.status = StatusChamado.ENCERRADO
