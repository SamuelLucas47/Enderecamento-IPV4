#Código escrito em python para descobrir o endereço IPV4 de um site.
import socket

resp="S"
while(resp=="S"):
    url=input("Digite uma URL: ")
    ip=socket.gethostbyname(url)
    print("O IP referente a url informada é: ", ip)
    resp=input("Digite <s> para continuar: ").upper()
