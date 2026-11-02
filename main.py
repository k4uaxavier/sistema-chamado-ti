
from aplicacao.usuario_service import UsuarioService
from aplicacao.chamado_service import ChamadoService

from infraestrutura.repositorio_usuarios import RepositorioUsuarios
from infraestrutura.repositorio_chamados import RepositorioChamados

from interface.terminal_cli import TerminalCLI


def main():

    repositorio_usuarios = RepositorioUsuarios()
    repositorio_chamados = RepositorioChamados()

    usuario_service = UsuarioService(repositorio_usuarios)

    chamado_service = ChamadoService(
        repositorio_chamados,
        repositorio_usuarios
    )

    terminal = TerminalCLI(
        usuario_service,
        chamado_service
    )

    terminal.executar()


if __name__ == "__main__":
    main()
