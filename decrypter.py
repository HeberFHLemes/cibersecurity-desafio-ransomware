import os
import pyaes

## Abrir o arquivo descriptografado
file_name = "teste.txt.ransomwaretroll"
with open(file_name, "rb") as file:
  file_data = file.read()

## Chave para descriptografar
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover arquivo criptografado
os.remove(file_name)

## Criar arquivo descriptografado
new_file = "teste.txt"
with open(new_file, "wb") as new_file:
  new_file.write(decrypt_data)
