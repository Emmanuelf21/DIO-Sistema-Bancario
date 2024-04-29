
saldo = 1300
limite = 500

extrato = ""
depositos = ""
saques = ""

numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input("Escolha a opção: \n[d] Depositar \n[s] Sacar \n[e] Extrato \n[q] Sair\n:")
    print("-----------------------------------\n")#quebrar linha
    if opcao.lower() == "d":
        valor = float(input("Informe o valor para o Depósito: "))
        
        if valor > 0:
            saldo += valor
            depositos+= f" R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
            
        else:
            print("O valor informado é inválido!")
        
    elif opcao.lower() == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques>=LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente!")
            
        elif excedeu_saques:
            print("Limite de Saques diários atingido!")
        
        elif excedeu_limite:
            print("O valor para saque excedeu o limite de R$ 500.00")
        
        elif valor > 0: 
            saldo -= valor
            numero_saques+=1
            saques+= f" R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
            
        else:
            print("O valor informado é inválido!")

    elif opcao.lower() == "e":
        
        if depositos:
            extrato+= f"Depósitos:\n{depositos}\n"
        if saques:
            extrato+= f"Saques:\n{saques}\n"
        print("---------------- EXTRATO ----------------\n")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
            
    elif opcao.lower() == "q":
        break
    
    print("-----------------------------------\n") #quebrar linha       
        
        