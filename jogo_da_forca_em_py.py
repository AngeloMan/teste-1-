import os 
clear = lambda: os.system('cls')
clear()

def get_mono_str(message):
    while True:
        try:
            value = str(input(message))
            value = value.lower()
            if (len(value) == 1) and (value in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']):
                return value
            else: 
                print("Digite apenas um caractere valido")      
        except ValueError:
            print("Digite apenas um caractere valido")
            
def get_option(message):
    while True:
        try:
            value = str(input(message))
            value = value.lower()
            if value == "n" or value == "nao" or value == "não" or value == "s" or value == "sim":
                return value
            else: 
                print("Digite uma opção valida")      
        except ValueError:
            print("Digite uma opção valida")    
            
def get_valid_world(message):
    while True:
        try:
            x = 0
            value = str(input(message))
            value = value.lower()

            for i in range(0, len(value)):
                if value != ' ' and (value[i] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', ' ']):
                    x = x + 0
                else:
                    x = x + 1   
                    
            for i in range(0, len(value)):
                if i < len(value) - 1:
                    if value[i] == ' ' and value[i + 1] == ' ':
                        x = x + 1 
                    else:
                        x = x + 0
                    
            if not bool(value) != True:
                x = x + 0
            else:
                x = x + 1
            if x == 0:
                return value
            
            else:
                clear()
                print("Digite uma palavra valida")              
        except ValueError:
            clear()
            print("Digite uma palavra valida")

while True:
    clear()
    palavra = get_valid_world("Digite a palavra: ")
    clear()
    pl = palavra
    letras_descobertas = "_" * len(pl) 
    letras_descobertas = list(letras_descobertas)
    palavra = list(palavra)
    n = palavra
    chances = 6
    digitos = []
    k = 0

    if " " in palavra:
        for i in range(0, len(palavra)):
            if " " == palavra[i]:
                letras_descobertas[i] = " "
        
        for i in range(0, len(n)):
            if " " in n:
                n.remove(" ")
            else:
                pass
                
        
    while (len(n) > 0) and (chances > 0.1):
        print("A palavra tem", len(n), "letras restantes e", end="")
        print(f' voce tem {chances:.0f} chances.')
        chancest = chances
        tentativa = get_mono_str("\nDigite uma letra: ")
        if tentativa in digitos:
            print('voce ja digitou essa letra')
            continue
        digitos.append(tentativa)
        if tentativa in n:
            for i in range(0, len(pl)): 
                if tentativa in n:  
                    n.remove(tentativa)
                    i = len(palavra)
                else:
                    pass
            for i in range(0, len(pl)): 
                if str(tentativa) == str(pl[i]):
                    letras_descobertas[i] = str(tentativa)
        elif not tentativa in palavra:
            chances = (chances - 1)
            
        clear()
        lenn = len(n)
        if chancest > chances:
            print('Voce errou')    
        else:
            print('Voce acertou')
        print("forca:")
        if chances > 5:
            print('----\n', '|  |\n', '| vazia\n', '| \n', '| \n', '|  ', sep='')
        elif chances > 4 and chances < 5.5:
                print('----\n', '|  |\n', '|  O\n', '| \n', '| \n', '|  ', sep='')
        elif chances > 3 and chances < 4.5:
                print('----\n', '|  |\n', '|  O\n', '| / \n', '|  \n', '|  ', sep='')
        elif chances > 2 and chances < 3.5:
                print('----\n', '|  |\n', '|  O\n', '| /| \n', '|  \n', '|  ', sep='')
        elif chances > 1 and chances < 2.5:
                print('----\n', '|  |\n', '|  O\n', '| /|\ \n', '|  \n', '|  ', sep='')
        elif chances > 0.5 and chances < 1.5:
                print('----\n', '|  |\n', '|  O\n', '| /|\ \n', '| /  \n', '|  ', sep='')
        elif chances > -1 and chances < 1:
                print('----\n', '|  |\n', '|  O\n', '| /|\ \n', '| / \ \n', '|  ', sep='')
        
        print('\nLetras descobretas: ', end='')
        for i in range(0, len(letras_descobertas)):
            print(f"{letras_descobertas[i]} ", end='')
        print('')
        if len(n) > 0:
            print(f"Voce ja digitou os caracteres: ", end='')   
            for i in range(0, len(digitos)):
                print(f"'{digitos[i]}' ", end='')
            print('')
                    
    clear()   
    if len(n) == 0:
        print(
                '   ___________    \n',
                '  :._=_==_=_.:    \n',
                '.-\:        :/-.    \n',
                '| (|vencedor|) |   \n',
                ' :-|:.      |-:    \n',
                '    \::.    /      \n',
                '     ::. .::       \n',
                '       ) (         \n',
                '     _.:_:._         '
        )
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")
        print(
            '----\n',
            '|  |\n',
            '|  O\n',
            '| /|\ \n',
            '| / \ \n',
            '|  ',
            sep=''       
            )
    print(f" A palavra era {pl.upper()}.\n")
    
    opcao_de_continuidade = get_option("Deseja continuar? ")
    if opcao_de_continuidade == "n" or opcao_de_continuidade == "nao" or opcao_de_continuidade == "não":
        break
    else:
        continue
