# Sistema de Gerenciamento de Chamados de TI

## 1. Sobre o projeto

O Sistema de Gerenciamento de Chamados de TI é um projeto acadêmico desenvolvido com o objetivo de facilitar a abertura, o acompanhamento e o gerenciamento de solicitações de suporte técnico.

A proposta é centralizar os chamados de TI em um único sistema, permitindo que usuários registrem problemas e que técnicos sejam responsáveis pelo atendimento e pela resolução dessas solicitações.

O projeto utiliza conceitos de Programação Orientada a Objetos (POO), organização em camadas, regras de negócio e testes automatizados.

## 2. Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Programação Orientada a Objetos (POO):** organização do sistema em classes e objetos.
- **Visual Studio Code:** ambiente de desenvolvimento.
- **Git e GitHub:** controle de versão e armazenamento do código.
- **Unittest:** biblioteca utilizada para os testes automatizados.

## 3. Estrutura do projeto

O projeto está organizado da seguinte maneira:

```text
sistema-chamado-ti/
│
├── aplicacao/
│   ├── __init__.py
│   ├── chamado_service.py
│   └── usuario_service.py
│
├── dominio/
│   ├── __init__.py
│   ├── usuario.py
│   ├── tecnico.py
│   ├── chamado.py
│   ├── status_chamado.py
│   └── excecoes.py
│
├── infraestrutura/
│   ├── __init__.py
│   ├── repositorio_chamados.py
│   └── repositorio_usuarios.py
│
├── interface/
│   ├── __init__.py
│   └── terminal_cli.py
│
├── tests/
│   ├── __init__.py
│   ├── test_chamado.py
│   ├── test_repositorios.py
│   ├── test_tecnico.py
│   ├── test_usuario_service.py
│   └── test_chamado_service.py
│
├── main.py
├── README.md
└── .gitignore
```

## 4. Organização do sistema

O sistema está organizado em camadas, separando as responsabilidades de cada parte do projeto.

### Domínio

Contém as classes e regras principais do sistema.

- **Usuario:** representa o usuário que solicita suporte técnico.
- **Tecnico:** representa o profissional responsável pelo atendimento, herdando características da classe Usuario.
- **Chamado:** representa uma solicitação de atendimento técnico.
- **StatusChamado:** define os estados possíveis de um chamado.
- **Excecoes:** contém exceções personalizadas utilizadas pelo sistema.

### Aplicação

Contém os serviços responsáveis por executar as operações do sistema.

**ChamadoService:**
- Abrir novos chamados.
- Verificar a existência do usuário solicitante.
- Validar os dados do chamado.
- Atribuir técnicos aos chamados.
- Listar chamados.
- Atualizar o status dos chamados.
- Encerrar chamados com registro da solução.

**UsuarioService:**
- Cadastrar usuários.
- Buscar usuários pelo ID.
- Listar usuários cadastrados.
- Cadastrar técnicos.
- Listar técnicos cadastrados.

### Infraestrutura

Responsável pelo armazenamento e recuperação dos dados.

**RepositorioChamados:**
- Salvar chamados.
- Buscar chamados pelo ID.
- Listar todos os chamados.

**RepositorioUsuarios:**
- Salvar usuários e técnicos.
- Buscar registros pelo ID.
- Listar os registros armazenados.

Atualmente, os dados são armazenados em memória, utilizando estruturas de dados do Python.

### Interface

Responsável pela interação entre o usuário e o sistema por meio do terminal.

**TerminalCLI:**
- Exibir o menu principal.
- Cadastrar e listar usuários.
- Cadastrar e listar técnicos.
- Abrir e listar chamados.
- Atribuir técnicos aos chamados.
- Iniciar atendimentos.
- Encerrar chamados.

## 5. Funcionalidades implementadas

O sistema possui as seguintes funcionalidades:

- Cadastro de usuários.
- Cadastro de técnicos com especialidade.
- Listagem de usuários e técnicos separadamente.
- Abertura de chamados vinculados a um usuário solicitante.
- Validação da descrição e do solicitante.
- Definição automática do status inicial como **Aberto**.
- Atribuição de técnicos aos chamados.
- Início do atendimento após a atribuição de um técnico.
- Atualização do status para **Em atendimento**.
- Encerramento de chamados com registro obrigatório da solução.
- Impedimento de alterações em chamados encerrados.
- Listagem de chamados com informações sobre solicitante, técnico, status e solução.

### Regras de negócio

O sistema respeita as seguintes regras:

- Todo chamado deve possuir uma descrição e um usuário solicitante.
- Todo chamado começa com o status **Aberto**.
- Um técnico deve ser atribuído antes do início do atendimento.
- O fluxo de status segue a sequência **Aberto → Em atendimento → Encerrado**.
- Um chamado encerrado não pode ter seu status alterado.
- O encerramento exige o registro de uma solução.

## 6. Testes automatizados

O projeto utiliza a biblioteca `unittest` do Python para verificar o funcionamento das classes, serviços e regras de negócio.

Atualmente, existem **30 testes automatizados**, distribuídos da seguinte forma:

| Arquivo de testes | Quantidade |
|---|---:|
| test_chamado.py | 11 |
| test_chamado_service.py | 6 |
| test_repositorios.py | 4 |
| test_tecnico.py | 3 |
| test_usuario_service.py | 6 |
| **Total** | **30** |

Todos os 30 testes foram executados com sucesso na última execução.

Para executar os testes, utilize:

```bash
python -m unittest discover -s tests -v
```

## 7. Como executar o projeto

### Pré-requisitos

- Python instalado.
- Visual Studio Code ou outro editor de código.
- Git instalado (opcional para execução local).

### Executando o sistema

1. Clone o repositório:

```bash
git clone https://github.com/k4uaxavier/sistema-chamado-ti.git
```

2. Entre na pasta do projeto:

```bash
cd sistema-chamado-ti
```

3. Execute o sistema:

```bash
python main.py
```

4. Utilize as opções apresentadas no menu para cadastrar usuários, cadastrar técnicos e gerenciar chamados.

### Executando os testes

Para executar todos os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

## 8. Observações

O projeto utiliza armazenamento em memória. Portanto, os dados cadastrados são mantidos somente enquanto o programa estiver em execução. Ao encerrar o sistema, os registros são perdidos.

## 9. Desenvolvimento e controle de versão

O projeto utiliza Git e GitHub para controle de versão e acompanhamento do desenvolvimento.

As funcionalidades foram organizadas em branches específicas, permitindo acompanhar as alterações e manter a branch principal (`main`) mais estável.

**Repositório:** https://github.com/k4uaxavier/sistema-chamado-ti

---

**Projeto acadêmico — Sistema de Gerenciamento de Chamados de TI.**