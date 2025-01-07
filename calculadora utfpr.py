#calculadora de nota utfpr 2024/2025
import os
clear = lambda: os.system('cls')
a=(' ________________________________________ ')
b=('|                                        |')
c=('|    DIGITE UM VALOR DENTRO DA ESCALA    |')
d=('| PRESSIONE ENTER PARA TENTAR NOVAMENTE  |')
e=('|________________________________________|')

def get_a_valid_option(message):
    while True:
        try:
            clear()
            print('calculadora de nota utfpr 2024/2025')
            print('ORDEM DE PESO POR MATÉRIA DOS CURSOS: (redação/matematica/naturezas/humanas/linguagens)')
            print(' ________________________________________ ')
            print('|             OPÇÔES DE CURSOS:          |')
            print('|----------------------------------------|')
            print('|      1- CURSOS DE PESO (1/4/2/1/1)     |')
            print('|      2- CURSOS DE PESO (1/1/1/1/1)     |')
            print('|      3- CURSOS DE PESO (1/4/3/1/1)     |')
            print('|      4- CURSOS DE PESO (1/3/3/1/1)     |')
            print('|      5- CURSOS DE PESO (1/3/1/2/2)     |')
            print('|      6- CURSOS DE PESO (1/3/2/2/1)     |')
            print('|----------------------------------------|')
            print('|             OPÇÕES DO MENU:            |')
            print('|----------------------------------------|')
            print('|      8-TABELA DE PESOS POR CURSO       |')
            print('|________________________________________|')
            value = int(input(message))
            if (value == 1) or (value == 2) or (value == 3) or (value == 4) or (value == 5) or (value == 6) or (value == 8):
                    return value
            else:
                print(' ________________________________________ ')
                print('|                                        |')
                print('|         TENTE UMA OPÇÃO VALIDA         |')
                print('| PRESSIONE ENTER PARA TENTAR NOVAMENTE  |')
                input('|________________________________________|')
                
                 
               
        except ValueError:
            print(' ________________________________________ ')
            print('|                                        |')
            print('|         TENTE UMA OPÇÃO VALIDA         |')
            print('| PRESSIONE ENTER PARA TENTAR NOVAMENTE  |')
            input('|________________________________________|')
                    
def get_0_to_8(message):
    while True:
        try:
            value = int(input(message))
            if (value >= 0) and (value <= 8):
                return value
            else:
                print(a)
                print(b)
                print(c)
                print(d)
                print(e)
        except ValueError:
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)

def get_0_to_6(message):
    while True:
        try:
            value = int(input(message))
            if (value >= 0) and (value <= 6):
                return value
            else:
                print(a)
                print(b)
                print(c)
                print(d)
                print(e)
        except ValueError:
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            
def get_0_to_4(message):
    while True:
        try:
            value = int(input(message))
            if (value >= 0) and (value <= 4):
                return value
            else:
                print(a)
                print(b)
                print(c)
                print(d)
                print(e)
        except ValueError:
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            
def get_0_to_100(message):
    while True:
        try:
            value = int(input(message))
            if (value >= 0) and (value <= 100):
                return value
            else:
                print(a)
                print(b)
                print(c)
                print(d)
                print(e)
        except ValueError:
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
                           

