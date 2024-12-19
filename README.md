# Entendendo um Ransomware na Prática com Python

#### Desafio de projeto do Bootcamp Cibersegurança #2, pela DIO.

### Objetivos:
  - Utilizar um código em Python para criptografar um arquivo de texto e outro código para descriptografá-lo, voltando a ser como o original;
  - Relacionar aos conteúdos estudados durante o Bootcamp, como criptografia, vulnerabilidades, ataques cibernéticos e ransomwares, por exemplo.

---

### Estrutura:
  - **encrypter.py**
    - Código para pegar o arquivo de teste e criptografá-lo.

  - **decrypter.py**
    - Código para descriptografar o arquivo já criptografado.

  - **teste.txt**
    - Arquivo de texto que será usado para as demonstrações, sendo criptografado e descriptografado em seguida.

---

### Processo de criação:
- Seguindo o código-fonte como exemplo, os arquivos, códigos e execuções foram criados/executados no Shell do Kali Linux, conforme a seguir:

  ```bash
  mkdir projeto-ramsomware
  cd projeto-ramsomware
  ```
  ``` bash
  touch teste.txt
  touch encrypter.py
  touch decrypter.py
  ```


### Após criados os arquivos, os conteúdos presentes nos mesmos estão conforme as imagens a seguir:
---
   - **encrypter.py**:

  ![encrypter code](https://github.com/user-attachments/assets/52ab6357-d05d-4bd7-95ae-16f5b92e60d9)

---

  - **decrypter.py**:

  ![decrypter code](https://github.com/user-attachments/assets/7e3e66f7-57a1-4e37-8e75-a30a819e469d)



---
  - **teste.txt**:
    
  ![arquivo-texto para teste](https://github.com/user-attachments/assets/977ae53c-ce6f-47dc-be75-9fa5161cdaab)

---
  - **teste.txt.ransomwaretroll** (teste.txt após ser criptografado):

  ![arquivo de texto 'teste.txt' criptografado](https://github.com/user-attachments/assets/f9279d75-985d-41ea-8c7d-79cedafd67c8)


---

- Processo de uso:
  - Para criptografar o arquivo **teste.txt**, basta executar o script:

  ```bash
  python encrypter.py
  ```

  - E para descriptografá-lo:

  ```bash
  python decrypter.py
  ```


# Fins educacionais


  
  


    
