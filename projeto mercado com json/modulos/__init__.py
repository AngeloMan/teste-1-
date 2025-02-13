from .codigo import*

def receber_nome_preco(message):
    erro = 'Digite (str), (float)!'
    while True:
        try:
            value = str(input(message))
            value = value.split(',')
            if len(value) == 2 and float(value[1]):
                value[1] = float(value[1])
                return value
            print(erro)
        except ValueError:
            print(erro)

def get_valid_menu_option(message):
    erro = 'Digite uma opção válida!'
    while True:
        try:
            value = int(input(message))
            if int(value) and value in range(1, 6):
                return value
            print(erro)
        except ValueError:
            print(erro)
 
def get_valid_menu_option2(message):
    erro = 'Digite uma opção válida!'
    while True:
        try:
            value = int(input(message))
            if int(value) and value in range(1, 6):
                return value
            print(erro)
        except ValueError:
            print(erro)   
            
def get_valid_percent(message):
    erro = 'digite uma porcentagem valida!'
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print(erro)        