while True:


        clear = lambda: os.system('cls')
        clear()
        opcao = get_a_valid_option('digite o numero da sua opção e pressione ENTER: ')
        
        if (opcao == 1) or (opcao == 2) or (opcao == 3) or (opcao == 4) or (opcao == 5) or (opcao == 6):
            clear = lambda: os.system('cls')
            clear()
            red = get_0_to_100('Digite a sua nota da readação de 0 a 100: ')  
            mat = get_0_to_8('Digite os seus acertos em matematica de 0 a 8: ')
            fis = get_0_to_8('Digite os seus acertos em fisica 0 a 8: ')
            qui = get_0_to_8('Digite os seus acertos em quimica 0 a 8: ')
            bio = get_0_to_6('Digite os seus acertos em biologia 0 a 6: ')
            fiso = get_0_to_4('Digite os seus acertos em filosofia e sociologia de 0 a 4: ')
            geo = get_0_to_4('Digite os seus acertos em geografia de  0 a 4: ')
            his = get_0_to_4('Digite os seus acertos em historia de  0 a 4: ')
            lin = get_0_to_6('Digite os seus acertos em lingua estrangeira de  0 a 6: ')
            port = get_0_to_8('Digite os seus acertos em portugues de  0 a 8: ')
            lit = get_0_to_4('Digite os seus acertos em literatura de  0 a 4: ')
            
            if opcao == 1 : 
                nota = ((((4*mat)/(8))+(2*(((fis)/8)+((qui)/8)+((bio)/6)))+((red)/100)+(((fiso)/4)+((geo)/4)+((his)/4)+((lin)/6)+((port)/8)+((lit)/4)))/(17))
            elif opcao == 2 :
                nota = ((((1*mat)/(8))+(1*(((fis)/8)+((qui)/8)+((bio)/6)))+((red)/100)+(((fiso)/4)+((geo)/4)+((his)/4)+((lin)/6)+((port)/8)+((lit)/4)))/(11))
            elif opcao == 3 :
                nota = ((((4*mat)/(8))+(3*(((fis)/8)+((qui)/8)+((bio)/6)))+((red)/100)+(((fiso)/4)+((geo)/4)+((his)/4)+((lin)/6)+((port)/8)+((lit)/4)))/(20))
            elif opcao == 4 :
                nota = ((((3*mat)/(8))+(3*(((fis)/8)+((qui)/8)+((bio)/6)))+((red)/100)+(((fiso)/4)+((geo)/4)+((his)/4)+((lin)/6)+((port)/8)+((lit)/4)))/(19))
            elif opcao == 5 :
                nota = ((((3*mat)/(8))+(1*(((fis)/8)+((qui)/8)+((bio)/6)))+((red)/100)+(2 * (((fiso)/4)+((geo)/4)+((his)/4)+((lin)/6)+((port)/8)+((lit)/4))))/(19))
            elif opcao == 6 :
                nota = ((((3*mat)/(8))+(2*(((fis)/8)+((qui)/8)+((bio)/6)))+((red)/100)+((((2 * fiso)/4)+((2 * geo)/4)+((2 * his)/4)+((lin)/6)+((port)/8)+((lit)/4))))/(19))
            
            clear()
            acertos = mat + fis + qui + bio + fiso + geo + his + lin + port + lit
            notafinal = int(nota * 1000)
            print(' ________________________________________ ')
            print('|               ACERTOS TOTAL:           |')
            print('|----------------------------------------|')
            print('|                  ',acertos,'                  ')
            print('|----------------------------------------|')
            print('|               NOTA FINAL:              |')
            print('|----------------------------------------|')
            print('|                  ',notafinal,'                  ')
            print('|________________________________________|')
            input('pressione ENTER para voltar ao menu')
            continue

        if opcao==8 :
            clear()
            print('pressione ENTER para voltar ao menu')
            print('ORDEM DE PESO POR MATÉRIA DOS CURSOS: (redação/matematica/naturezas/humanas/linguagens)')
            print('_____________________________________________________________________________________________________')
            print('1- CURSOS DE PESO (1/4/2/1/1): ')
            print('   | ENGENHARIA AMBIENTAL E SANITÁRIA      | ENGENHARIA CIVIL        | ENGENHARIA DE ALIMENTOS      | ')
            print('   | ENGENHARIA DE CONTROLE E AUTOMAÇÃO    | ENGENHARIA DE MATERIAIS | ENGENHARIA DE PRODUÇÃO       | ')
            print('   | ENGENHARIA ELETRÔNICA                 | ENGENHARIA MECÂNICA     | ENGENHARIA MECATRÔNICA       | ')
            print('   | QUÍMICA, QUÍMICA INDUSTRIAL           | SISTEMAS DE INFORMAÇÃO  | MATEMÁTICA                   | ')
            print('   | AUTOMAÇÃO INDUSTRIAL                  | MANUTENÇÃO INDUSTRIAL   | SISTEMAS DE TELECOMUNICAÇÕES | ')
            print('   | ENGENHARIA DE COMPUTAÇÃO              | ENGENHARIA ELETRICA     | CIÊNCIA DA COMPUTAÇÃO        | ')
            print('   | ANÁLISE E DESENVOLVIMENTO DE SISTEMAS | ENGENHARIA DE SOFTWARE  | SISTEMAS PARA INTERNET       |')
            print('_____________________________________________________________________________________________________')
            print('2- CURSOS DE PESO (1/1/1/1/1): ')
            print('   | ENGENHARIA FLORESTAL                  | AGRONOMIA               | ARQUITETURA E URBANISMO      | ')
            print('   | COMUNICAÇÃO ORGANIZACIONAL            | CIÊNCIAS CONTÁBEIS      | DESIGN GRÁFICO               | ')
            print('   | DESIGN                                | ZOOTECNIA               | CIENCIAS BIOLOGICAS          | ')
            print('   | LETRAS PORTUGUÊS - INGLES             | LETRAS PORTUGUÊS        | ALIMENTOS                    | ')
            print('   | DESIGN DE MODA                        |  GESTÃO DO AGRONEGÓCIO  |                              |') 
            print('_____________________________________________________________________________________________________')
            print('3- CURSOS DE PESO (1/4/3/1/1): ')
            print('   | ENGENHARIA DE BIOPRO. E BIOTECN.      | ENGENHARIA QUIMICA      |  ENGENHARIA TÊXTIL           |')
            print('   | QUIMICA AMBIENTAL                     | QUÍMICA                 | PROCESSOS QUÍMICOS           |')
            print('_____________________________________________________________________________________________________')
            print('4- CURSOS DE PESO (1/3/3/1/1): ')
            print('   |  RADIOLOGIA                           |                         |                              |')
            print('_____________________________________________________________________________________________________')
            print('5- CURSOS DE PESO (1/3/1/2/2): ')
            print('   |   ADMINISTRAÇÃO                       |                         |                              |')
            print('_____________________________________________________________________________________________________')
            print('6- CURSOS DE PESO (1/3/2/2/1): ')
            print('   | ENGENHARIA CARTOGRÁFICA E DE AGRIM.   |                         |                              |')
            print('_____________________________________________________________________________________________________')
            print('pressione ENTER para voltar ao menu')
            print('ORDEM DOS PESOS:(redação/matematica/naturezas/humanas/linguagens)') 
                     
            input()
            continue