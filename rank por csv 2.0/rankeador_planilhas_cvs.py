import os 
import csv
import random

clear = lambda: os.system('cls')
          
def get_valid_i(list_, message):
    erro = 'Indice invalido!'
    while True:
        try:
            len_ = len(list_)
            if len_ > 0:
                for i in range(len_):
                    print(i, list_[i])
                value = str(input(message))
                # clear()
                if float(value) in range(len_):
                    return int(value)
                raise Exception
            else:
                print('Sem arquivos csv na pasta /arquivos_csv!')
        except BaseException:
            clear()
            print(erro)  
            
def get_crt(list_, message):
    erro = 'Indice invalido!'
    while True:
        try:
            value = float(input(message))
            if value in range(len(list_) + 2):
                return int(value)
            raise Exception
        except BaseException:
            print(erro)  

csv_folder = os.path.join(os.path.dirname(__file__), 'arquivos_csv')

while True:
    clear()
    for root_, dirs_, files_ in os.walk(csv_folder):
       indice = get_valid_i(files_, 'Digite o indice do arquivo desejado: ')
       file_path = os.path.join(csv_folder, files_[indice])
       
    with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            full_data = [dict(zip(headers, rows)) for rows in reader]
    while True:
        clear()
        for i in full_data:
            print(i)
            
        print('\nCRITERIOS DE ORDEM:')
        for i in range(len(headers)):
            print(i, headers[i])
        print(f"{len(headers)} misturar\n\n{len(headers) + 1} escolher outro arquivo\n")
        criterio = get_crt(headers, 'Digite o indice da opcao:')
        
        if criterio in range(len(headers)):
            a = headers[criterio]
            reverse_ = False
            if a.lower() in ['pontuação', 'nota', 'desempenho']:
                reverse_ = True
            full_data = sorted(full_data, key=lambda x: x[a], reverse=reverse_)
            
        elif criterio == len(headers):
            full_data = random.sample(full_data, len(full_data))
            
        else:
            break
        
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(f=file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(full_data)
                      
        # input()
    