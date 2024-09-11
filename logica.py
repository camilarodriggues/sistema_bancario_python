menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Inicializar variáveis
saldo = 0
limite_saque = 500
historico_extrato = []
max_saques = 3
saques_realizados = 0

def realizar_deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        historico_extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso.")
    else:
        print("Erro: Valor de depósito inválido.")

def realizar_saque(valor):
    global saldo, saques_realizados
    if valor > saldo:
        print("Erro: Saldo insuficiente para o saque.")
    elif valor > limite_saque:
        print("Erro: O valor do saque excede o limite permitido.")
    elif saques_realizados >= max_saques:
        print("Erro: Limite de saques diários alcançado.")
    elif valor > 0:
        saldo -= valor
        historico_extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Erro: Valor de saque inválido.")

def mostrar_extrato():
    print("\n--- Extrato Bancário ---")
    if not historico_extrato:
        print("Nenhuma transação realizada.")
    else:
        for linha in historico_extrato:
            print(linha)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("------------------------")

# Loop principal do programa
while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        realizar_deposito(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))
        realizar_saque(valor)

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")
