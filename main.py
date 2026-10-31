# primeiro teste: criação de chamado 
"""
from dominio.usuario import Usuario
from dominio.chamado import Chamado

usuario = Usuario(1, "João", "joao@email.com")

chamado = Chamado(
    "Computador não está ligando",
    usuario
)

chamado.validar()

print("Chamado criado com sucesso!")
print("Solicitante:", chamado.solicitante.nome)
print("Descrição:", chamado.descricao)
print("Status:", chamado.status.value)
"""
# segundo teste: repositório de chamados
from dominio.usuario import Usuario
from dominio.chamado import Chamado
from infraestrutura.repositorio_chamados import RepositorioChamados

usuario = Usuario(1, "João", "joao@email.com")

chamado = Chamado("Computador não liga", usuario)

repositorio = RepositorioChamados()

repositorio.salvar(chamado)

print("ID:", chamado.id)
print("Chamado:", repositorio.buscar_por_id(1).descricao)

print("Todos os chamados:")
for item in repositorio.listar_todos():
    print(item.id, item.descricao)

