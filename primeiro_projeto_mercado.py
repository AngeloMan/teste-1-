import os 
import random
clear = lambda: os.system('cls')

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
            
def get_valid_code(message):
    global codigos_cadastrados
    erro = 'Digite um codigo valido!'
    while True:
        try:
            value = int(input(message))
            if value in codigos_cadastrados or value == -1:
                return value
            print(erro)
        except ValueError:
            print(erro)
            
def get_indice(message):
    global codigos_cadastrados
    erro = 'Digite um indice valido!'
    while True:
        try:
            value = int(input(message))
            if value < indice and value >= -1:
                return value
            print(erro)
        except ValueError:
            print(erro)

def get_valid_code_amount(message):
    global codigos_cadastrados
    erro = 'Digite um codigo e (quantia/peso) valida!'
    while True:
        try:
            value = str(input(message))
            value = value.split(',')
            if len(value) == 2 and int(value[0]) and float(value[1]):
                if int(value[0]) in codigos_cadastrados:
                    value[0] = int(value[0])
                    value[1] = float(value[1])
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

produtos = []
codigos_cadastrados = set()

while True:
    
    clear()        
    print(' | 1 - Adicionar produto \n', '| 2 - Remover produto   \n', '| 3 - conferir lista de produtos\n' ,'| 4 - corrigir valores geral\n' , '| 5 - simular compra')
    
    opcao_menu = get_valid_menu_option("Digite o numero da opção desejada: ")
    
    if opcao_menu == 1:
        k = 0
        while True:
            k +=1
            x = random.randint(1, 200)
            if x not in codigos_cadastrados:
                codigos_cadastrados.add(x)
                break
            elif k > 11:
                input('Limite de produtos estorado')
                k = -1
                break
        if k != -1:
            entrada = receber_nome_preco("digite nome, preco: ")
            print(entrada)

            produtos.append({'nome': entrada[0], 'preco': entrada[1], 'codigo': x})
        
    if opcao_menu == 2:
        if len(codigos_cadastrados) > 0:
            clear()
            for i in produtos:
                print(i)

            codigo_a_deletar = get_valid_code('Digite o codigo do produto que deseje remover do sistema: ')
            if codigo_a_deletar == -1:
                pass
            else:
                for i in produtos:           
                    if codigo_a_deletar == int(i['codigo']):
                        produtos.remove(i)
                        codigos_cadastrados.remove(codigo_a_deletar)       
        else:
            print("Sem nada a remover")
            input()
                
    
    if opcao_menu == 3:
        if len(produtos) > 0:
            for i in produtos:
                print(i)
                
            print(codigos_cadastrados)
            input()
        else:
            input("Sem produtos no sistema!")
        
    if opcao_menu == 4:
        correcao_percentual = get_valid_percent("Digite a porcentagem a ser alterada: ")
        porcentagem = 1 + (correcao_percentual/100)
        if len(produtos) > 0:
            produtos = [
                {**produtos, 'preco' : produtos['preco'] * porcentagem}
                for produtos in produtos
            ]
        else:
            input("Sem produtos no sistema!")
        
    if opcao_menu == 5:
        if len(produtos) > 0:
            clear()
            carrinho = []
            while True:
                clear()
                if len(carrinho) > 0:
                    total = 0.0
                    print("CARRINHO:")
                    for a, b, c, d in carrinho:
                        print(f'| Quantidade/peso: {a}, produto: {b}, codigo: {c}, preço total: {d:.2f}')
                        total += float(d)
                    print(f'SUBTOTAL: {total}')
                    print()
                print(' | 1 - coferir tabela de produtos \n', '| 2 - remover produto do carrinho \n', '| 3 - adicionar produto ao carrinho\n','| 4 - finalizar compra')
                opcao_simulacao = get_valid_menu_option2("Digite o numero da opção desejada: ")
                if opcao_simulacao == 1:
                    clear()
                    for i in produtos:
                        print(i)
                    input()
                if opcao_simulacao == 3:
                    clear()
                    for i in produtos:
                        print(i)
                    cod_quan = get_valid_code_amount("digite o codigo, quantia do produto: ")
                    temporario = []
                    for i in produtos:
                        if cod_quan[0] == i['codigo']: 
                            preco_total = float(i['preco']) * cod_quan[1]     
                            temporario.append(cod_quan[1])
                            temporario.append(i['nome'])
                            temporario.append(i['codigo'])
                            temporario.append(preco_total)
                    carrinho.append(temporario)
                if opcao_simulacao == 2:
                    clear()
                    if len(carrinho) > 0:
                        indice = 0
                        for a, b, c, d in carrinho:
                            print(f'| indice: {indice}, Quantidade/peso: {a}, produto: {b}, codigo: {c}, preço total: {d:.2f}')
                            indice += 1       
                        indice_remover = get_indice("Digite o indice do produto que deseja remover: ")
                        if indice_remover == -1:
                            pass
                        else:
                            carrinho.pop(indice_remover)
                        
                    else:
                        print("nada a remover!")
                        input()  
                        
                if opcao_simulacao == 4:
                    clear()
                    print("CARRINHO FINAL:")
                    total = 0.0
                    for a, b, c, d in carrinho:
                        print(f'| Quantidade/peso: {a}, produto: {b}, codigo: {c}, preço total: {d:.2f}')
                        total += float(d)
                    print()
                    
                    print(f"Valor a pagar: {total:.2f}")
                    input()
                    break
        else:
            input("sem produtos no sistema para a simulação!")
