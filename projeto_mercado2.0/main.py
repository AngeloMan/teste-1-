import os
from manipulacao_arquivos import *
from defs import*
# classes
class Carrinho:
    def __init__(self):
        self.items = carrinho_salvo
    def add(self, nome, preco, quantia):
        self.items.append({'nome': nome, 'preco': preco, 'quantia': quantia, 'total_produto': preco * quantia})
        
class Produtos:
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco 
        self.codigo = codigo
        
#funcoes          
 
def salvar_kart():
    carrinho_salvo = carrinho.items       
    with open(file_kart, 'w') as file:
        json.dump(carrinho_salvo, file, indent=2)
    
def salvar_prod():
    produtos_covertido = []
    for prod in produtos_salvos:
        produtos_covertido.append(vars(prod))

    with open(file_prod, 'w') as file:
        json.dump(produtos_covertido, file, indent=2)
        
def atualizar_code():
    global code
    code = code + 1
    with open(file_code, 'w') as file:
        json.dump(code, file, indent=2)

clear = lambda: os.system('cls')

# carregamento de dados salvos
if len(produtos_covertido) > 0:
    produtos_salvos = []
    for produto_dict in produtos_covertido:
        produtos_salvos.append(Produtos(**produto_dict))
else:
    produtos_salvos = []        
produtos_covertido = []

# CODIGO PRODUTO

          
# corpo do codigo
if __name__ == '__main__':
  
    while True:

        clear()
        print('| 1 - opções produtos \n', '| 2 - opções carrinho', sep='')
        opcao1 = opcao_menu('digite uma opção: ')
        
        if opcao1 == 1:
            while opcao1 == 1:
                clear()
                # print(produtos_covertido)
                print('| 1 - adicionar produtos \n', '| 2 - remover produtos\n', '| 3 - alterar preços\n', '| 4 - listar produtos\n', '| 5 - voltar ao menu', sep='')
                opcaop = opcao_produto('digite uma opção: ') 
                if opcaop == 1:
                    clear()
                    nome = pegar_nome("Digite o nome do produto: ")
                    preco = pegar_preco('Digite o preço do produto: ')
                    produtos_salvos.append(Produtos(nome, preco, code))
                    atualizar_code()
                    salvar_prod() 

                if opcaop == 2:
                    clear()
                    if produtos_salvos:
                        for produto in produtos_salvos:
                            produto_des = vars(produto)
                            print(f'| {produto_des['nome']:}, preço: {produto_des['preco']}, codigo: {produto_des['codigo']}')
                        codigo_remover = pegar_int("Digite o codigo do produto que deseja remover: ")
                        prod_save = produtos_salvos
                        x = 0
                        for produto in produtos_salvos:
                            if vars(produto)['codigo'] == codigo_remover:
                                prod_save.remove(produto)
                                x = 1
                        produtos_salvos = prod_save 
                        salvar_prod()
                        if x == 0:
                            print('codigo não encontrado')
                            
                    else:
                        input('nenhum produto cadastrado')
                if opcaop == 3:
                    clear()
                    for produto in produtos_salvos:
                        produto_des = vars(produto)
                        print(f'| {produto_des['nome']:}, preço: {produto_des['preco']}, codigo: {produto_des['codigo']}')
                    print('| 1 - alterar preço individual\n', '| 2 - alterar preço de tudo', sep='')
                    opcao_alterar = opcao_menu('digite uma opção: ')
                    if opcao_alterar == 1:
                        porcentagem = pegar_porcentagem('digite a porcentagem que deseja alterar: ')
                        codigo_remover = pegar_int("Digite o codigo do produto que deseja alterar: ")
                        x = 0
                        for produto in produtos_salvos:
                            if vars(produto)['codigo'] == codigo_remover:
                                produto.preco *= porcentagem
                                x = 1
                        salvar_prod()
                        if x == 0:
                            print('codigo não encontrado')                         
                        
                    if opcao_alterar == 2:
                        porcentagem = pegar_porcentagem('digite a porcentagem que deseja alterar: ')
                        for produto in produtos_salvos:
                            produto.preco *= porcentagem 
                        salvar_prod()
                        
                            
                if opcaop == 4:
                    clear()
                    if produtos_salvos:
                        for produto in produtos_salvos:
                            produto_des = vars(produto)
                            print(f'| {produto_des['nome']:}, preço: {produto_des['preco']}, codigo: {produto_des['codigo']}')
                        input()
                    else:
                        input('nenhum produto cadastrado')
                elif opcaop == 5:
                    break
                
        
        if opcao1 == 2:         
            carrinho = Carrinho()
            carrinho.items = carrinho_salvo
            while opcao1 == 2:
                clear()
                if carrinho.items:
                    total = 0
                    for produto in carrinho.items:
                        total += produto['total_produto']
                        print(f'| {produto['nome']:}, preço: {produto['preco']}, quantia: {produto['quantia']}, total: {produto['total_produto']}')
                    print(f'TOTAL DO CARRINHO: ${total}\n')
                print('| 1 - adicionar item\n', '| 2 - remover item\n', '| 3 - zerar carrinho\n', '| 4 - finalizar compra\n', '| 5 - voltar ao menu', sep='')
                opcao2 = opcao_kart('Digite a sua opcao:')
                if opcao2 == 1:
                    clear()
                    if produtos_salvos:
                        for produto in produtos_salvos:
                            produto_des = vars(produto)
                            print(f'| {produto_des['nome']:}, preço: {produto_des['preco']}, codigo: {produto_des['codigo']}') 
                        codigo_remover = pegar_int("Digite o codigo do produto: ")
                        quantidade = pegar_int_positivo('Digite a quantidade: ')
                        x = 0
                        for produto in produtos_salvos:
                            if vars(produto)['codigo'] == codigo_remover:
                                carrinho.add(nome=produto.nome, preco=produto.preco, quantia=quantidade)
                                x = 1
                        if x == 0:
                            input('nenhum produto cadastrado para comprar')
                    else:
                        input('nenhum produto cadastrado para comprar')
                    salvar_kart()
                elif opcao2 == 2:
                    clear()
                    if carrinho.items:
                        indicec = 0
                        for produto in carrinho.items:
                            print(f'| indice: {indicec}, {produto['nome']:}, preço: {produto['preco']}, quantia: {produto['quantia']}, total: {produto['total_produto']}')
                            indicec += 1
                        indice = get_indice(indicec)
                        carrinho.items.pop(indice)
                    else:
                        input('sem items para remover')
                elif opcao2 == 3:
                    carrinho.items = []
                    salvar_kart()
                elif opcao2 == 4:
                    clear()
                    input(f"| VALOR A PAGAR: ${total}")
                    carrinho.items = []
                    salvar_kart()
                    
                elif opcao2 == 5:
                    break