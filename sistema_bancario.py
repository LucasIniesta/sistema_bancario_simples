menu = """

==================

    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair

==================

Digite a opção desejada: """

saldo = 0.00
limite_saque = 500
extrato = f"""
===== Extrato =====

"""
LIMITE_DE_SAQUES = 3
numero_de_saques_realizados = 0
numero_de_depositos_realizados = 0

while True:

    opcao = input(menu)

    if opcao == "0":
        
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito <= 0:

            print("Valor de depósito inválido. Seu depósito precisa ser maior do que R$ 0.01")
        
        print("Depósito realizado com sucesso!")
        numero_de_depositos_realizados += 1
        saldo += valor_deposito
        extrato += f"Depósito de: R$ {valor_deposito:.2f} \n"
        
    elif opcao == "1":

        if numero_de_saques_realizados == LIMITE_DE_SAQUES:

            print('Você já atingiu o seu limite diário de saques. Você poderá realizar novos saques amanhã!')
        
        else:

            valor_saque = float(input("Digite o valor que deseja sacar: "))

            if valor_saque > limite_saque:

                print("Operação não permitida! Seu limite por saque é de: R$ 500,00")

            else:

                if valor_saque > saldo:
                    
                    print('Saldo insuficiente!')

                else:

                    print("Saque realizado com sucesso!")

                    numero_de_saques_realizados += 1
                    saldo -= valor_saque
                    extrato += f"Saque de: R$ {valor_saque:.2f} \n"    
        

    elif opcao == "2":

        if numero_de_depositos_realizados == 0 and numero_de_saques_realizados == 0:

            print(
f"""
{extrato}
Não foram realizadas movimentações

==================

Saldo: R$ {saldo:.2f}

======= Fim ======

""")
        else:

            print(
f"""
{extrato}

==================

Saldo: R$ {saldo:.2f}

======= Fim ======

""")

    elif opcao == "3":
        print("Obrigado por utilizar o nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")
