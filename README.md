# Sistema de Gerenciamento de Chamados de TI

## 1. Sobre o projeto

O Sistema de Gerenciamento de Chamados de TI é um projeto acadêmico desenvolvido com o objetivo de facilitar a abertura, o acompanhamento e o gerenciamento de solicitações de suporte técnico.

A proposta é centralizar os chamados de TI em um único sistema, permitindo que usuários registrem problemas e que a equipe técnica possa acompanhar e realizar o atendimento.

O projeto está sendo desenvolvido utilizando conceitos de Programação Orientada a Objetos (POO), organização em camadas e testes automatizados.

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
│   ├── chamado.py
│   ├── status_chamado.py
│   └── excecoes.py
│
├── infraestrutura/
│   ├── __init__.py
│   ├── repositorio_chamados.py
│   └── repositorio_usuarios.py
│
├── tests/
│   ├── __init__.py
│   ├── test_chamado.py
│   ├── test_repositorios.py
│   ├── test_chamado_service.py
│   └── test_usuario_service.py
│
├── main.py
├── README.md
└── .gitignore
```

## 4. Organização do sistema

O sistema está organizado em camadas, separando as responsabilidades de cada parte do projeto.

### Domínio

Contém as classes e regras principais do sistema.

- **Usuario:** representa o usuário que solicita suporte.
- **Chamado:** representa uma solicitação de atendimento técnico.
- **StatusChamado:** define os possíveis estados de um chamado.
- **Excecoes:** contém exceções personalizadas utilizadas pelo sistema.

### Aplicação

Contém os serviços responsáveis por executar as operações do sistema.

**ChamadoService:**
- Abrir novos chamados.
- Verificar se o usuário solicitante existe.
- Validar os dados do chamado.
- Salvar o chamado no repositório.

**UsuarioService:**
- Cadastrar novos usuários.
- Buscar usuários pelo ID.
- Listar todos os usuários cadastrados.

### Infraestrutura

Responsável pelo armazenamento e recuperação dos dados.

**RepositorioChamados:**
- Salvar chamados.
- Buscar chamados pelo ID.
- Listar todos os chamados.

**RepositorioUsuarios:**
- Salvar usuários.
- Buscar usuários pelo ID.
- Listar todos os usuários.

Atualmente, os dados são armazenados em memória, utilizando estruturas de dados do Python.

## 5. Funcionalidades implementadas

Até o momento, foram desenvolvidas as seguintes funcionalidades:

- Criação e validação de chamados.
- Definição automática do status inicial como "Aberto".
- Cadastro de usuários.
- Busca de usuários pelo ID.
- Listagem de usuários cadastrados.
- Armazenamento de chamados em memória.
- Armazenamento de usuários em memória.
- Abertura de chamados por meio do serviço da aplicação.
- Verificação da existência do usuário solicitante antes da abertura de um chamado.
- Tratamento de erros relacionados a operações inválidas.

O arquivo `main.py` possui atualmente uma estrutura inicial de execução do sistema.

## 6. Testes automatizados

O projeto utiliza a biblioteca `unittest` do Python para verificar o funcionamento das classes e operações implementadas.

Atualmente, existem **12 testes automatizados**, distribuídos da seguinte forma:

- **Chamado:** 2 testes.
- **RepositorioChamados:** 1 teste.
- **RepositorioUsuarios:** 3 testes.
- **ChamadoService:** 3 testes.
- **UsuarioService:** 3 testes.

Todos os 12 testes foram executados com sucesso.

Para executar os testes, utilize o comando:

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

### Executando os testes

Para executar todos os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

## 8. Próximas etapas

O projeto continua em desenvolvimento. As próximas etapas incluem:

- Desenvolver a interface de interação pelo terminal.
- Integrar os serviços à interface do sistema.
- Implementar a listagem e consulta de chamados.
- Implementar a atribuição de chamados aos técnicos.
- Implementar a atualização dos status dos chamados.
- Implementar o encerramento de chamados com registro da solução.
- Ampliar os testes automatizados.
- Realizar a revisão geral do sistema.

## 9. Desenvolvimento e controle de versão

O projeto utiliza Git e GitHub para controle de versão e acompanhamento do desenvolvimento.

As funcionalidades são desenvolvidas em branches específicas, permitindo organizar as alterações e manter a branch principal (`main`) mais estável.

**Repositório:** https://github.com/k4uaxavier/sistema-chamado-ti

---

**Projeto acadêmico — Sistema de Gerenciamento de Chamados de TI.**