## Vault password encrypter and decrpyter
   ## Alex Arias 11/10/2022

from cryptography.fernet import Fernet

## Generate Encrypted Key

def gen_key():
    key = Fernet.generate_key()
    with open('vault.key', 'wb') as file:
        file.write(key)


## Read data from file & Encrypt data

def read_and_encrypt():

    with open('vault.key', 'rb') as file:
        key = file.read()

    f = Fernet(key)

    with open('manifest.env', 'rb') as read:
        data = read.read()

    encryptedData = f.encrypt(data)

    with open('manifest.env', 'wb') as save:
        save.write(encryptedData)


## Decrypt File and Print

def decrypt():
    with open('vault.key', 'rb') as file:
        key = file.read()
    ## Open and read keyfile

    with open('manifest.env', 'rb') as read:
        encryptedData = read.read()
    ## Open and Read Encrypted data
    f = Fernet(key)

    decryptedData = f.decrypt(encryptedData)
    print()
    print(decryptedData.decode())

decrypt()
