from datetime import date

# 1 - Função para calcular gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)


# 2 - Função para verificar palíndromo
def eh_palindromo(texto):
    texto_limpo = ""

    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere.lower()

    return texto_limpo == texto_limpo[::-1]


# 3 - Função para calcular preço com desconto
def calcular_preco_com_desconto(preco, desconto_percentual):
    valor_desconto = preco * (desconto_percentual / 100)
    preco_final = preco - valor_desconto
    return round(preco_final, 2)


# 4 - Função para calcular dias de vida
def calcular_dias_vivos(ano, mes, dia):
    data_nascimento = date(ano, mes, dia)
    data_atual = date.today()
    return (data_atual - data_nascimento).days


# MENU PRINCIPAL
print("===== MENU =====")
print("1 - Calcular gorjeta")
print("2 - Verificar palíndromo")
print("3 - Calcular preço com desconto")
print("4 - Calcular dias de vida")

opcao = input("Escolha uma opção (1 a 4): ")

# OPÇÃO 1
if opcao == "1":
    valor = float(input("Digite o valor da conta: "))
    porcentagem = float(input("Digite a porcentagem da gorjeta: "))
    gorjeta = calcular_gorjeta(valor, porcentagem)
    print("Valor da gorjeta:", gorjeta)

# OPÇÃO 2
elif opcao == "2":
    texto = input("Digite uma palavra ou frase: ")

    if eh_palindromo(texto):
        print("Sim")
    else:
        print("Não")

# OPÇÃO 3
elif opcao == "3":
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o percentual de desconto: "))
    preco_final = calcular_preco_com_desconto(preco, desconto)
    print("Preço final com desconto: R$", preco_final)

# OPÇÃO 4
elif opcao == "4":
    ano = int(input("Digite o ano de nascimento: "))
    mes = int(input("Digite o mês de nascimento: "))
    dia = int(input("Digite o dia de nascimento: "))

    dias = calcular_dias_vivos(ano, mes, dia)
    print("Quantidade de dias vividos:", dias)

else:
    print("Opção inválida")
