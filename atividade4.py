print("===== MENU =====")
print("1 - Calculadora Básica")
print("2 - Média de Notas da Turma")
print("3 - Verificador de Senha")
print("4 - Analisador de Números (Pares e Ímpares)")

opcao = input("Escolha uma opção (1 a 4): ")

# 1 - Calculadora Básica
if opcao == "1":
    print("Calculadora Básica")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Escolha a operação (1 a 4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        print("Resultado:", num1 + num2)
    elif operacao == "2":
        print("Resultado:", num1 - num2)
    elif operacao == "3":
        print("Resultado:", num1 * num2)
    elif operacao == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero")
    else:
        print("Operação inválida")

# 2 - Média de Notas da Turma
elif opcao == "2":
    quantidade = int(input("Quantos alunos há na turma? "))

    soma = 0

    for i in range(quantidade):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        soma += nota

    media = soma / quantidade
    print("Média da turma:", media)

# 3 - Verificador de Senha
elif opcao == "3":
    senha = input("Digite a senha: ")

    tem_numero = False

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True

    if len(senha) >= 8 and tem_numero:
        print("Senha válida")
    else:
        print("Senha inválida")

# 4 - Analisador de Números
elif opcao == "4":
    quantidade = int(input("Quantos números você vai digitar? "))

    pares = 0
    impares = 0

    for i in range(quantidade):
        numero = int(input(f"Digite o número {i + 1}: "))

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Quantidade de números pares:", pares)
    print("Quantidade de números ímpares:", impares)

# Opção inválida
else:
    print("Opção inválida")
