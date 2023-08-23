menu = """
1 - Deposito
2 - Saque
3 - Extrato
4 - Sair

"""

menu_confirmacao = "Digite s para sim e n para não\n"
saldo = float(1000)
NUMERO_SAQUES = 3
LIMITE_SAQUE = float(500)
saques_no_mes = 0
extrato = ""
GREEN = "\033[92m"
RED = "\033[1;31m"
RESET = "\033[0;0m"

while True:
    print("\nBem vindo ao Banco PLP:\n")
    opcao = input(menu)

    if opcao == "1":
        while True:
            deposito = float(input("\nQuanto você gostaria de depositar?\n"))
            if deposito > 0:
                print(f"\nDeseja depositar R$ {deposito:.2f}?")
                confirmacao = input(menu_confirmacao)
                if confirmacao == "s":
                    saldo += deposito
                    extrato += (GREEN + f"Depósito realizado: R$ {deposito:.2f}\n" + RESET)
                    print(f"\nSeu novo saldo é de R$ {saldo:.2f}\n")
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
        
    elif opcao == "2":
        if NUMERO_SAQUES == saques_no_mes:
            print("\nVocê já atingiu seu limites de saque do mês\n")
        else:
            while True:
                saque = float(input("\nQuanto você gostaria de sacar?\n"))
                if saque <= LIMITE_SAQUE and saque <= saldo and saque > 0:
                    print(f"\nDeseja sacar R$ {saque:.2f}?")
                    confirmacao = input(menu_confirmacao)
                    if confirmacao == "s":
                        saldo -= saque
                        extrato += (RED + f"Saque realizado: R$ {saque:.2f}\n" + RESET)
                        print(f"\nSeu novo saldo é de R$ {saldo:.2f}\n")
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

    elif opcao == "3":
        while True:
            if extrato == "":
                print("\nNão foram realizadas operações recentemente")
                print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
                break
            else:
                print("\nSeu extrato no período solicitado está descrito abaixo:")
                print(extrato)
                print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
                break

    elif opcao == "4": 
        print("\nObrigado por utilizar nossos serviços!\n")
        break

    else:
        print("\nOperação inválida.\n")

    print("Gostaria de fazer mais alguma operação?")
    confirmacao = input(menu_confirmacao)
    if confirmacao == "n":
        print("\nObrigado por utilizar nossos serviços!\n")
        break
    elif confirmacao == "s":
        continue
    else:
        print("\nResposta inválida. Retornando ao menu principal.")