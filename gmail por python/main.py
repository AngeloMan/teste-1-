import os 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from modulo import*
import json
from datetime import datetime

html = os.path.join(os.path.dirname(__file__), "texto_html.html")
arquivo_json = os.path.join(os.path.dirname(__file__), "historico_emails.json")

if __name__ == "__main__":
    try:
        with open(arquivo_json, "r") as file:
            historico_emails = json.load(file)
    except BaseException:
        historico_emails = []    
        
    logado = False
    while True:
        # menu principal 
        # datetime.now().strftime("%d/%m/%Y %H:%M")
        print("|            login")
        gmail = get_gmail("| gmail: ")
        if not gmail:
            continue
        senha = str(input("| senha de app: "))
        len_maior = int(max(len(gmail), len(senha))/2) + 2
        print('-'*len_maior,'logando','-'*len_maior, sep="")
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.ehlo()
                server.starttls()
                server.login(gmail, senha)
                logado = True
        except BaseException:
            clear()
            print('gmail ou senha invalidos!')
        while logado:
            clear()
            print('| 1 - enviar email\n', '| 2 - ver historico de emails\n', '| 3 - deslogar', sep='')
            opcao = opcao_menu(3, "Opçäo: ")
            if opcao == 1:
                destinatario = get_gmail("Destinatario: ")
                assunto = str(input("Assunto: "))
                corpo = str(input("Corpo (use <br> para quebra de linha): "))
                with open(html, "w") as file:
                    file.write(base_html)
                    file.write("    ")
                    file.write(corpo)
                    file.write("\n</body>")
                    file.write("\n</html>")
                with open(html, "r") as file:
                    texto = file.read()
                
                mimemultipart = MIMEMultipart()
                mimemultipart['from'] = gmail
                mimemultipart['to'] = destinatario
                mimemultipart['subject'] = assunto
                mimemultipart.attach(MIMEText(texto, "html", "utf-8"))
                print("Conectando ao servidor...")
                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.ehlo()
                        server.starttls()
                        server.login(gmail, senha)
                        print("Conectado")
                        server.send_message(mimemultipart)
                        clear()
                        historico_emails.append(dict(zip(['remetente',"destinatario","assunto", "data"], [gmail, destinatario, assunto, datetime.now().strftime("%d/%m/%Y %H:%M")])))
                        with open(arquivo_json, "w") as file:
                            json.dump(historico_emails, file, indent=2, ensure_ascii=False)
                        input("Enviado!")                  
                                               
                except BaseException as e:
                    clear()
                    input(f"Erro ao enviar o email! {e}")
                    
            if opcao == 2:
                clear()
                if historico_emails:
                    for i in reversed(historico_emails):
                        print(f"Remetente: {i['remetente']}\nDestinatario: {i['destinatario']}\nAssunto: {i['assunto']}\nData: {i['data']}\n")
                else:
                    print("Historico vazio!")
                input()
            if opcao == 3:
                break
            clear()
            continue
