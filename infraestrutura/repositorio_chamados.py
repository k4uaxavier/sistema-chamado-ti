class RepositorioChamados:
    # __init__ É executado quando criamos um objeto da classe
    def __init__(self):
    # Dicionário para armazenar os chamados, onde a chave é o ID do chamado e o valor é o objeto chamado
        self.chamados = {} 
    # Variável para controlar o próximo ID a ser atribuído a um chamado
        self.proximo_id = 1

    def salvar(self, chamado):
        if chamado.id is None:
            chamado.id = self.proximo_id
            self.proximo_id += 1

        self.chamados[chamado.id] = chamado
        return chamado

    def buscar_por_id(self, id):
        return self.chamados.get(id)

    def listar_todos(self):
        return list(self.chamados.values())
