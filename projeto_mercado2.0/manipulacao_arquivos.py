import os
import json

path_ = os.path.dirname(__file__)
file_kart = os.path.join(path_ ,'data/carrinho_salvo.json')
file_prod = os.path.join(path_ ,'data/produtos_salvos.json')
file_code = os.path.join(path_ ,'data/codigo_seguite.json')

try: 
    with open(file_kart, 'r') as file:
        carrinho_salvo = json.load(file)
except BaseException:
    carrinho_salvo = []
        
try: 
    with open(file_prod, 'r') as file:
        produtos_covertido = json.load(file)
except BaseException:
    produtos_covertido = []
    
try: 
    with open(file_prod, 'r') as file:
        code = json.load(file)
except BaseException:
    produtos_covertido = []
    
try: 
    with open(file_code, 'r') as file:
        code = json.load(file)
except BaseException:
    code = 1000
    
