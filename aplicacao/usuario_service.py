
from dominio.usuario import Usuario
from dominio.tecnico import Tecnico


class UsuarioService:

    def __init__(self, repositorio_usuarios):
        self.repositorio_usuarios = repositorio_usuarios

    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(None, nome, email)

        return self.repositorio_usuarios.salvar(usuario)

    def cadastrar_tecnico(self, nome, email, especialidade):
        tecnico = Tecnico(None, nome, email, especialidade)

        return self.repositorio_usuarios.salvar(tecnico)

    def buscar_usuario(self, usuario_id):
        return self.repositorio_usuarios.buscar_por_id(usuario_id)

    def listar_usuarios(self):
        usuarios = self.repositorio_usuarios.listar_todos()

        return [
            usuario for usuario in usuarios
            if type(usuario) is Usuario
        ]

    def listar_tecnicos(self):
        usuarios = self.repositorio_usuarios.listar_todos()

        return [
            usuario for usuario in usuarios
            if isinstance(usuario, Tecnico)
        ]
