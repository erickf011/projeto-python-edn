def verificar_resultado(nota):
    if nota >=6:
        return "Aprovado"
    else:
        return "Reprovado"
nota = float(input("Digite a nota do aluno"))
print(verificar_resultado(nota))


