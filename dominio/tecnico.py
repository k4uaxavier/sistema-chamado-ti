
from dominio.usuario import Usuario

# A classe Tecnico é uma subclasse da classe Usuario, representando um técnico com uma especialidade específica.
class Tecnico(Usuario):

    def __init__(self, id, nome, email, especialidade):
        super().__init__(id, nome, email)
        self.especialidade = especialidade
