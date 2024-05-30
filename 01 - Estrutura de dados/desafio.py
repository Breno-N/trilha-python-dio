def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def visualizar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_cliente(*, nome, data_nascimento, cpf, endereco):
    novo_cliente = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco }
    
    global clientes
    tem_na_lista = False
    for cliente in clientes:
        if cliente["cpf"] == novo_cliente["cpf"]:
            tem_na_lista = True
            break
    
    if tem_na_lista:
        print("\nErro ao criar novo cliente, CPF já cadastrado.")
        return
    else:
        print("\n================ NOVO CLIENTE ================")
        print("Novo cliente criado.")
        print(f"\nNome: {novo_cliente["nome"]}")
        print(f"\nNascimento: {novo_cliente["data_nascimento"]}")
        print(f"\nCPF: {novo_cliente["cpf"]:.0f}")
        print(f"\nEndereço: {novo_cliente["endereco"]}")
        print("==========================================")
        return novo_cliente


def criar_conta_corrente(cpf):
    global clientes
    cliente_consultado = {}
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente_consultado = cliente
            break
    
    if not bool(cliente_consultado):
        print("\nCPF inexistente não é possivel prosseguir com o cadastro da conta")
        return

    global contas
    agencia = "0001"
    numero_conta = len(contas) + 1
    nova_conta_cliente = {"cliente": cliente_consultado, "conta": numero_conta, "agencia": agencia}
    
    return nova_conta_cliente


def visualizar_clientes():
    print("\n================ Dados dos Clientes ================")
    if len(clientes) > 0 :
        for cliente in clientes:
            print(f"\nCliente: {cliente}")
    else:
        print("Sem clientes cadastrados")
    print("=======================================================")


def visualizar_contas():
    print("\n================ Dados das Contas de Clientes ================")
    if len(contas) > 0 :
        for conta in contas:
            print(f"\nConta: {conta}")
    else:
        print("Sem contas cadastradas")
    print("=======================================================")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Novo Cliente
[cc] Conta Corrente
[vc] Visualizar Clientes
[vcc] Visualizar Contas de Clientes
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        (saldo, extrato) = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        (saldo, extrato, numero_saques) = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        visualizar_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a data de nascimento: ")
        cpf = int(input("Informe o valor do cpf: "))
        endereco = input("Informe o endereço: ")

        novo_cliente = criar_cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        if novo_cliente:
            clientes.append(novo_cliente)

    elif opcao == "cc":
        cpf = int(input("Informe o valor do cpf: "))
        
        nova_conta_cliente = criar_conta_corrente(cpf=cpf)
        if nova_conta_cliente:
            contas.append(nova_conta_cliente)
            print("\n================ NOVA CONTA CORRENTE ================")
            print("Nova conta corrente criada.")
            print(f"\nCliente: {nova_conta_cliente["cliente"]}")
            print(f"\nConta: {nova_conta_cliente["conta"]}")
            print(f"\nAgência: {nova_conta_cliente["agencia"]}")
            print("==========================================")

    elif opcao == "vc":
        visualizar_clientes()

    elif opcao == "vcc":
        visualizar_contas()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")