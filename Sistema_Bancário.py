cont = 0
extrato_saque = []
deposito = []

while True:
    print(f"{'-=' * 5} Banco da JK {'-=' * 5}")
    print("Por favor, digite a opção que deseja realizar")
    print('-=' * 25)
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print('-=' * 25)
    resp = int(input("Opção: "))
    while resp > 3 or resp < 1:
        print('Opção inválida!')
        resp = int(input("Digite um número entre 1 e 3: "))

    if resp == 1:
        valor = float(input("Valor do depósito: "))
        while valor < 0.1:
            valor = float(input("Valor digitado incorreto, digite um valor correto: "))

        deposito.append(valor)

    saldo = sum(deposito) - sum(extrato_saque)

    if resp == 2:
        if saldo == 0:
            print("Saldo insuficiente, não é possível realizar essa operação.")
        else:
            if cont > 2:
                print("Você já atingiu o limite diário de saque.")

            else:
                while True:
                    saque = float(input("Digite o valor que deseja sacar: R$ "))
                    if saque > 500 or saque < 0.1:
                        print("Valor não permitido para saque")
                        if saque > 500:
                            print("O valor máximo é de R$ 500,00")
                    else:
                        break

                if saque <= saldo:
                    extrato_saque.append(saque)
                    print(f"Você sacou R${saque:.2f}")
                    cont += 1

                elif saque > saldo:
                    print("Saldo insuficiente")


    if resp == 3:
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
        print(f"Você realizou {cont} saques")
        if len(extrato_saque) > 0:
            print("Histórico de saque: ")
            for c in range(len(extrato_saque)):
                print(f"O {c+1}º saque foi de R$ {extrato_saque[c]:.2f}")

    continuar = str(input("Deseja continuar? [S/N]")).upper()

    while continuar not in 'NS':
        continuar = str(input("Digite apenas S ou N: ")).upper()

    if continuar == 'N':
        break
