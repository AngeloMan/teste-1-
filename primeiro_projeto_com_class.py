import os 

clear = lambda: os.system('cls')

def mensagem_erro(opcao):
    if opcao and not opcao in range(1, 3):
        print(opcao)

def mensagem_erro2(opcao):
    if opcao and not opcao in range(1, 5):
        print(opcao)

def get_op1(message):
    erro = 'Digite uma opcao valida!'
    while True:
        try:
            value = float(input(message))
            if value in range(1, 3):
                return value
            else:
                return erro
        except BaseException:
            return erro

def get_indice(item ,message):
    erro = 'Digite uma opcao valida!'
    while True:
        try:
            value = float(input(message))
            if value in range(len(item)):
                return int(value)
            else:
                return erro
        except BaseException:
            return erro

def get_op2(message):
    erro = 'Digite uma opcao valida!'
    while True:
        try:
            value = float(input(message))
            if value in range(1, 5):
                return int(value)
            else:
                return erro
        except BaseException:
            return erro
        
def adicionar_carro(carro):
    clear()
    carro_ = Carro(carro)
    listar_tal(marcas_registradas)
    indice = get_indice(item=marcas_registradas, message="Digite o indice da marca:")
    carro_.marca = marcas_registradas[indice]
    clear()
    listar_tal(motores_registrados)
    indice = get_indice(item=motores_registrados, message="Digite o indice do motor:")
    carro_.motor = motores_registrados[indice]
    carros_registrados.append(carro_)
    
def listar_carros():
    for i in carros_registrados:
        print(i.nome, i.marca.nome, i.motor.nome)  
    input()  

def adicionar_marca(marca):
    marcas_registradas.append(Marca(marca))
def adicionar_motor(motor):
    motores_registrados.append(Motor(motor))
    
def listar_tal(tal):
    for i in range(len(tal)):
        print(i, tal[i].nome)
    if len(tal) == 0:
        print('sem elementos para listar')

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._marca = None
        self._motor = None

    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
class Motor: 
    def __init__(self, nome):
        self.nome = nome
        
class Marca:
    def __init__(self, nome):
        self.nome = nome


marcas_registradas = []
motores_registrados = []        
carros_registrados = [] 

opcao_1 = False

while True:
    clear()
    mensagem_erro(opcao_1)
    print('| 1 - adicionar\n','| 2 - listar',sep='')
    opcao_1 = get_op1('digite uma opção: ')
    
    opcao_2 = False

    if opcao_1 == 1:
        while True:
            clear()
            mensagem_erro2(opcao_2)
            print('| 1 - adicionar marca\n', '| 2 - adicionar motor\n', '| 3 - adicionar carro\n', '| 4 - voltar ao menu', sep='')
            opcao_2 = get_op2('digite uma opção: ')
            if opcao_2 == 1:
                clear()
                marca = str(input("Digite o nome da marca: "))
                adicionar_marca(marca)
            elif opcao_2 == 2:
                clear()
                motor = str(input("Digite o tipo de motor: "))
                adicionar_motor(motor)
            elif opcao_2 == 3:
                clear()
                carro = str(input('Digite o nome do carro: '))
                adicionar_carro(carro=carro)
            elif opcao_2 == 4:
                break
        

    elif opcao_1 == 2:
        while True:
            clear()
            mensagem_erro2(opcao_2)
            print('| 1 - listar marcas\n', '| 2 - listar motores\n', '| 3 - listar carros\n', '| 4 - voltar ao menu', sep='') 
            opcao_2 = get_op2('digite uma opção: ')
            if opcao_2 == 1:
                clear()
                listar_tal(marcas_registradas)
                input()
            elif opcao_2 == 2:
                clear()
                listar_tal(motores_registrados)
                input()
            elif opcao_2 == 3:
                clear()
                listar_carros()
            elif opcao_2 == 4:
                break
            else:
                pass
