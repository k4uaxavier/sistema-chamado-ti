
from dominio.chamado import Chamado
from dominio.excecoes import OperacaoInvalidaError


class ChamadoService:

    def __init__(self, repositorio_chamados, repositorio_usuarios):
        self.repositorio_chamados = repositorio_chamados
        self.repositorio_usuarios = repositorio_usuarios

    def abrir_chamado(self, usuario_id, descricao):

        usuario = self.repositorio_usuarios.buscar_por_id(usuario_id)

        if usuario is None:
            raise OperacaoInvalidaError(
                "Usuário não encontrado."
            )

        chamado = Chamado(descricao, usuario)

        chamado.validar()

        return self.repositorio_chamados.salvar(chamado)

    def atribuir_tecnico(self, chamado, tecnico):
        chamado.atribuir_tecnico(tecnico)

    def listar_chamados(self):
        return self.repositorio_chamados.listar_todos()

    def atualizar_status(self, chamado, novo_status):
        chamado.atualizar_status(novo_status)

    def encerrar_chamado(self, chamado, solucao):
        chamado.encerrar(solucao)
