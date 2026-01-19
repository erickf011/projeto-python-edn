import random
import string
import requests


def gerar_senha():
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        caracteres = string.ascii_letters + string.digits + string.punctuation

        senha = ""
        for i in range(tamanho):
            senha += random.choice(caracteres)

        print("Senha gerada:", senha)
    except ValueError:
        print("Digite um número válido para o tamanho da senha.")


def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        usuario = dados["results"][0]

        nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("Nome:", nome)
        print("Email:", email)
        print("País:", pais)

    except requests.exceptions.RequestException:
        print("Falha ao conectar na API de usuário.")


def consultar_cep():
    cep = input("Digite o CEP: ")
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("Logradouro:", dados["logradouro"])
            print("Bairro:", dados["bairro"])
            print("Cidade:", dados["localidade"])
            print("Estado:", dados["uf"])

    except requests.exceptions.RequestException:
        print("Falha ao consultar o CEP.")


def consultar_moeda():
    moeda = input("Digite a moeda (ex: USD, EUR): ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = moeda + "BRL"

        if chave not in dados:
            print("Moeda não encontrada.")
        else:
            info = dados[chave]
            print("Valor atual:", info["bid"])
            print("Máxima:", info["high"])
            print("Mínima:", info["low"])
            print("Última atualização:", info["create_date"])

    except requests.exceptions.RequestException:
        print("Erro ao consultar a cotação da moeda.")


# MENU PRINCIPAL
while True:
    print("\n=== ATIVIDADE 6 ===")
    print("1 - Gerar senha aleatória")
    print("2 - Buscar usuário fictício")
    print("3 - Consultar CEP")
    print("4 - Consultar cotação de moeda")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        gerar_senha()
    elif opcao == "2":
        buscar_usuario()
    elif opcao == "3":
        consultar_cep()
    elif opcao == "4":
        consultar_moeda()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
        
