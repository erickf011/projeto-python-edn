tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 / num2
        print("Resultado da divisão", resultado)
        break  # sai do loop se der certo

    except ValueError:
        tentativas += 1
        print(f"Erro: digite apenas números. Tentativa {tentativas}\3")

    except ZeroDivisionError:
        tentativas += 1
        print(f"Erro não é possivel dividir por zero. Tentativa {tentativas}/3")

if tentativas == max_tentativas:
    print("Número máximo de tentativas atingido. Encerrando o programa")
