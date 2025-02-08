import os 
clear = lambda: os.system('cls')
clear()

def get_valid_alternative(message):
    while True:
        value = str(input(message))
        value = value.lower()
        if len(value) == 1 and value in 'abcd':
            return value
        else:
            print('Digite a letra de uma alternativa valida!')
            
def get_valid_menu_op(message):
    while True:
        value = str(input(message))
        if len(value) == 1 and value in '1234':
            return value
        else:
            print('Digite uma opção valida!')
            
def counter_alternative(counter):
    if counter == 0:
        alternative = 'a'
    if counter == 1:
        alternative = 'b'
    if counter == 2:
        alternative = 'c'
    if counter == 3:
        alternative = 'd'
    return alternative

def counter_alternative_reverse(alternative_given):
    if alternative_given == 'a':
        alternative = 0
    if alternative_given == 'b':
        alternative = 1
    if alternative_given == 'c':
        alternative = 2
    if alternative_given == 'd':
        alternative = 3
    return alternative

def get_valid_remove(message):
    while True:
        try:
            value = float(input(message))
            if (value > 0 and value <= numero_de_perguntas and value == int(value)) or value == 0:
                return value
            else:
                print("Digite um valor valido")
        except ValueError:
            print("Digite um valor valido")
            
def sim_nao(message):
    while True:
        escolha_sim_nao = str(input(message))
        escolha_sim_nao = escolha_sim_nao.lower()
        if escolha_sim_nao == 'sim' or escolha_sim_nao == 's' or escolha_sim_nao == 'n' or escolha_sim_nao == 'nao' or escolha_sim_nao == 'não':
            return escolha_sim_nao
            
            
lista_de_exercicios = {
        'questão': [],
        'alternativas': [],
        'resposta': []
    }

while  True:
    numero_de_perguntas = len(lista_de_exercicios['questão'])
    clear()
    print(' | 1- adicionar questão |\n','| 2- remover questão   |\n','| 3- vizualizar lista  |\n','| 4- fazer lista       |',)
    
    opcao_menu = get_valid_menu_op('Escolha uma opção: ')
    
    if opcao_menu == '1':
        clear()
        counter_n = numero_de_perguntas + 1
        for i in lista_de_exercicios.keys():
            if i == 'questão': 
                print(f"Digite a {i}:")
                entrada = str(input())
                lista_de_exercicios[i].append(entrada)
            elif i == 'alternativas':
                lista_de_exercicios[i].append([])
                for k in range(0, 4):
                    letra = counter_alternative(k)
                    alternativa = str(input(f"Digite a alternativa {letra}) "))
                    lista_de_exercicios[i][numero_de_perguntas].append(alternativa)
            else:
                entrada = get_valid_alternative("Digite a alternativa correta: ")
                lista_de_exercicios[i].append(entrada)
        
    if opcao_menu == '2':
        clear()
        if numero_de_perguntas > 0:
            questao_a_remover = get_valid_remove("Digite o numero da questão que deseja remover: ")
            if questao_a_remover != 0:
                questao_a_remover -= 1
                for i in lista_de_exercicios.keys():
                    lista_de_exercicios[i].pop(int(questao_a_remover))                
        else:
            input("Sem questões para remover!")

    if opcao_menu == '3':
        clear()
        for i in range(0, numero_de_perguntas):
            numero_da_questao = i + 1
            for j in lista_de_exercicios.keys():
                if lista_de_exercicios[j][i] == list(lista_de_exercicios[j][i]):
                    for w in range(0, len(lista_de_exercicios[j][i])):
                        alternativa_p = counter_alternative(w)
                        print(f"{alternativa_p}) {lista_de_exercicios[j][i][w]}")
                    print()
                else:
                    print(f"{j} {numero_da_questao}: {lista_de_exercicios[j][i]}")            
            print()
        input("Press ENTER para voltar ao menu.") 
        
    if opcao_menu == '4':
        clear()
        if numero_de_perguntas > 0:
            acertos = 0
            erros = 0
            for i in range(0, numero_de_perguntas):
                numero_da_questao = i + 1
                print("")
                print(f"{numero_da_questao}- {lista_de_exercicios['questão'][i]}")
                for j in lista_de_exercicios.keys():
                    if lista_de_exercicios[j][i] == list(lista_de_exercicios[j][i]):
                        for w in range(0, len(lista_de_exercicios[j][i])):
                            alternativa_p = counter_alternative(w)
                            print(f"{alternativa_p}) {lista_de_exercicios[j][i][w]}")
                        print()      
                print()
                resposta_do_usuario = get_valid_alternative("Digite a alternativa da resposta: ")
                indice_resposta_do_certa = int(counter_alternative_reverse(lista_de_exercicios['resposta'][i]))
                if lista_de_exercicios['resposta'][i] == resposta_do_usuario:
                    print("voce arcertou!")
                    acertos += 1
                else:
                    print("voce errou!")
                    print(f"A resposta era: {lista_de_exercicios['alternativas'][i][indice_resposta_do_certa]} ")
                    erros += 1
            print()
            opcao_sim_nao = sim_nao("Deseja ver o relatorio? ")
            if opcao_sim_nao == 's' or opcao_sim_nao == 'sim':
                percentual_de_acertos = (acertos/(numero_de_perguntas)) * 100
                print(
                    f' | Acertos: {acertos}\n',
                    f'| Erros:   {erros}\n',
                    f'| Percental:{percentual_de_acertos:.2f}%'
                )
                input()
        else:
            input("Sem questoes para praticar!")
