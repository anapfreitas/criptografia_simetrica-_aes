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

## 🧠 Explicação Técnica do Código

| Etapa                                     | Explicação                                                                                  |
|-------------------------------------------|----------------------------------------------------------------------------------------------|
| `get_random_bytes(16)`                    | Gera uma chave AES aleatória de 128 bits (16 bytes).                                        |
| `.encode()`                               | Converte a mensagem de texto para bytes, pois o AES só aceita dados binários.              |
| `pad(..., AES.block_size)`                | Adiciona preenchimento à mensagem para que ela tenha tamanho múltiplo de 16 bytes.         |
| `AES.new(chave, AES.MODE_CBC)`           | Cria o objeto de cifragem no modo CBC, utilizando a chave gerada.                          |
| `cipher.encrypt(...)`                     | Cifra a mensagem em blocos encadeados usando a chave e o IV.                               |
| `iv + mensagem_cifrada`                   | Junta o vetor de inicialização (IV) com a mensagem cifrada.                                |
| `base64.b64encode(...)`                   | Codifica a mensagem cifrada em Base64 para facilitar envio, armazenamento ou visualização. |
| `base64.b64decode(...)`                   | Decodifica a mensagem Base64 de volta para bytes (para decifrar).                          |
| `dados[:16]`                              | Recupera os primeiros 16 bytes do IV.                                                      |
| `dados[16:]`                              | Recupera o restante da mensagem cifrada.                                                   |
| `AES.new(chave, AES.MODE_CBC, iv=...)`   | Cria o objeto de decifragem AES com o mesmo IV usado na cifragem.                          |
| `cipher.decrypt(...)`                     | Decifra os dados de volta para a versão original com padding.                              |
| `unpad(..., AES.block_size)`              | Remove o padding adicionado durante a cifragem.                                             |
| `.decode()`                               | Converte os bytes decifrados de volta para string legível.                                 |


👩‍💻 Autora
Ana Paula Santos de Freitas
Curso: Análise e Desenvolvimento de Sistemas
Disciplina: Segurança da Informação
Instituto Federal do Triângulo Mineiro – Campus Patrocínio.

📜 Licença
Este projeto é de uso acadêmico e didático.
