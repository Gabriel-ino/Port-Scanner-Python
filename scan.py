import nmap


scanner = nmap.PortScanner()

print("Bem-vindo ao Scanner")
print("*--------------------------------------*")

ip = input("Digite o ip a ser varrido: ")
print ("O ip digitado foi ", ip)
type(ip)

menu = input("""\nEscolha o tipo de varredura:
                1-> Varredura SYN
                2_> Varredura UDP
                3-> Varredura Intensa~
                Digite a opção requisitada: """)



if menu == "1":
    print("Versão Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

elif menu == "2":
    print("Versão Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())

elif menu == "3":
    print("Versão Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print("Status do IP: ", scanner[ip].state)
    print (scanner[ip].all_protocols())
    print("")
    print("Portas Abertas ", scanner[ip]['tcp'].keys())

else:
    print("Selecione uma opção válida!")
    
    





