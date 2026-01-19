print("===== MENU =====")
print("1 - Classificador de Idade")
print("2 - Calculadora de IMC")
print("3 - Conversor de Temperatura")
print("4 - Verificador de Ano Bissexto")

opcao = input("Escolha uma opção (1 a 4): ")

# 1 Classificador de Idade
if opcao == "1":
    idade = int(input("Digite sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Classificação: Criança")
    elif idade <= 17:
        print("Classificação: Adolescente")
    elif idade <= 59:
        print("Classificação: Adulto")
    elif idade >= 60:
        print("Classificação: Idoso")
    else:
        print("Idade inválida")

# 2 Calculadora de IMC
elif opcao == "2":
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"Seu IMC é {imc:.2f}")
    print(f"Classificação: {classificacao}")

# 3 Conversor de Temperatura
elif opcao == "3":
    temperatura = float(input("Digite a temperatura: "))
    origem = input("Unidade de origem (C, F ou K): ").upper()
    destino = input("Unidade de destino (C, F ou K): ").upper()

    if origem == "C" and destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif origem == "C" and destino == "K":
        resultado = temperatura + 273.15
    elif origem == "F" and destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif origem == "F" and destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
    elif origem == "K" and destino == "C":
        resultado = temperatura - 273.15
    elif origem == "K" and destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    elif origem == destino:
        resultado = temperatura
    else:
        print("Unidade inválida")
        exit()

    print(f"Temperatura convertida: {resultado:.2f} {destino}")

# 4  Verificador de Ano Bissexto
elif opcao == "4":
    ano = int(input("Digite um ano: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto")
    else:
        print(f"{ano} não é um ano bissexto")

# Opção inválida
else:
    print("Opção inválida. Escolha um número de 1 a 4.")
