# Sistema de Gerenciamento de Chamados de TI

## 1. Sobre o projeto

O Sistema de Gerenciamento de Chamados de TI é um projeto acadêmico desenvolvido na disciplina de Programação Orientada a Objetos.

O objetivo é desenvolver uma aplicação que permita centralizar e organizar solicitações de suporte técnico, facilitando o registro, acompanhamento e gerenciamento de chamados de TI.

O sistema prevê diferentes tipos de usuários, como solicitantes, técnicos e administradores.

## 2. Tecnologias utilizadas

- **Linguagem:** Python
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Editor de código:** Visual Studio Code
- **Controle de versão:** Git e GitHub
- **Testes automatizados:** unittest

## 3. Estrutura do projeto

```text
sistema-chamado-ti/
│
├── aplicacao/
│   └── __init__.py
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
│   └── test_repositorios.py
│
├── main.py
├── README.md
└── .gitignore
```

## 4. Funcionalidades desenvolvidas

Até o momento, foram implementadas as seguintes partes:

### Classes do domínio

- **Usuario:** representa o usuário solicitante, contendo identificador, nome e e-mail.
- **Chamado:** representa uma solicitação de suporte técnico, contendo descrição, status, data de abertura, solução e solicitante.
- **StatusChamado:** define os estados possíveis de um chamado: ABERTO, EM_ATENDIMENTO e ENCERRADO.
- **Exceções personalizadas:** utilizadas para tratar situações inválidas durante as operações do sistema.

### Repositórios

Foram desenvolvidas duas classes para armazenamento de dados em memória, utilizando dicionários Python:

**RepositorioChamados**
- Salvar chamados com geração automática de identificadores.
- Buscar chamados pelo ID.
- Listar todos os chamados cadastrados.

**RepositorioUsuarios**
- Salvar usuários com geração automática de identificadores.
- Buscar usuários pelo ID.
- Listar todos os usuários cadastrados.

### Inicialização do sistema

O arquivo `main.py` foi organizado como ponto de entrada da aplicação, apresentando uma mensagem de inicialização do sistema.

## 5. Testes automatizados

Foram criados testes utilizando a biblioteca `unittest`, com o objetivo de verificar o funcionamento das classes e a integração entre os componentes.

Até o momento, foram implementados:

- Teste unitário para verificar se um chamado inicia com o status ABERTO.
- Teste unitário para verificar se uma descrição vazia gera uma exceção.
- Teste de integração para verificar o salvamento e a recuperação de um chamado pelo repositório.

**Resultado atual:** 3 testes executados com sucesso.

### Como executar os testes

Para executar todos os testes, utilize o comando:

```bash
python -m unittest discover -s tests -v
```

## 6. Como executar o projeto

### Pré-requisitos

- Python instalado.
- Visual Studio Code (recomendado).

### Execução

1. Clone o repositório:

```bash
git clone https://github.com/k4uaxavier/sistema-chamado-ti.git
```

2. Entre na pasta do projeto:

```bash
cd sistema-chamado-ti
```

3. Execute o programa:

```bash
python main.py
```

## 7. Armazenamento de dados

Nesta etapa do desenvolvimento, os dados são armazenados temporariamente em dicionários Python.

Isso significa que os registros são mantidos somente enquanto o programa está em execução. A persistência em banco de dados não foi implementada até o momento.

## 8. Próximas etapas

O projeto continuará sendo desenvolvido gradualmente. As próximas etapas previstas são:

- Implementação dos serviços da aplicação.
- Desenvolvimento da interface de terminal.
- Abertura e listagem de chamados.
- Atribuição de técnicos aos chamados.
- Atualização dos status.
- Encerramento de chamados com registro da solução.
- Ampliação dos testes automatizados.
- Melhorias na documentação e organização do código.

## 9. Desenvolvimento em equipe

O projeto utiliza Git e GitHub para controle de versão e colaboração entre os integrantes.

O desenvolvimento é organizado por meio de branches, permitindo que cada integrante trabalhe em partes específicas do sistema antes da integração à branch principal (`main`).

### Ampliação dos testes automatizados

Foram adicionados três novos testes para a classe `RepositorioUsuarios`, verificando:

- O salvamento de usuários.
- A busca de usuários pelo identificador.
- A listagem dos usuários cadastrados.

Após a implementação, foram executados todos os testes automatizados do projeto, totalizando seis testes aprovados.
---

**Projeto acadêmico — Sistemas de Informação.**
