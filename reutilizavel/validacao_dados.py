def validar_nome(): 
     
    while True:

        nome_digitado = input("Digite seu nome: ").strip() #validar nome
        nome_limpo = nome_digitado.replace(" ", "") # remove espaços " " por ""

        if not nome_limpo.isalpha(): #isalpha ve sem espaço ou simbolos/numeros
            print("Erro: Digite apenas letras (sem números ou símbolos).")
            continue # Volta para o início

        if len(nome_digitado) < 3 or len(nome_digitado) > 20:
            print("Erro: O nome deve ter entre 3 e 20 caracteres.")
            continue # Volta para o início

        return nome_digitado

def validar_email():

    while True:
        email_digitado = str(input("Digite um email para contato: ")).strip() # validar email
        email_limpo = email_digitado.replace(" ", "")
        if "@" in email_limpo and "." in email_limpo:
            return email_digitado
        else:
            print("Erro: email invalido, digite novamente")
            continue

def validar_numero():
    while True:
        numero_digitado = input("Digite seu numero para contato: ").strip()

        if not numero_digitado.isnumeric():
            print("Digite apenas numeros. ")
            continue
        if len(numero_digitado) < 7 or len(numero_digitado) > 12:
            print("Erro: Tamanho irregular de numero") 
            continue
        else:
            return numero_digitado
