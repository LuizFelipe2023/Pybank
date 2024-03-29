import os

LIMITE_SAQUES = 3
VALOR_MAXIMO = 500

saldo = 0
saques_feitos = 0

def deposito(saldo):
    valor_deposito = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    return saldo

def saque(saldo, saques_feitos):
    if saques_feitos >= LIMITE_SAQUES:
        print("Você atingiu o limite de saques.")
        return saldo, saques_feitos
    else:
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > VALOR_MAXIMO or valor_saque > saldo:
            print("Valor de saque inválido.")
            return saldo, saques_feitos
        else:
            saldo -= valor_saque
            saques_feitos += 1
            print("Saque de", valor_saque, "realizado com sucesso.")
            return saldo, saques_feitos

def extrato(saldo, saques_feitos):
    print("Saldo atual:", saldo)
    print("Saques feitos:", saques_feitos)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Bem-vindo ao Pybank")
print("Essas são as opções disponíveis para realizar em nosso sistema:")
print("1-Depósito, 2-Saque, 3-Extrato")
while True:
    op = int(input("Digite a operação que deseja fazer (0 para sair): "))
    limpar_tela()
    
    if op == 0:
        break
    elif op == 1:
        saldo = deposito(saldo)
    elif op == 2:
        saldo, saques_feitos = saque(saldo, saques_feitos)
    elif op == 3:
        extrato(saldo, saques_feitos)
    else:
        print("Opção inválida.")

    input("Pressione Enter para continuar...")
    limpar_tela()
    print("Bem-vindo ao Pybank")
    print("Essas são as opções disponíveis para realizar em nosso sistema:")
    print("1-Depósito, 2-Saque, 3-Extrato")

print("Obrigado por usar o Pybank. Volte sempre!")
