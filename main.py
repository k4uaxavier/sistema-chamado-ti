
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
