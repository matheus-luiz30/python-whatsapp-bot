from classes.class_cliente import Cliente 
from database.iniciar_banco import gerar_banco
from reutilizavel.validacao_dados import validar_nome, validar_email, validar_numero

gerar_banco()

nome_final = validar_nome()
email_final = validar_email()
numero_final = validar_numero()

novo_cliente = Cliente(nome_final, email_final, numero_final)
novo_cliente.salvar_no_banco()