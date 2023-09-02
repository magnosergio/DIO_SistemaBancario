MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = input(MENU)
    if opcao == "d":
        print("Depositar")
    elif opcao == "s":
        print("Sacar")
    elif opcao == "e":
        print("Extrato")
    elif opcao == "q":
        print("Sair")
    else:
        print("Opção inválida, por favor selecione uma opção válida.")
