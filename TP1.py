
#Exercício 1 Atualizar dicionário de estoque de livros 
# Dados iniciais
estoque = {
    "Python Crash Course": 4,
    "Clean Code": 2,
    "Automate the Boring Stuff": 0
}

def adiciona_livro(estoque, livro, quantidade):
    """Adiciona ou atualiza a quantidade de um livro no estoque."""
    estoque[livro] = quantidade
    return estoque, livro, quantidade

def removeLivroQuantidadeFor0(estoque, livro, quantidade):
    """Remove o livro do estoque se a quantidade for 0."""
    if quantidade == 0:
        estoque.pop(livro, None)
        return estoque, livro, quantidade



# Função para atualizar o estoque
def atualizar_estoque(estoque, livro, quantidade):
    """Atualiza o estoque com base na quantidade fornecida."""
    if quantidade == 0:
        # Remove o livro se a quantidade final for 0
        removeLivroQuantidadeFor0(estoque, livro, quantidade)
    else:
        # Atualiza ou adiciona o livro
        adiciona_livro(estoque, livro, quantidade)

    # Imprime o estoque atualizado
    print(f"Estoque atualizado: {estoque}")
    return estoque

# Testes solicitados
atualizar_estoque(estoque, "Clean Code", 0)
atualizar_estoque(estoque, "Fluent Python", 5)
atualizar_estoque(estoque, "Automate the Boring Stuff", 1)
atualizar_estoque(estoque, "C#", 5)
atualizar_estoque(estoque, "C++", 5)


#%%
#Exercício 2 Criar dicionário de notas por aluno

# Lista de tuplas com nome e notas
registros = [
    ("Ana", [8, 9, 7]),
    ("Bruno", [5, 6, 5]),
    ("Carla", [10, 9, 10])
]


# 1. Converte a lista em um dicionário
def convert_lista_em_dicionario(lista):
    """Converte uma lista de tuplas em um dicionário."""
    lista = dict(registros)
    return lista

# 2. Adiciona Daniel ao dicionário
def adicionar(lista_convertida, nome, notas):
    """Adiciona um novo aluno e suas notas ao dicionário."""
    lista_convertida[nome] = notas
    return lista_convertida, nome, notas


#Chamando funções do Programa
lista_convertida = convert_lista_em_dicionario(registros)
adicionar(lista_convertida, "Daniel", [7, 7, 8])


# 3. Remove alunos com média < 6
# Cria um novo dicionário apenas com os aprovados
notas_filtradas = {}

for aluno, lista_notas in lista_convertida.items():
    media = sum(lista_notas) / len(lista_notas)
    if media >= 6:
        notas_filtradas[aluno] = lista_notas
    


# 4️⃣ Imprime o resultado final
print("Dicionário final de notas (apenas alunos com média ≥ 6):")
print(notas_filtradas)
#%%

#Exercício 3 Comparar desempenho de buscas em lista e dicionário

import time

# Dados iniciais
sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
sensores_dict = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

# Listas para armazenar os tempos de cada busca
tempos_lista = []
tempos_dict = []

# Número de execuções
execucoes = 10000

# 🔍 Busca na lista
for _ in range(execucoes):
    inicio = time.perf_counter()
    for chave, valor in sensores_lista:
        if chave == "S3":
            resultado = valor
            break
    fim = time.perf_counter()
    tempos_lista.append(fim - inicio)

# 🔍 Busca no dicionário
for _ in range(execucoes):
    inicio = time.perf_counter()
    resultado = sensores_dict["S3"]
    fim = time.perf_counter()
    tempos_dict.append(fim - inicio)

# 🧮 Cálculo das médias
media_lista = sum(tempos_lista) / execucoes
media_dict = sum(tempos_dict) / execucoes

# 📊 Relatório final
print("\n# Relatório de Comparação de Desempenho")
print(f"Execuções: {execucoes}")
print(f"Tempo médio (lista): {media_lista:.8f} segundos")
print(f"Tempo médio (dicionário): {media_dict:.8f} segundos")
#%%

#Exercício 4 Converter dicionário em lista tabular

medias = {"Ana": 8.5, "Bruno": 6.3, "Carla": 9.1}

lista_medias = list(medias.items())# Converte o dicionário em uma lista de tuplas

print("Lista de médias:", lista_medias)


def ordenar_medias(lista_medias):
    """Ordena a lista com base nas médias em ordem decrescente usando sorted(), lambda e reverse=True"""
    ranking = sorted(lista_medias, key=lambda x: x[1], reverse=True)
    return ranking

print("Ranking de médias Ordenado:", ordenar_medias(lista_medias))

#%%

#Exercício 5 Remover leituras incorretas

temperaturas = {
    "RJ": 29.4, "SP": -99.0, "MG": 27.2, "BA": 31.1, "RS": -88.0
}


def filtrar_temperaturas(temp_dict):
    """Remove leituras incorretas (valores negativos) do dicionário de temperaturas."""
    temp_filtradas = {}
    for cidade, temp in temp_dict.items():
        if temp >= 0:
            temp_filtradas[cidade] = temp
    return temp_filtradas

temperaturas_corretas = filtrar_temperaturas(temperaturas)
print("Temperaturas corretas:", temperaturas_corretas)

#%%

#Exercício 6 Atualizar estoque com vencimento
import datetime

medicamentos = {
    "Aspirina": "2024-11-01",
    "Dipirona": "2026-03-10",
    "Paracetamol": "2023-12-01"
}

