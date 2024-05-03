import textwrap

def menu():
        menu = """\n
        ========================= MENU =========================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Contas
        [nu]\tNovo usuário
        [q]\tSair
        ==>""" 
        return input(textwrap.dedent(menu))
    
def main():
    saldo = 0
    limite = 500
    numero_saques = 0
    depositos = ""
    saques = ""
    extrato = ""
    usuarios =[]
    contas =[]
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    while True:
        opcao = menu()
       
        if opcao.lower() == "d":
            valor = float(input("Informe o valor para o Depósito: "))
            saldo, depositos = depositar(saldo, valor, depositos)#passagem por keyword
            
        elif opcao.lower() == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, saques, numero_saques = sacar(
                                valor=valor,
                                saldo=saldo,
                                saques=saques,
                                numero_saques=numero_saques,
                                limite=limite,
                                LIMITE_SAQUES=LIMITE_SAQUES
                            )#passagem por keyword
            
        elif opcao.lower() == "e":
            exibir_extrato(saldo, depositos, saques, extrato=extrato)
        
        elif opcao.lower() == "nu":
            criar_usuario(usuarios)  
            
        elif opcao.lower() == "lc":
            listar_contas(contas)  
            
        elif opcao.lower() == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao.lower() == "q":
            break       

def depositar(saldo, valor, depositos):
    if valor > 0:
        saldo += valor
        depositos+= f"\t\tR$ {valor:.2f}\n"
        print("--- Depósito realizado com sucesso! ---")
            
    else:
        print("@ Operação falhou! O valor informado é inválido. @")
        
    return saldo, depositos

def sacar(valor, saldo, saques, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
        
    excedeu_limite = valor > limite
        
    excedeu_saques = numero_saques>=LIMITE_SAQUES
        
    if excedeu_saldo:
        print("@ Saldo insuficiente! @")
            
    elif excedeu_saques:
        print("@ Limite de Saques diários atingido! @")
        
    elif excedeu_limite:
        print("@ O valor para saque excedeu o limite de R$ 500.00 @")
        
    elif valor > 0: 
        saldo -= valor
        numero_saques+=1
        saques += f"\t\tR$ {valor:.2f}\n"
        print("--- Saque realizado com sucesso! ---")
            
    else:
        print("@ O valor informado é inválido! @")
    return saldo, saques, numero_saques

def exibir_extrato(saldo, depositos, saques, /, *, extrato):
    if depositos:
        extrato+= f"Depósitos:\n{depositos}\n"
    if saques:
        extrato+= f"Saques:\n{saques}\n"
    print("========================= MENU =========================\n")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@ Ja´existe usuário com esse CPF! @")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairo - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    
    print("--- Usuário criado com sucesso! ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    print(numero_conta)
    if usuario:#se usuário existir, a conta será criada
        print("\n--- Conta criada com sucesso! ---")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario":usuario}
    
    print("\n@ Usuário não encontrado, fluxo de criação de conta encerrado! @")
    #retorna None caso usuário não exista
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\t
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*1000)
        print(textwrap.dedent(linha))
    
main()
        