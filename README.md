# 📅 Projeto Agenda de Tarefas em Python

Este é um projeto de estudo desenvolvido para praticar os conceitos fundamentais da linguagem Python, evoluindo desde a manipulação de dados em memória até a persistência em bancos de dados.

## 🚀 Evolução do Projeto

O projeto foi dividido em marcos de aprendizagem para demonstrar o progresso técnico:

### 🔹 Versão 1.0 - Manipulação em Memória (RAM)
* **Foco:** Lógica de programação, Listas e Dicionários.
* **Funcionamento:** Os dados são armazenados em uma lista de dicionários durante a execução. Ao fechar o programa, os dados são perdidos.
* **Conceitos:** CRUD (Create, Read, Update, Delete), loops `while`, condicionais e funções.

### 🔹 Versão 2.0 - Persistência em Arquivo TXT
* **Foco:** Manipulação de arquivos (I/O).
* **Funcionamento:** Utiliza o gerenciador de contexto `with open` para salvar e ler dados em um arquivo `agenda.txt`.
* **Conceitos:** Persistência de dados, tratamento de strings (`split`, `strip`), e manipulação de arquivos nos modos `r` (leitura), `a` (append) e `w` (escrita).

### 🔹 Versão 3.0 - Banco de Dados MySQL (Próximo Passo)
* **Objetivo:** Integrar o Python com um banco de dados relacional (MySQL).
* **Conceitos:** SQL, conexões via `mysql-connector`, queries e segurança de dados.

## 🛠️ Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório ou baixe o arquivo `.py`.
3. Execute o programa via terminal:
   ```bash
   python agenda_v2.py
