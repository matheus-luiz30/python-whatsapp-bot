## Estrutura do Projeto

python-whatsapp-bot/
│
├── main.py
│
├── classes/
│   └── class_cliente.py
│
├── database/
│   ├── banco.db
│   └── iniciar_banco.py
│
 ── reutilizavel/
    └── validacao_dados.py


## Função dos Diretórios e Arquivos

### main.py

- iniciar o banco de dados
- chamar as funções de validação
- criar o cliente
- executar o fluxo principal do programa


### classes/

Diretório responsável pelas classes do sistema.

Utilizado para separar estruturas principais da aplicação.

### class_cliente.py

- armazenar informações do cliente
- salvar clientes no banco de dados
- deletar clientes
- tratar erros relacionados ao SQLite

Centraliza a lógica relacionada aos clientes.

### database/

Diretório responsável pelos arquivos relacionados ao banco de dados.


### banco.db

armazena:
- nome
- email
- número
- data de criação
- status do cliente

### iniciar_banco.py

Arquivo responsável pela criação do banco de dados.

- criar conexão SQLite
- criar tabela `clientes`
- definir estrutura do banco

Executado no início da aplicação.

---

### reutilizavel/

Diretório utilizado para funções reutilizáveis do sistema.

Ainda em andamento

---

### validacao_dados.py

Responsável pelas validações de entrada do usuário.

- validar nome
- validar email
- validar número

---


#_____________________________________________________________#

## Direções Futuras

A proposta do projeto é evoluir para um sistema fullstack de atendimento automatizado, utilizando Python, banco de dados, APIs e interface web.

---

## Objetivos Futuros

- Integração com API do WhatsApp
- Criação de painel administrativo web
- Sistema de login
- Histórico de atendimentos
- Organização de chamados técnicos
- Estruturação de backend mais escalável

---

## O que ainda falta

- Interface gráfica
- Integração real com WhatsApp
- API funcional
- Sistema de autenticação
- Hospedagem online
- Estrutura frontend
