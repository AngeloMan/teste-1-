from os import system
from .corpohtml import*

clear = lambda: system('cls')

def opcao_menu(len_, message):
    erro = "Opçäo invalida!"
    while True:
        try:
            value = float(input(message))
            if value in range(1, len_ + 1):
                return int(value)
            raise BaseException
        except BaseException:
            print(erro)

def get_gmail(message):
    erro = "GMAIL invalido!"
    while True:
        try:
            value = str(input(message))
            value = value.lower()
            if "@gmail.com" in value:
                return value
            raise BaseException
        except BaseException:
            clear()
            print(erro)
            return False       
            
            
if __name__ == "__main__":
    while True:
        ...
        # a = opcao_menu(4, "Digite: ")
        # print(a)
        email = get_gmail("gmail: ")
        print(email)