menu = f"""
================ MENU ================
[d] Depositar
[s] Sacar (Limite por saque: R$ 500,00)
[e] Extrato
[q] Sair
======================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

historico_depositos = []
historico_saques = []

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            historico_depositos.append(valor)
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")

        elif excedeu_saques:
            print("Operação falhou! Limite de saques diários atingido (3 por dia).")

        elif valor > 0:
            saldo -= valor
            historico_saques.append(valor)
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")

        if not historico_depositos and not historico_saques:
            print("Sem movimentações.")
        else:
            if historico_depositos:
                print("\n--- Depósitos ---")
                for deposito in historico_depositos:
                    print(f"R$ {deposito:.2f}")

            if historico_saques:
                print("\n--- Saques ---")
                for saque in historico_saques:
                    print(f"R$ {saque:.2f}")

        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        print("Obrigado por usar o nosso sistema bancário. Até mais!")
        break

    else:
        print("Opção inválida! Escolha uma opção do menu.")
