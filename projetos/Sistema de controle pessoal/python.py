import pandas as pd
import os.path

# Define o nome do arquivo CSV para armazenar os dados
CSV_FILE_NAME = 'dados_financeiros.csv'

# Verifica se o arquivo CSV existe, se não existir, cria um novo
if not os.path.isfile(CSV_FILE_NAME):
    dados_iniciais = pd.DataFrame(columns=['Data', 'Descrição', 'Valor'])
    dados_iniciais.to_csv(CSV_FILE_NAME, index=False)

# Função para adicionar uma transação aos dados
def adicionar_transacao(data, descricao, valor):
    dados = pd.read_csv(CSV_FILE_NAME)
    nova_transacao = pd.DataFrame([[data, descricao, valor]], columns=['Data', 'Descrição', 'Valor'])
    dados = pd.concat([dados, nova_transacao], ignore_index=True)
    dados.to_csv(CSV_FILE_NAME, index=False)

# Função para exibir todas as transações
def exibir_transacoes():
    dados = pd.read_csv(CSV_FILE_NAME)
    print(dados)

# Função para calcular o saldo atual
def calcular_saldo():
    dados = pd.read_csv(CSV_FILE_NAME)
    saldo = dados['Valor'].sum()
    print(f"Saldo atual: R${saldo:.2f}")

# Menu principal
while True:
    print("Controle Financeiro Pessoal")
    print("1. Adicionar Transação")
    print("2. Exibir Transações")
    print("3. Calcular Saldo")
    print("4. Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        data = input("Data (DD/MM/AAAA): ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: R$"))
        adicionar_transacao(data, descricao, valor)
    elif escolha == 2:
        exibir_transacoes()
    elif escolha == 3:
        calcular_saldo()
    elif escolha == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")
