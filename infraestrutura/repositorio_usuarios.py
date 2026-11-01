#classe que representa o repositório de usuários, responsável por armazenar e gerenciar os objetos de usuário.
class RepositorioUsuarios:
    def __init__(self):
        # Dicionário para armazenar os usuários, onde a chave é o ID do usuário e o valor é o objeto usuário
        self.usuarios = {}
         # Variável para controlar o próximo ID a ser atribuído a um usuário
        self.proximo_id = 1

#cada método da classe RepositorioUsuarios, que é responsável por salvar um usuário no repositório.
    def salvar(self, usuario):
        if usuario.id is None:
            usuario.id = self.proximo_id
            self.proximo_id += 1

        self.usuarios[usuario.id] = usuario
        return usuario
#busca um usuário pelo seu ID no repositório. Se o usuário existir, ele é retornado; caso contrário, None é retornado.
    def buscar_por_id(self, id):
        return self.usuarios.get(id)
#lista todos os usuários presentes no repositório. Ele retorna uma lista contendo todos os objetos de usuário armazenados.
    def listar_todos(self):
        return list(self.usuarios.values())
