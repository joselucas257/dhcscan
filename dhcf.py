import os
import time
import socket
os.system ("clear")
while True:
    password = input("digite sua senha:")
    
    if password == "dhcteam":
        print ('\033[32m'+'senha correta!'+'\033[0;0m')
        break
    else:
        print ('\033[31m'+'senha incorreta'+'\033[0;0m')
        print ('\033[42m'+'\033[1m'+'\033[33m'+'digita essa merda direito krlh pqp!!!'+'\033[0;0m')
os.system ("clear")
print ("")
print ("")
print ("")
print ("")
print ('\033[32m'+'________________________'+'\033[0;0m')
print ('\033[32m'+'|[!]instalando recursos|'+'\033[0;0m')
print ('\033[32m'+'|______________________|'+'\033[0;0m')
os.system ("apt update && apt upgrade && apt install python2")

os.system ("clear")

print ('\033[32m'+'########      ##     ##      ###### '+'\033[0;0m')
print ('\033[32m'+'##     ##     ##     ##     ##    ##'+'\033[0;0m')
print ('\033[32m'+'##     ##     ##     ##     ##      '+'\033[0;0m')
print ('\033[32m'+'##     ##     #########     ##      '+'\033[0;0m')
print ('\033[32m'+'##     ##     ##     ##     ##      '+'\033[0;0m')
print ('\033[32m'+'##     ## ### ##     ## ### ##    ##'+'\033[0;0m')
print ('\033[32m'+'#######   ### ##     ## ###  ###### '+'\033[0;0m')

time.sleep (4)


print ("")
print ("")
print ("")
print ("__________________________________")
time.sleep (0.2)
print ("|   autor: professor             |")
time.sleep (0.2)
print ("|   team: D.H.C team             |")
time.sleep (0.2)
print ("|   github: joselucas257         |")
time.sleep (0.2)
print ("|   youtube: dhcteam             |")
time.sleep (0.2)
print ("|________________________________|")
print ("")
print ("")
print ("")
input("de enter pra continuar ou Crtl+c pra sair: ")
os.system ("clear")
print ("")
print ("")
print ("")
print ("")
print ("")
print ('\033[32m'+'______________________________'+'\033[0;0m')
time.sleep (0.2)
print ('\033[32m'+'|       ferramentas:         |'+'\033[0;0m')
time.sleep (0.2)
print ('\033[32m'+'|    [1] dos attack [!]      |'+'\033[0;0m')
time.sleep (0.2)
print ('\033[32m'+'|    [2]brute force [!]      |'+'\033[0;0m')
time.sleep (0.2)
print ('\033[32m'+'|    [3]  phishing  [!]      |'+'\033[0;0m')
print ('\033[32m'+'|    [4] scan porta [!]      |'+'\033[0;0m')
print ('\033[32m'+'|    [5]  exploits  [!]      |'+'\033[0;0m')
time.sleep (0.2)
print ('\033[32m'+'|____________________________|'+'\033[0;0m')
while True:
    opcao = int(input('digite a opção desejada:  ' ))
    if opcao == 1:
        os.system("clear")
        print("instalando o dos attack...")
        os.system("apt update && apt upgrade")
        os.system("apt install git,python,python2")
        os.system("git clone https://github.com/joselucas257/D.H.C-DDos")
        os.system("mv D.H.C-DDos /$HOME/")
        print("ágora de Ctrl+C para voltar pra home, e de o comando [cd D.H.C-DDos] para abrir o script")
    elif opcao == 2:
        print("brute force")
    elif opcao == 3:
        print ("phishing")
    elif opcao == 4:
        print("BAIXANDO RECURSOS, AGUARDE!...")
        time.sleep(2)
        os.system("apt update && apt upgrade")
        os.system("apt install wget")
        os.system("wget https://www.mediafire.com/file/e7ey9lbc2xbxvoq/dhcscan.py/file")
        time.sleep(2)
        os.system("mv dhcscan.py /$HOME/")
        print('\033[42;1;33m'+'agora de Ctrl+C e de o comando cd para voltar para a home e de o comando python3 dhcscan.py (e o ip do alvo)'+'\033[0;0m')
    elif opcao == 5:
        print("exploits")