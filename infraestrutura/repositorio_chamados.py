#classe que representa o repositório de chamados, responsável por armazenar e gerenciar os objetos de chamado.
class RepositorioChamados:
    # __init__ É executado quando criamos um objeto da classe
    def __init__(self):
    # Dicionário para armazenar os chamados, onde a chave é o ID do chamado e o valor é o objeto chamado
        self.chamados = {} 
    # Variável para controlar o próximo ID a ser atribuído a um chamado
        self.proximo_id = 1
#cada método da classe RepositorioChamados, que é responsável por salvar um chamado no repositório.
    def salvar(self, chamado):
        if chamado.id is None:
            chamado.id = self.proximo_id
            self.proximo_id += 1

        self.chamados[chamado.id] = chamado
        return chamado
#busca um chamado pelo seu ID no repositório. Se o chamado existir, ele é retornado; caso contrário, None é retornado.
    def buscar_por_id(self, id):
        return self.chamados.get(id)
#lista todos os chamados presentes no repositório. Ele retorna uma lista contendo todos os objetos de chamado armazenados.
    def listar_todos(self):
        return list(self.chamados.values())
