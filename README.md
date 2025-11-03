
<div align="center">

# 🐍 Exercícios em Python — Dicionários, Listas e Conjuntos

<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="300"/>

### 💻 Repositório de práticas com manipulação de dados em Python  
Aprenda e pratique conceitos fundamentais de **estrutura de dados**, **tratamento de arquivos**, e **operações com JSON**, usando exemplos reais e organizados por tópicos.

---

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Ativo-success)
![License](https://img.shields.io/badge/Licença-MIT-green)
![Contribuições](https://img.shields.io/badge/Contribuições-Bem%20vindas-orange)

---

</div>

## 📚 Sumário

1. [Exercício 1 — Atualizar Dicionário de Estoque de Livros](#-1-atualizar-dicionário-de-estoque-de-livros)  
2. [Exercício 2 — Criar Dicionário de Notas por Aluno](#-2-criar-dicionário-de-notas-por-aluno)  
3. [Exercício 3 — Comparar Desempenho de Buscas](#-3-comparar-desempenho-de-buscas)  
4. [Exercício 4 — Converter Dicionário em Lista Tabular](#-4-converter-dicionário-em-lista-tabular)  
5. [Exercício 5 — Remover Leituras Incorretas](#-5-remover-leituras-incorretas)  
6. [Exercício 6 — Atualizar Estoque de Medicamentos com Vencimento](#-6-atualizar-estoque-de-medicamentos-com-vencimento)  
7. [Exercício 7 — Garantir Unicidade de E-mails](#-7-garantir-unicidade-de-e-mails)  
8. [Exercício 8 — Interseção e Diferença entre Conjuntos](#-8-interseção-e-diferença-entre-conjuntos)  
9. [Exercício 9 — Ler Arquivo e Contar Palavras](#-9-ler-arquivo-e-contar-palavras)  
10. [Exercício 10 — Gerar Arquivo de Configuração](#-10-gerar-arquivo-de-configuração)  
11. [Exercício 11 — Converter Dicionário em JSON](#-11-converter-dicionário-em-json)  
12. [Exercício 12 — Consolidar Bases e Exportar para JSON](#-12-consolidar-bases-e-exportar-para-json)  
13. [Como Executar o Projeto](#-como-executar)  
14. [Tecnologias Utilizadas](#-tecnologias-utilizadas)  
15. [Autor](#-autor)  

---

## 🧩 1. Atualizar Dicionário de Estoque de Livros
📚 Atualiza o estoque de livros, adicionando ou removendo conforme a quantidade informada.  
Remove automaticamente os livros com quantidade igual a zero.

```python
estoque = {
    "Python Crash Course": 4,
    "Clean Code": 2,
    "Automate the Boring Stuff": 0
}
```
---

## 🎓 2. Criar Dicionário de Notas por Aluno

* Converte uma lista de tuplas `(aluno, notas)` em dicionário.
* Adiciona novos alunos e filtra apenas os aprovados (média ≥ 6).
* Calcula médias dinamicamente com `sum()` e `len()`.

---

## ⚡ 3. Comparar Desempenho de Buscas

* Compara a velocidade de busca em **listas** e **dicionários**.
* Mede o tempo de execução com `time.perf_counter()`.
* Demonstra a eficiência dos dicionários em consultas.

---

## 📋 4. Converter Dicionário em Lista Tabular

* Transforma um dicionário em uma lista de tuplas.
* Ordena com `sorted()` e `lambda` para gerar um **ranking de notas**.

---

## 🌡️ 5. Remover Leituras Incorretas

* Remove valores negativos (leituras incorretas) do dicionário de temperaturas.
* Garante que os dados finais sejam válidos.

---

## 💊 6. Atualizar Estoque de Medicamentos com Vencimento

* Verifica medicamentos vencidos com `datetime`.
* Remove produtos com data expirada e informa quantos foram removidos.

---

## 📧 7. Garantir Unicidade de E-mails

* Elimina duplicatas usando conjuntos (`set`).
* Exibe lista final ordenada alfabeticamente.

---

## 👥 8. Interseção e Diferença entre Conjuntos

* Mostra:

  * **União** → Todos os clientes únicos
  * **Interseção** → Clientes em comum
  * **Diferença** → Clientes exclusivos de cada grupo
* Ideal para cruzamento de dados de campanhas.

---

## 📖 9. Ler Arquivo e Contar Palavras

* Lê um arquivo `.txt`, remove pontuação e normaliza texto.
* Conta frequência das palavras com um dicionário.
* Exibe as 3 mais frequentes, ordenadas por ocorrência.

---

## ⚙️ 10. Gerar Arquivo de Configuração

* Cria um arquivo `configuracoes.txt` com formato `chave:valor`.
* Lê o arquivo e imprime as configurações gravadas.
* Exemplo simples de escrita/leitura com `open()`.

---

## 💾 11. Converter Dicionário em JSON

* Exporta um dicionário de produtos para `produtos.json` usando `json.dump()`.
* Reabre o arquivo e lê os dados com `json.load()`.
* Exibe o conteúdo e o tipo de dado carregado.

---

## 🌍 12. Consolidar Bases e Exportar para JSON

* Une listas de campanhas em uma **base única de clientes**.
* Usa conjuntos (`set`) para evitar duplicações.
* Exporta os resultados consolidados para `base_clientes.json`.

---

## 🚀 Como Executar

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/exercicios-python-dicionarios.git
   ```

2. **Acesse a pasta**

   ```bash
   cd exercicios-python-dicionarios
   ```

3. **Execute o arquivo principal**

   ```bash
   python exercicios.py
   ```

> 💡 **Dica:** Execute cada bloco em um ambiente interativo (VSCode, Jupyter Notebook ou PyCharm) para visualizar os resultados passo a passo.

---

## 🧰 Tecnologias Utilizadas

| Tecnologia                 | Descrição                                            |
| -------------------------- | ---------------------------------------------------- |
| 🐍 Python 3.10+            | Linguagem principal utilizada                        |
| 🧾 JSON                    | Estrutura de dados para exportação e leitura         |
| ⏱️ time / datetime         | Controle de tempo e manipulação de datas             |
| 📄 Manipulação de Arquivos | Leitura e escrita em `.txt` e `.json`                |
| 🧮 pandas (opcional)       | Utilizado para leitura e exibição de dados tabulares |

---

## ✨ Autor

👤 **Weslley**
🎓 Estudante de Engenharia de Software

> 💬 *"Transformando lógica e dados em soluções eficientes com Python."*

📫 Contato:
🔗 [LinkedIn](https://www.linkedin.com/in/weslley-soares-6677a4234/) | 💻 [GitHub](https://github.com/WeslleySoaresm)

---

<div align="center">

Feito com ❤️ e ☕ usando **Python**

</div>
