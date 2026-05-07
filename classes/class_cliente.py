import sqlite3

class Cliente:
    def __init__(self, nome, email, numero):
        self.nome = nome
        self.email = email
        self.numero = numero

    def salvar_no_banco(self):
        conexao = None
        try:
            conexao = sqlite3.connect("banco.db")
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO clientes (nome, email, numero) 
                VALUES (?, ?, ?)
            """, (self.nome, self.email, self.numero))


            conexao.commit()
            print("CLiente cadastrado com sucesso! ")

        except sqlite3.IntegrityError as erro: # Erro de repetição 'IntegrityError' do sqlite

            print( f"email ou número já está cadastrado\n {erro}")

        except Exception as erro: # Erro de conexão 'Exception'  
        
            print(f"Ocorreu um erro inesperado: {erro}")
        
        finally:
                if conexao:
                    conexao.close()

    @staticmethod
    def deletar_usuario(id_para_deletar):
        conexao = None
        try:
            conexao = sqlite3.connect("banco.db")
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM clientes WHERE id = ?", (id_para_deletar,))

            conexao.commit()

            if cursor.rowcount == 0:
                print("Erro: nenhum cliente encontrado com esse ID.")
            else:
                print("Cliente deletado com sucesso.")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")
        
        finally:
            if conexao:
                conexao.close()

