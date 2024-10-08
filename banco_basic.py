menu = """\n
    ╔═══════════════════════════════════╗
    ║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ MENU ▒▒▒▒▒▒▒▒▒▒▒▒▒▒║
    ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
    ║   [d]\tDepositar               ║
    ║   [s]\tSacar                   ║
    ║   [e]\tExtrato                 ║
    ║   [q]\tSair                    ║
    ╚═══════════════════════════════════╝
    =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"  Depósito:\t\tR$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"  Saque:\t\t(R$ {valor:.2f})\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\nOperação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("╔═══════════════════════════════════╗")
        print("║▒▒▒▒▒▒▒▒▒▒▒▒▒ EXTRATO ▒▒▒▒▒▒▒▒▒▒▒▒▒║\n")
        print("\n Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n  Saldo:\t\tR$ {saldo:.2f}\n")
        print("║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║")
        print("╚═══════════════════════════════════╝")
    
    elif opcao == "q":
        print("SAINDO ...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")