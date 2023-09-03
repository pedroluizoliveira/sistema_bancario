
def menu():
    AGENCIA = "0001"
    NUMERO_SAQUES = 3
    LIMITE_SAQUE = float(500)
    saldo = float(0)
    saques_no_mes = 0
    extrato = ""
    usuarios = []
    contas = []

    exibir_menu = """

Bem vindo ao Banco PLP!
Insira o número corresponde à operação desejada:

1 - Depósito
2 - Saque
3 - Extrato
4 - Criar conta
5 - Cadastrar usuário
6 - Sair

"""

    while True:
        opcao = input(exibir_menu)

        if opcao == "1":
            deposito = float(input("\nQuanto você gostaria de depositar?\n"))
            saldo, extrato = func_deposito(saldo, deposito, extrato)
            
        elif opcao == "2":
            saldo, extrato, saques_no_mes = func_saque(
                saldo=saldo,
                extrato=extrato,
                LIMITE_SAQUE=LIMITE_SAQUE,
                NUMERO_SAQUES=NUMERO_SAQUES,
                saques_no_mes=saques_no_mes
            )

        elif opcao == "3":
            saldo, extrato = func_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) +1
            conta = func_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            func_usuario(usuarios)

        elif opcao == "6": 
            print("\nObrigado por utilizar nossos serviços!\n")
            break

        else:
            print("\nOperação inválida.\n")

        confirmacao = input("Gostaria de fazer mais alguma operação?\nDigite s para sim e n para não\n")
        if confirmacao == "n":
            print("\nObrigado por utilizar nossos serviços!\n")
            break
        elif confirmacao == "s":
            continue
        else:
            print("\nResposta inválida. Retornando ao menu principal.")

def func_deposito(saldo, deposito, extrato, /):
    while True:
        if deposito > 0:
            confirmacao = input(f"\nDeseja depositar R$ {deposito:.2f}?\nDigite s para sim e n para não\n")
            if confirmacao == "s":
                saldo += deposito
                GREEN = "\033[92m"
                RESET = "\033[0;0m"
                extrato += (GREEN + f"Depósito realizado: R$ {deposito:.2f}\n" + RESET)
                print("\nDepósito realizado com sucesso!\n")
                break
            elif confirmacao == "n":
                print("\n")
                break
            else:
                print("Resposta inválida!")
                break
        else:
            print("\nValor inválido!\n")
            break
    return saldo, extrato

def func_saque(*, saldo, extrato, LIMITE_SAQUE, NUMERO_SAQUES, saques_no_mes):
    RED = "\033[1;31m"
    RESET = "\033[0;0m"
    if NUMERO_SAQUES == saques_no_mes:
        print("\nVocê já atingiu seu limites de saque do mês\n")
    else:
        while True:
            saque = float(input("\nQuanto você gostaria de sacar?\n"))
            if saque <= LIMITE_SAQUE and saque <= saldo and saque > 0:
                confirmacao = input(f"\nDeseja sacar R$ {saque:.2f}??\nDigite s para sim e n para não\n")
                if confirmacao == "s":
                    saldo -= saque
                    extrato += (RED + f"Saque realizado: R$ {saque:.2f}\n" + RESET)
                    print("\nOperação realizada com sucesso!\n")
                    saques_no_mes += 1
                    break
                elif confirmacao == "n":
                    break
                else:
                    print("\nResposta inválida!\n")
                    break
            elif saque > LIMITE_SAQUE:
                print(f"\nSeu limite de saque por operação é de R$ {LIMITE_SAQUE:.2f}\n")
                break
            elif saque > saldo:
                print(f"Seu saldo atual é de R$ {saldo:.2f}. Por favor, insira um valor dentro deste intervalo.\n")
            else:
                print("\nValor inválido!\n")
                break
    return saldo, extrato, saques_no_mes

def func_extrato(saldo, /, *, extrato):
    while True:
        if extrato == "":
            print("\nNão foram realizadas operações recentemente")
            print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
            break
        else:
            print("\nSeu extrato no período solicitado está descrito abaixo:\n")
            print(extrato)
            print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
            break
    return saldo, extrato

def func_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário:\n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"Agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, criação de conta encerrada!\n")

def func_usuario(usuarios):
    
    cpf = input("\nPara iniciarmos, informe os 11 digitos do seu CPF:\n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Você já está cadastrado em nosso banco!\n")
        return
    
    nome = input("\nInforme o nome completo, sem abreviações:\n")
    data_nascimento = input("\nInforme a sua data de nascimento no formato - dd-mm-aaaa:\n")  
    endereco = input("\nInforme seu endereço no formato - rua, número, complemento (se houver), bairro, cidade, sigla do estado:\n") 

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "encereco": endereco}) 

    print("\nUsuário criado com sucesso, seja bem vindo!\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


menu()
