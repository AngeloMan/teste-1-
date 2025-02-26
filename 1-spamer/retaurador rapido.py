import os

n = 200 # números de arquivos a ser criados
ar_nome = 'KKKKK.txt'

dir_p = os.path.dirname(__file__)
while True:
    try:
        if (os.path.dirname(dir_p)) != dir_p:
            penultimo = dir_p
            dir_p = os.path.dirname(dir_p)
            print(dir_p)
            continue
        else:
            raise Exception
        
    except BaseException:
        dir_p = penultimo #pra deixar mais de boa senão ferra o pc inteiro
        print('limite f', dir_p)
        break
# dir_p = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
for i in range(n):
    nome = str(i) + ar_nome
    arqui = os.path.join(dir_p, nome)
    os.remove(arqui)

for dir_, b, *c in os.walk(dir_p):
    print(dir_, b)
    for i in b:
        final_dir = os.path.join(dir_, i)
        for i in range(n):
            nome = str(i) + ar_nome
            arqui = os.path.join(final_dir, nome)
            os.remove(arqui)
        print(f'{final_dir}\n')

        a = os.walk(final_dir)
        for i in a:
            for j in i:
                if type(j) == list:
                    for k in j:
                        # print('123')
                        print("   deletando",final_dir,k)
                else:
                    print(j)