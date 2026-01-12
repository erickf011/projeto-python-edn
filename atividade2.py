# 1 - Conversor de Moeda
reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = reais / taxa_dolar
valor_euro = reais / taxa_euro

print("Reais:", reais)
print("Dólares:", round(valor_dolar, 2))
print("Euros:", round(valor_euro, 2))

# 2 - Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
desconto = 20

valor_desconto = preco_original * desconto / 100
preco_final = preco_original - valor_desconto

print("Produto:", produto)
print("Preço original:", preco_original)
print("Valor do desconto:", valor_desconto)
print("Preço final:", preco_final)

# 3 - Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média:", round(media, 2))

# 4 - Calculadora de Consumo de Combustível
distancia = 300
combustivel = 25

consumo = distancia / combustivel

print("Distância:", distancia)
print("Combustível:", combustivel)
print("Consumo médio:", round(consumo, 2), "km/l")

