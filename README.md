# 🔐 Projeto de Criptografia Simétrica com AES

Este projeto foi desenvolvido como parte da avaliação da disciplina **Segurança da Informação**, e tem como objetivo aplicar os conceitos de **criptografia simétrica** utilizando o algoritmo **AES (Advanced Encryption Standard)**.

---

## 📘 Descrição

O sistema implementado permite:
- Gerar uma **chave AES de 128 bits**.
- Cifrar uma mensagem de texto com a chave e um IV (vetor de inicialização) aleatório.
- Decifrar a mensagem com segurança, utilizando a mesma chave e IV.
- Utilizar o **modo de operação CBC (Cipher Block Chaining)**, que encadeia os blocos cifrados.
- Converter os dados cifrados para **Base64**, facilitando o armazenamento e a visualização.

---

## 📌 Conceitos Abordados

| Conceito                     | Explicação                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| 🔑 Criptografia Simétrica   | Mesma chave para cifrar e decifrar                                         |
| 🔒 AES                      | Algoritmo moderno e seguro, baseado em blocos de 128 bits                  |
| 🔁 Modo CBC                 | Cada bloco é encadeado ao anterior, aumentando a segurança                 |
| 🧱 Padding                  | Preenchimento para adequar o tamanho dos dados aos blocos do AES           |
| 📜 Base64                   | Codificação que transforma bytes em texto legível para armazenamento/transmissão |

---

## 💻 Execução do Código

### ✅ Requisitos:
- Python 3 instalado
- Biblioteca [`pycryptodome`](https://pypi.org/project/pycryptodome/)

### 🔧 Instalação da biblioteca:

```bash
pip install pycryptodome

```

🖼️ Exemplo de Execução
📷 Imagem da execução do programa: ![image](https://github.com/user-attachments/assets/5c9103a3-00b0-475c-9850-c885aefaa213)

🧠 Explicação Técnica do Código
A chave é gerada aleatoriamente com get_random_bytes(16).

A mensagem é transformada em bytes com .encode().

Usamos pad() para ajustar a mensagem ao tamanho dos blocos do AES.

O AES é executado no modo CBC e o IV é salvo junto com a mensagem cifrada.

O conteúdo é codificado em Base64 para facilitar o envio/armazenamento.

Para decifrar, usamos b64decode(), separamos IV + mensagem e usamos unpad() após decifrar.

👩‍💻 Autora
Ana Paula Santos de Freitas
Curso: Análise e Desenvolvimento de Sistemas
Disciplina: Segurança da Informação
Instituto Federal do Triângulo Mineiro – Campus Patrocínio.
📜 Licença
Este projeto é de uso acadêmico e didático.
