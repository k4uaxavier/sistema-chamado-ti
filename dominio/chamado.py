
from datetime import datetime

from dominio.status_chamado import StatusChamado
from dominio.excecoes import ChamadoInvalidoError

#Classe mais importante do sistema, pois representa um chamado aberto por um usuário solicitante.
class Chamado:
    def __init__(self, descricao, solicitante):
        self.id = None
        self.descricao = descricao
        self.status = StatusChamado.ABERTO
        self.data_abertura = datetime.now()
        self.solucao = None
        self.solicitante = solicitante

    def validar(self):
        if not self.descricao or not self.descricao.strip():
            raise ChamadoInvalidoError(
                "A descrição do chamado é obrigatória."
            )

        if self.solicitante is None:
            raise ChamadoInvalidoError(
                "O chamado precisa ter um usuário solicitante."
            )
