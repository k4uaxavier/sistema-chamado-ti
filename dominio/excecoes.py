#responsável por armazenar os erros específicos do nosso sistema

class ChamadoInvalidoError(Exception):
    pass


class OperacaoInvalidaError(Exception):
    pass