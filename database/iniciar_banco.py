import sqlite3

def gerar_banco():

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        numero TEXT NOT NULL UNIQUE,
        criacao_data DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'ativo'
    )
    """)

    conexao.commit()
    conexao.close()

