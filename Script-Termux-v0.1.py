#!/usr/bin/python3
import os
import time
import sys

# Subprocessos 
def executar_script(script, args=""):
    os.system(f"python3 {script} {args}")

# Comandos do sistema operacional.
def executar_comando(comando, args=""):
    os.system(f"{comando} {args}")

# Acesso inicial.
def acesso():
    senha = input("Senha: ")
    if senha != "123456":
        print("Acesso não liberado")
        exit()
    elif senha == "123456":
        print("Acesso liberado")
        time.sleep(3)
        os.system("clear")
    else:
        print("Senha inválida")

# Loading.
def imprimir_cabecalho():
    print("Olá FjrSon")
    time.sleep(1)
    print("LOADING...")
    time.sleep(2)
    os.system("clear")
    os.system("neofetch")
    time.sleep(2)
    os.system("clear")

# Banner + menu.
def exibir_menu():
    print('\033[0;37m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print("")
    print("\033[0;31m         ..............")
    print("               ..,;:ccc,.")
    print("             ......''';lxO.")
    print("   .....''''..........,:ld;")
    print("              .';;;:::;,,.x,")
    print("         ..'''.            0Xxoc:,.  ...")
    print("     ....                ,ONkc;,;cokOdc',.")           
    print("             .          OMo           ':ddo.")
    print("                     dMc               :OO;")
    print("                      0M. \033[0;37m  ➤ FjrSon\033[0;31m     .:o.")
    print("                     ;Wd")
    print("                        ;XO,")
    print("                         ,d0Odlc;,..")
    print("                              ..',;:cdOOd::,.")
    print("                                       .:d;.':;.")
    print("                                          'd,  .'")
    print("                                            ;l   ..")
    print("                                             .o")
    print("                                               c")
    print("                                               .")
    print("                                               .")
    print("")
    print("                    t3rmux n3thunt3r kal1 l1nux")
    print("")
    print('\033[0;37m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
# Menu de opções.
    print("1: \033[0;31m➤ \033[0;37m Update and Upgrade")
    print("2: \033[0;31m➤ \033[0;37m Nmap")
    print("3: \033[0;31m➤ \033[0;37m SQLmap")
    print("4: \033[0;31m➤ \033[0;37m Sherlock")
    print("5: \033[0;31m➤ \033[0;37m MrHolmes")
    print("6: \033[0;31m➤ \033[0;37m Checker CPF")
    print("7: \033[0;31m➤ \033[0;37m Scan Subdomínios")
    print("8: \033[0;31m➤ \033[0;37m Scan Hosts Proxys")
    print("9: \033[0;31m➤ \033[0;37m Executar Outro Script")
    print("10: \033[0;31m➤ \033[0;37m Sair")
    print("11: \033[0;31m➤ \033[0;37m Reiniciar Menu")

# Reset.
def reiniciar():
    print("Reiniciando o menu...")
    time.sleep(1)
    os.system("clear")
    imprimir_cabecalho()

# Função principal.
def main():
    acesso()
    imprimir_cabecalho()  
    escolha = False

# Prompt de comando.

    while not escolha:
        exibir_menu()
        nivel = int(input("PROMPT ➤ "))

#Menu em operações por niveis.

#Primeiro Nivel.
        if nivel == 1:
# Comando para sistema operacional.
           os.system("pkg update && pkg upgrade")

#Segundo Nivel.
        elif nivel == 2:
            while True:         
# Execução do NMAP ao sistema operacional.
                argumento = input("NMAP ")
# Sistema operacional limpando impresões.
                os.system("clear")
                # Executa o Nmap com o argumento fornecido
                os.system(f"nmap {argumento}")
                
                # Voltar ao menu ou continuar com Nmap
                voltar = input("'v' para voltar ao menu ou 'ENTER' para continuar com NMAP: ")
                if voltar.lower() == 'v':
                    break

        elif nivel == 3:
            while True:
                # Pergunta ao usuário qual argumento ele quer passar para o sqlmap.py
                argumento = input("SQLMAP ")
                os.system("clear")
                # Executa o sqlmap.py com o argumento fornecido
                executar_script("sqlmap.py", argumento)
                voltar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SQLMAP: ")
                if voltar.lower() == 'v':
                    break
       
        elif nivel == 4:
            while True:
                # Pergunta ao usuário qual nome de usuário deseja pesquisar com o Sherlock
                username = input("USERNAME?: ")
                
                # Executa o Sherlock com o nome de usuário fornecido
                os.system(f"cd $HOME/sherlock && ./sherlock {username}")
                
                # Voltar ao menu ou continuar com Sherlock
                voltar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SHERLOCK: ")
                if voltar.lower() == 'v':
                    break

        elif nivel == 5:
            while True:
                # Pergunta quais argumentos deseja passar para o MrHolmes
                argumento = input("'ENTER' para MR.HOLMES: ")

                # Muda para o diretório do Mr.Holmes e executa o script
                os.system("cd $HOME/Mr.Holmes && python3 MrHolmes.py " + argumento)

                # Opção para retornar ao menu inicial ou continuar usando MrHolmes
                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com MR.HOLMES: ")
                if continuar.lower() == 'v':
                    break

        elif nivel == 6:
            while True:
                # Executa o Checker CPF
                os.system("python3 checkerCPF.py")
                
                # Opção para retornar ao menu ou continuar com Checker CPF
                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com CHECKER CPF: ")
                if continuar.lower() == 'v':
                    break

        elif nivel == 7:
            while True:
                # Executa o Scan Subdomínios
                os.system("python3 subf.py")

                # Opção para retornar ao menu ou continuar com Scan Subdomínios
                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SCAN SUBDOMÍNIOS: ")
                if continuar.lower() == 'v':
                    break

        elif nivel == 8:
            while True:
                # Executa o Scan Hosts Proxys
                os.system("python3 scanfast.py")

                # Opção para retornar ao menu ou continuar com Scan Hosts Proxys
                continuar = input("'v' para retornar ao menu ou 'ENTER' para continuar com SCAN HOSTS PROXYS: ")
                if continuar.lower() == 'v':
                    break

        elif nivel == 9:
            while True:
                script = input("Scripts.py: ")
                if script.lower() == 'sair':
                    break
                if os.path.isfile(script):
                    print(f"Executando {script}...")
                    executar_script(script)
                    input("Pressione Enter para voltar ao menu...")
                else:
                    print("Script nao esta na pasta ou nao existe!")

        elif nivel == 10:
            print("Saindo do Script...")
            escolha = True

        elif nivel == 11:
            reiniciar()

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()

