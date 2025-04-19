from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad 
from Crypto.Util.Padding import unpad 
import base64 

chave = get_random_bytes(16) 
print("Chave AES gerada:", chave.hex()) 

mensagem = "Segredo importante!"
mensagem_bytes = mensagem.encode() 

cifra = AES.new(chave, AES.MODE_CBC)
iv = cifra.iv 
mensagem_cifrada = cifra.encrypt(pad(mensagem_bytes, AES.block_size)) 

mensagem_final = base64.b64encode(iv + mensagem_cifrada).decode() 
print("Mensagem cifrada (Base64):", mensagem_final)

dados = base64.b64decode(mensagem_final) 
iv_recuperado = dados[:16] 
mensagem_cifrada_recuperada = dados[16:]
cifra2 = AES.new(chave, AES.MODE_CBC, iv=iv_recuperado) 
mensagem_decifrada = unpad(cifra2.decrypt(mensagem_cifrada_recuperada), AES.block_size)

print("Mensagem decifrada:", mensagem_decifrada.decode()) 




