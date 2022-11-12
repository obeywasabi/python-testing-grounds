## Vault password encrypter and decrpyter
   ## Alex Arias 11/10/2022

from cryptography.fernet import Fernet
import random
import base64
import os


#USER Variables
name = ""
fav_number = ""
color = ""
phrase = ""

def clear():
   os.system("cls")
   #os.system("clear")


## Generate Encrypted Key

def gen_enc_key():
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


## Add password to vault
def vault_add_Pass():
    clear()

    service = input("First, add what service this password will belong to: > ")
    passwd = input("Now type in the password you'd like to save: > ")

    with open('vault.key', 'rb') as file:
        key = file.read()

    fernet = Fernet(key)

    with open('manifest.env', 'rb') as enc_file:
        encrypted = enc_file.read()

    ## Above opens key file, reads encrypted manifest, if valid then decrypts it

    decrypted = fernet.decrypt(encrypted)

    with open('manifest.env', 'wb') as dec_file:
        dec_file.write(decrypted)

    ## The file is now decrypted and ready for writing

    with open('manifest.env', 'ab') as append_new:
        append_new.write(f'\n{service.upper()} : {passwd}'.encode())

    ## We append and add a new line to the list and then re-encrypt
    read_and_encrypt()

def b64_decode():
   with open("stub.ini", "r") as f:
       result = f.readline()
       decoded = base64.b64decode(result).decode("utf-8")
       global secretKey
       secretKey = decoded
       f.close()
       clear()


def gen():
    shuffle = [name, fav_number, color, phrase]
    random.shuffle(shuffle)
    result = ''.join(str(item) for item in shuffle)
    print("Your new password is" + result +"$")


def gen_key():
    keygen = input("Enter a 4-digit pin number or password to associate with your key file: > ")
    user_key = open("stub.ini", "wb")
    encoded = base64.b64encode(keygen.encode("utf-8"))
    user_key.write(encoded)
    user_key.close()

    gen_enc_key()
    read_and_encrypt()
    input("Key file successfully generated, Press enter to return to main menu")
    clear()
