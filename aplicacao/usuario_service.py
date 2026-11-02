#aplicacao/usuario_service.py
from dominio.usuario import Usuario

# A classe UsuarioService é responsável por gerenciar as operações relacionadas aos usuários, como cadastro, busca e listagem de usuários.

class UsuarioService:
# O método __init__ é o construtor da classe, que recebe um repositório de usuários como parâmetro e o armazena como um atributo da instância.
    def __init__(self, repositorio_usuarios):
        self.repositorio_usuarios = repositorio_usuarios
# O método cadastrar_usuario cria um novo usuário com o nome e email fornecidos, utilizando a classe Usuario, e salva o usuário no repositório de usuários.
    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(None, nome, email)

        return self.repositorio_usuarios.salvar(usuario)
# O método buscar_usuario busca um usuário pelo seu ID, utilizando o repositório de usuários.
    def buscar_usuario(self, usuario_id):
        return self.repositorio_usuarios.buscar_por_id(usuario_id)
# O método listar_usuarios retorna uma lista de todos os usuários cadastrados, utilizando o repositório de usuários.
    def listar_usuarios(self):
        return self.repositorio_usuarios.listar_todos()
