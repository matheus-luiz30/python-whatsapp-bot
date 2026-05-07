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

1_Função dos Diretórios e Arquivos

### main.py

- iniciar o banco de dados
- chamar as funções de validação
- criar o cliente
- executar o fluxo principal do programa


### classes/

Diretório responsável pelas classes do sistema.

### class_cliente.py

- armazenar informações do cliente
- salvar clientes no banco de dados
- deletar clientes
- tratar erros relacionados ao SQLite

### database/

### banco.db

armazena:
- nome
- email
- número
- data de criação
- status do cliente

### iniciar_banco.py

- criar conexão SQLite
- criar tabela `clientes`
- definir estrutura do banco