#1. comparar datas de vencimento
def verificar_vencimento(medicamentos):
    """Verifica e imprime os medicamentos vencidos."""
    hoje = datetime.date.today()
    medicamentos_vencidos = []

    for medicamento, data_vencimento in medicamentos.items():
        data_venc = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d").date()
        if data_venc < hoje:
            medicamentos_vencidos.append(medicamento)

    return medicamentos_vencidos



#2. atualizar estoque removendo medicamentos vencidos
def atualizar_estoque(medicamentos):
    """Atualiza o estoque removendo medicamentos vencidos."""
    hoje = datetime.date.today()
    estoque_atualizado = {}

    for medicamento, data_vencimento in medicamentos.items():
        data_venc = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d").date()
        if data_venc >= hoje:
            estoque_atualizado[medicamento] = data_vencimento

    return estoque_atualizado

# Testando a função
print("\nMedicamentos vencidos:", verificar_vencimento(medicamentos))
estoque_atualizado = atualizar_estoque(medicamentos)
print("\nEstoque atualizado (sem vencidos):", estoque_atualizado)

print("\nTotal de medicamentos removidos:", len(medicamentos) - len(estoque_atualizado)) # Imprime a quantidade de medicamentos removidos

#%%
#Exercício 7 Garantir unicidade

emails = [
    "ana@empresa.com", "bruno@empresa.com", "ana@empresa.com",
    "carla@empresa.com", "bruno@empresa.com", "daniel@empresa.com"
]

# Garantindo unicidade removendo duplicatas
emails_unicos = set(emails)

print(sorted(emails_unicos))  # Saída ordenada em ordem alfabética para melhor visualização

#%%

#Exercício 8 Analisar interseção e diferença entre conjuntos

clientes_A = {"Ana", "Bruno", "Carla", "Daniel"}
clientes_B = {"Bruno", "Carla", "Eduardo", "Fernanda"}


uniao_conjuntos = clientes_A | clientes_B #atalho para cliente_A.union(cliente_B)
print("\nUnião:", uniao_conjuntos)

conjuntos = clientes_A & clientes_B #atalho para cliente_A.intersection(cliente_B)
print("\nInterseção:", conjuntos)

diferenca_conjuntos = clientes_A - clientes_B   #atalho para cliente_A.difference(cliente_B)
print("\nDiferença:", diferenca_conjuntos)

print(f"\ntotal de clientes : {len(uniao_conjuntos)}") #total de clientes únicos nos dois conjuntos

#%%
#Exercício 9 Ler arquivo e contar palavras 

import string
import pandas as pd

palavras = []
with open("relatorio.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        relatorio_limpo = linha.lower().translate(str.maketrans("","", string.punctuation))
        print(relatorio_limpo.strip())
        palavras.extend(relatorio_limpo.split()) 


contagem_palavras =  {}

for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print("\nContagem de palavras:\n", contagem_palavras)

palavras_frequentes = sorted(contagem_palavras.items(), key=lambda item: item[1], reverse=True)[:3]
print("\nPalavras mais frequentes:\n", palavras_frequentes)
for palavra, frequencia in palavras_frequentes:
    print(f"A palavra '{palavra}' apareceu {frequencia} vezes.")
#%%

#Exercício 10 Gerar arquivo de configuração
config = {
    "servidor": "192.168.0.10",
    "porta": 8080,
    "modo": "produção"
}

with open("configuracoes.txt", "w", encoding="utf-8") as arquivo:
    for chave, valor in config.items():
        arquivo.write(f"{chave}:{valor}\n")
        print("\u2705 Configuração gravada:", chave, "->", valor)

with open("configuracoes.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print("\U0001F527 Configuração lida:", linha.strip())


#Exercício 11 Converter dicionário em JSON 
import json
import os
import pandas as pd
#dicionário de produtos
produtos = {
    "Smartphone": {"preco": 2500, "estoque": 12},
    "Notebook": {"preco": 4800, "estoque": 5},
    "Fone Bluetooth": {"preco": 300, "estoque": 25}
}

#exportando o dicionário para um arquivo JSON
with open("produtos.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(produtos, arquivo_json, indent=4, ensure_ascii=False)
    print("\U0001F4BE Arquivo 'produtos.json' criado com sucesso.")


#reabrindo o arquivo JSON e carregando os dados em um dicionário
with open("produtos.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json)
    print("\U0001F4C2 Dados carregados do arquivo JSON:")
    print(dados_carregados)
    print(f"\ntipos de dados: {type(dados_carregados)}")

#%%

#Exercício 12 Consolidar bases e exportar para JSON 
import json

campanha_1 = ["Ana", "Bruno", "Carla"]
campanha_2 = ["Bruno", "Daniel", "Eduardo"]
campanha_3 = ["Ana", "Fernanda", "Gustavo"]

#converter listas em conjuntos para facilitar as operações
set_1 = set(campanha_1)
set_2 = set(campanha_2)
set_3 = set(campanha_3)

base_unica = set_1 | set_2 | set_3  # união dos três conjuntos
print("Base única de clientes:", base_unica)\

dados = {
    "total_clientes": len(base_unica),
    "clientes": list(base_unica)
}

with open("base_clientes.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
    print("\U0001F4BE Arquivo 'base_clientes.json' criado com sucesso.")

with open("base_clientes.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json)
    print("\U0001F4C2 Dados carregados do arquivo JSON:")
    print(dados_carregados)

#%%

