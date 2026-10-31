#Classe que representa um usuário do sistema
class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def listar_chamados(self):
        return []
