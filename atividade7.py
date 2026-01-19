import csv
import json
import statistics


def analisar_csv():
    nome_arquivo = input("Digite o nome do arquivo CSV: ")

    try:
        tempos = []

        with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                tempos.append(float(linha["tempo_execucao"]))

        media = statistics.mean(tempos)
        maior = max(tempos)

        print("Média do tempo de execução:", media)
        print("Maior tempo de execução:", maior)

    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except Exception:
        print("Erro ao ler o arquivo CSV.")


def criar_arquivo_txt():
    nome_arquivo = input("Digite o nome do arquivo TXT para salvar: ")

    pessoas = [
        {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
        {"nome": "Mariana", "idade": 22, "cidade": "Belo Horizonte"}
    ]

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("Nome\tIdade\tCidade\n")

            for pessoa in pessoas:
                linha = f"{pessoa['nome']}\t{pessoa['idade']}\t{pessoa['cidade']}\n"
                arquivo.write(linha)

        print("Arquivo salvo com sucesso.")

    except Exception:
        print("Falha ao salvar o arquivo.")


def ler_arquivo_txt():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception:
        print("Erro ao ler o arquivo.")


def trabalhar_com_json():
    nome_arquivo = input("Digite o nome do arquivo JSON: ")

    dados = {
        "nome": "João",
        "idade": 28,
        "cidade": "Curitiba"
    }

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados_lidos = json.load(arquivo)

        print("Dados lidos do JSON:")
        print("Nome:", dados_lidos["nome"])
        print("Idade:", dados_lidos["idade"])
        print("Cidade:", dados_lidos["cidade"])

    except Exception:
        print("Erro ao salvar ou ler o arquivo JSON.")


# MENU PRINCIPAL
while True:
    print("\n=== ATIVIDADE 7 ===")
    print("1 - Analisar arquivo CSV")
    print("2 - Criar arquivo TXT com dados")
    print("3 - Ler arquivo TXT")
    print("4 - Escrever e ler arquivo JSON")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        analisar_csv()
    elif opcao == "2":
        criar_arquivo_txt()
    elif opcao == "3":
        ler_arquivo_txt()
    elif opcao == "4":
        trabalhar_com_json()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
