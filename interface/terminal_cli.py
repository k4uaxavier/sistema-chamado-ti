
from dominio.status_chamado import StatusChamado


class TerminalCLI:

    def __init__(self, usuario_service, chamado_service):
        self.usuario_service = usuario_service
        self.chamado_service = chamado_service

    def exibir_menu(self):
        print("\n====================================")
        print("       SISTEMA DE CHAMADOS DE TI")
        print("====================================")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Cadastrar técnico")
        print("4 - Listar técnicos")
        print("5 - Abrir chamado")
        print("6 - Listar chamados")
        print("7 - Atribuir técnico ao chamado")
        print("8 - Iniciar atendimento")
        print("9 - Encerrar chamado")
        print("0 - Sair")
        print("====================================")

    def aguardar(self):
        input("\nPressione Enter para voltar ao menu...")

    def executar(self):

        while True:
            self.exibir_menu()

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_usuario()
                self.aguardar()

            elif opcao == "2":
                self.listar_usuarios()
                self.aguardar()

            elif opcao == "3":
                self.cadastrar_tecnico()
                self.aguardar()

            elif opcao == "4":
                self.listar_tecnicos()
                self.aguardar()

            elif opcao == "5":
                self.abrir_chamado()
                self.aguardar()

            elif opcao == "6":
                self.listar_chamados()
                self.aguardar()

            elif opcao == "7":
                self.atribuir_tecnico()
                self.aguardar()

            elif opcao == "8":
                self.iniciar_atendimento()
                self.aguardar()

            elif opcao == "9":
                self.encerrar_chamado()
                self.aguardar()

            elif opcao == "0":
                print("\nSistema encerrado. Até mais!")
                break

            else:
                print("\nOpção inválida. Tente novamente.")
                self.aguardar()

    def cadastrar_usuario(self):
        print("\n--- CADASTRO DE USUÁRIO ---")

        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")

        try:
            usuario = self.usuario_service.cadastrar_usuario(
                nome,
                email
            )

            print("\nUsuário cadastrado com sucesso!")
            print(f"ID: {usuario.id}")
            print(f"Nome: {usuario.nome}")
            print(f"E-mail: {usuario.email}")

        except Exception as erro:
            print(f"\nErro ao cadastrar usuário: {erro}")

    def listar_usuarios(self):
        print("\n--- USUÁRIOS CADASTRADOS ---")

        usuarios = self.usuario_service.listar_usuarios()

        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in usuarios:
            print("------------------------------------")
            print(f"ID: {usuario.id}")
            print(f"Nome: {usuario.nome}")
            print(f"E-mail: {usuario.email}")

    def cadastrar_tecnico(self):
        print("\n--- CADASTRO DE TÉCNICO ---")

        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        especialidade = input("Digite a especialidade: ")

        try:
            tecnico = self.usuario_service.cadastrar_tecnico(
                nome,
                email,
                especialidade
            )

            print("\nTécnico cadastrado com sucesso!")
            print(f"ID: {tecnico.id}")
            print(f"Nome: {tecnico.nome}")
            print(f"E-mail: {tecnico.email}")
            print(f"Especialidade: {tecnico.especialidade}")

        except Exception as erro:
            print(f"\nErro ao cadastrar técnico: {erro}")

    def listar_tecnicos(self):
        print("\n--- TÉCNICOS CADASTRADOS ---")

        tecnicos = self.usuario_service.listar_tecnicos()

        if not tecnicos:
            print("Nenhum técnico cadastrado.")
            return

        for tecnico in tecnicos:
            print("------------------------------------")
            print(f"ID: {tecnico.id}")
            print(f"Nome: {tecnico.nome}")
            print(f"E-mail: {tecnico.email}")
            print(f"Especialidade: {tecnico.especialidade}")

    def abrir_chamado(self):
        print("\n--- ABERTURA DE CHAMADO ---")

        try:
            usuario_id = int(
                input("Digite o ID do usuário solicitante: ")
            )

            descricao = input("Descreva o problema: ")

            chamado = self.chamado_service.abrir_chamado(
                usuario_id,
                descricao
            )

            print("\nChamado aberto com sucesso!")
            print(f"Número do chamado: {chamado.id}")
            print(f"Descrição: {chamado.descricao}")
            print(f"Solicitante: {chamado.solicitante.nome}")
            print(f"Status: {chamado.status.value}")

        except ValueError:
            print("\nErro: o ID deve ser um número inteiro.")

        except Exception as erro:
            print(f"\nNão foi possível abrir o chamado: {erro}")

    def listar_chamados(self):
        print("\n--- CHAMADOS CADASTRADOS ---")

        chamados = self.chamado_service.listar_chamados()

        if not chamados:
            print("Nenhum chamado cadastrado.")
            return

        for chamado in chamados:
            print("------------------------------------")
            print(f"ID: {chamado.id}")
            print(f"Descrição: {chamado.descricao}")
            print(f"Solicitante: {chamado.solicitante.nome}")
            print(f"Status: {chamado.status.value}")

            if chamado.tecnico is not None:
                print(f"Técnico: {chamado.tecnico.nome}")
            else:
                print("Técnico: Não atribuído")

            if chamado.solucao is not None:
                print(f"Solução: {chamado.solucao}")

    def atribuir_tecnico(self):
        print("\n--- ATRIBUIÇÃO DE TÉCNICO ---")

        try:
            chamado_id = int(input("Digite o ID do chamado: "))
            tecnico_id = int(input("Digite o ID do técnico: "))

            chamado = self.chamado_service.repositorio_chamados.buscar_por_id(
                chamado_id
            )

            tecnico = self.usuario_service.buscar_usuario(tecnico_id)

            if chamado is None:
                print("\nChamado não encontrado.")
                return

            if tecnico is None:
                print("\nTécnico não encontrado.")
                return

            self.chamado_service.atribuir_tecnico(
                chamado,
                tecnico
            )

            print("\nTécnico atribuído com sucesso!")
            print(f"Chamado: {chamado.id}")
            print(f"Técnico responsável: {tecnico.nome}")

        except ValueError:
            print("\nErro: os IDs devem ser números inteiros.")

        except Exception as erro:
            print(f"\nNão foi possível atribuir o técnico: {erro}")

    def iniciar_atendimento(self):
        print("\n--- INICIAR ATENDIMENTO ---")

        try:
            chamado_id = int(input("Digite o ID do chamado: "))

            chamado = self.chamado_service.repositorio_chamados.buscar_por_id(
                chamado_id
            )

            if chamado is None:
                print("\nChamado não encontrado.")
                return

            self.chamado_service.atualizar_status(
                chamado,
                StatusChamado.EM_ATENDIMENTO
            )

            print("\nAtendimento iniciado com sucesso!")
            print(f"Chamado: {chamado.id}")
            print(f"Status: {chamado.status.value}")

        except ValueError:
            print("\nErro: o ID deve ser um número inteiro.")

        except Exception as erro:
            print(f"\nNão foi possível iniciar o atendimento: {erro}")

    def encerrar_chamado(self):
        print("\n--- ENCERRAR CHAMADO ---")

        try:
            chamado_id = int(input("Digite o ID do chamado: "))
            solucao = input("Descreva a solução do problema: ")

            chamado = self.chamado_service.repositorio_chamados.buscar_por_id(
                chamado_id
            )

            if chamado is None:
                print("\nChamado não encontrado.")
                return

            self.chamado_service.encerrar_chamado(
                chamado,
                solucao
            )

            print("\nChamado encerrado com sucesso!")
            print(f"Chamado: {chamado.id}")
            print(f"Solução: {chamado.solucao}")
            print(f"Status: {chamado.status.value}")

        except ValueError:
            print("\nErro: o ID deve ser um número inteiro.")

        except Exception as erro:
            print(f"\nNão foi possível encerrar o chamado: {erro}")
