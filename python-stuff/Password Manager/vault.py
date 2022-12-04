## Vault password encrypter and decrpyter
   ## Alex Arias 11/10/2022

from cryptography.fernet import Fernet
import random
import time
import base64
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich import print
from rich.panel import Panel
from rich import box
import os


console = Console()

#USER Variables
name = ""
fav_number = ""
color = ""
phrase = ""

def clear():
   #os.system("cls")
   os.system("clear")


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

    with open('manifest.obey', 'rb') as read:
        data = read.read()

    encryptedData = f.encrypt(data)

    with open('manifest.obey', 'wb') as save:
        save.write(encryptedData)


## Decrypt File and Print

def decrypt():
    with open('vault.key', 'rb') as file:
        key = file.read()
    ## Open and read keyfile

    with open('manifest.obey', 'rb') as read:
        encryptedData = read.read()
    ## Open and Read Encrypted data
    f = Fernet(key)

    decryptedData = f.decrypt(encryptedData)
    print()
    print(decryptedData.decode())


## Add password to vault
def vault_add_Pass():
    clear()
    print(Panel.fit("[b]Type the name of the service this password will belong to[/]", title="Service Name", padding=(2, 25)))
    service = console.input("[b][yellow][r]Service Name:[/] > ")
    if service == "":
        input("You must provide a service name! Press enter to conitnue...")
        vault_add_Pass()
    clear()
    print(Panel.fit("[b]Now type in the password you want stored. INFO HERE[/]", title="Password", padding=(2, 25)))
    passwd = console.input("[b][yellow][r]Password:[/] > ")
    with open('vault.key', 'rb') as file:
        key = file.read()

    fernet = Fernet(key)

    with open('manifest.obey', 'rb') as enc_file:
        encrypted = enc_file.read()

    ## Above opens key file, reads encrypted manifest, if valid then decrypts it

    decrypted = fernet.decrypt(encrypted)

    with open('manifest.obey', 'wb') as dec_file:
        dec_file.write(decrypted)

    ## The file is now decrypted and ready for writing

    with open('manifest.obey', 'ab') as append_new:
        append_new.write(f'\n{service.upper()} : {passwd}'.encode())

    ## We append and add a new line to the list and then re-encrypt
    read_and_encrypt()
    clear()


def turnicate_entry():

    service_name = input("To remove a password entry, type in the service name: > ").upper()
    with open('vault.key', 'rb') as file:
        key = file.read()

    fernet = Fernet(key)

    with open('manifest.obey', 'rb') as enc_file:
        encrypted = enc_file.read()

    ## Above opens key file, reads encrypted manifest, if valid then decrypts it

    decrypted = fernet.decrypt(encrypted)

    with open('manifest.obey', 'wb') as dec_file:
        dec_file.write(decrypted)

    ## The file is now decrypted and ready for deletion

    with open('manifest.obey', 'r+') as turn:
        e = turn.readlines()
        turn.seek(0)
        for line in e:
            if service_name not in line:
                turn.write(line)
        turn.truncate()

    ## Opens as read & write, resets cursor, rewrites everything to file except
    ## specified service
    input("Password successfully removed, press enter to return to main menu")
    read_and_encrypt()

    ## Re-encrypts file



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
    print(Panel.fit("\n[b][blue]Your new password is:[/] " + result +"$\n", box=box.ASCII))


def gen_key(): 
    console.print(Panel("[b][yellow]Enter a 4-digit pin number or password to associate with your key file[/]\n", padding=(2, 20)))
    keygen = console.input("\n[b][yellow][r]>[/] ")
    user_key = open("stub.ini", "wb")
    encoded = base64.b64encode(keygen.encode("utf-8"))
    user_key.write(encoded)
    os.system("attrib +h stub.ini")
    user_key.close()
    with open('manifest.obey', 'w') as f:
        f.write("")
    gen_enc_key()
    read_and_encrypt()
    input("Key file successfully generated, Press enter to enter vault menu")
    clear()
