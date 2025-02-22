def opcao_menu(message):
    error = 'opção inválida!'
    while True:
        try:
            value = float(input(message))
            if value in range(1, 3):
                return value
            print(error)
        except BaseException:
            print(error)
            
def opcao_kart(message):
    error = 'opção inválida!'
    while True:
        try:
            value = float(input(message))
            if value in range(1, 6):
                return value
            print(error)
        except BaseException:
            print(error)
            
def opcao_produto(message):
    error = 'opção inválida!'
    while True:
        try:
            value = float(input(message))
            if value in range(1, 6):
                return value
            print(error)
        except BaseException:
            print(error)
            
def pegar_preco(message):
    error = 'opção inválida!'
    while True:
        try:
            value = float(input(message))
            if value:
                return value
        except BaseException:
            print(error)
            
def pegar_nome(message):
    error = 'opção inválida!'
    while True:
        try:
            value = str(input(message))
            return value
        except BaseException:
            print(error)
            
def pegar_int(message):
    error = 'valor invalido'
    while True:
        try:
            value = float(input(message))
            if int(value):
                return value
            print(error)
        except BaseException:
            print(error)

def get_indice(len_):
    error = 'indice invalido'
    while True:
        try:
            value = float(input("Digite o indice a remover: "))
            if int(value) == value and int(value) in range(len_):
                return int(value)
            print(error)
        except BaseException as e:
            print(error, e)  

def pegar_int_positivo(message):
    error = 'valor invalido'
    while True:
        try:
            value = float(input(message))
            if int(value) == value and value > 0:
                return value
            print(error)
        except BaseException:
            print(error)
            
def pegar_porcentagem(message):
    error = 'indice invalido'
    while True:
        try:
            value = float(input(message))
            if int(value):
                return 1 + (value/100)
            print(error)
        except BaseException:
            print(error)
            
if __name__ == '__main__':
    while True:
        nome = pegar_nome('teste: ')
        