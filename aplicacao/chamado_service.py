# Chamado Service
from dominio.chamado import Chamado
from dominio.excecoes import OperacaoInvalidaError

# Chamado Service
class ChamadoService:
#objeto ChamadoService é responsável por gerenciar a lógica de negócios relacionada aos chamados, incluindo a abertura de novos chamados e a validação dos dados fornecidos pelos usuários.
    def __init__(self, repositorio_chamados, repositorio_usuarios):
        self.repositorio_chamados = repositorio_chamados
        self.repositorio_usuarios = repositorio_usuarios
#abrir_chamado é um método que permite abrir um novo chamado, associando-o a um usuário existente. Ele valida se o usuário existe e se os dados do chamado são válidos antes de salvar o chamado no repositório.
    def abrir_chamado(self, usuario_id, descricao):
#abrir_chamado recebe o ID do usuário e a descrição do chamado como parâmetros. Ele busca o usuário no repositório de usuários e, se o usuário não for encontrado, lança uma exceção OperacaoInvalidaError. Em seguida, cria um novo objeto Chamado com a descrição fornecida e o usuário associado, valida os dados do chamado e salva o chamado no repositório de chamados.
        usuario = self.repositorio_usuarios.buscar_por_id(usuario_id)
#logica de negócios para abrir um chamado, incluindo a validação do usuário e a criação do objeto Chamado.
        if usuario is None:
            raise OperacaoInvalidaError(
                "Usuário não encontrado."
            )

        chamado = Chamado(descricao, usuario)

        chamado.validar()

        return self.repositorio_chamados.salvar(chamado)
