import os 
clear = lambda: os.system('cls')
clear()
'''prototipo primitivo'''
# def get_score_name(message):
#     menssagem_de_erro = "Digite nome, nota valida!"
#     while True:
#         try:
#             dados = input(message)
#             dados = dados.split(',')           
#             if len(dados) == 2:
#                 for i in range(0, len(dados)):
#                     dados[i] = dados[i].strip()
#                 if float(dados[1]) >= 0 and float(dados[1]) <= 3420:
#                     dados[0] = dados[0].upper()
#                     return dados  
#                 else:
#                     print(menssagem_de_erro)  
#             else:
#                 print(menssagem_de_erro)         
#         except ValueError:
#             print(menssagem_de_erro) 
            
# lista_primitiva = []
# x = 0 
            
# while True:
#     x = x + 1
#     nome_nota = get_score_name("Digite [nome], [nota]: ")
#     clear()
#     if x == 1: 
#         lista_primitiva.append(nome_nota)
#         for a, b in enumerate(lista_primitiva, start=1):
#             print(f"{a} ", end='')
#             for w in b:
#                 print(f"{w} ", end='')
#             print()
#     if x > 1:
#         lista_ordem = list(" " * x)
#         lista_primitiva = list(lista_primitiva)
#         lista_primitiva.append(nome_nota)
#         lista_modelar = lista_primitiva
#         lista_primitiva = tuple(lista_primitiva)
#         for i in range(0, len(lista_primitiva)):
#             elemento_maior = ['none', -0.1]
#             for j in lista_modelar:
#                 if float(j[1]) > float(elemento_maior[1]):
#                     elemento_maior = j
#                     clone_delecao = j
#             lista_modelar.remove(clone_delecao)
#             lista_ordem[i] = elemento_maior
            
#         for a, b in enumerate(lista_ordem, start=1):
#             print(f"{a} ", end='')
#             for w in b:
#                 print(f"{w} ", end='')
#             print()

'''projeto final simples'''

def recieve_name_score(message):
    while True:
        try:
            value = str(input(message))
            value = value.split(',')
            if len(value) == 2 and (float(value[1]) or float(value[1]) == 0):
                value[1] = float(value[1])
                return value
            else:
                pass
            print("Erro")
        except ValueError:
            print("Erro")
            
def print_lista(lista):
    ordem = 1
    for i in lista:
        print(f"{ordem}", end=' | ')
        ordem += 1
        for j in range(len(i)):
            print(f'{i[j]}', end=' | ')
        print()           

lista = []
while True:  
    clear()
    dados = recieve_name_score("Digite: ")
    lista.append(dados)
    print('\nordem pontuacao\n')
    lista = sorted(lista, key=lambda item: item[1])
    lista = lista[::-1]
    print_lista(lista)
    
    print('\nordem chamada\n')
    lista = sorted(lista, key=lambda item: item[0])
    print_lista(lista)
    input()
