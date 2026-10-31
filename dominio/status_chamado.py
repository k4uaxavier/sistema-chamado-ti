#usaremos Enum que Em vez de escrever o status como qualquer texto, utilizaremos opções previamente definidas

from enum import Enum

#Classe que representa os status de um chamado

class StatusChamado(Enum):
    ABERTO = "Aberto"
    EM_ATENDIMENTO = "Em atendimento"
    ENCERRADO = "Encerrado"
