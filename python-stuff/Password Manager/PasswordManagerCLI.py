## NoFrillsPasswordManager - Non-GUI Based, Alex Arias 10.27.2022
import random
import os
import base64
import requests
import urllib.request
import time
from cryptography.fernet import Fernet

currentVersion = '0.7.4'

def getupdate():
    URL = urllib.request.urlopen('https://raw.githubusercontent.com/obeywasabi/python-testing-grounds/main/python-stuff/Password%20Manager/version.txt')
    data = URL.read().decode('utf-8')

    if (data == currentVersion):
        print("Up to date!")
        quit()

    else:
        print("App is not up to date! You are on version " + currentVersion + " but you could be on version " + data + "!")
        choice = int(input("Do you want to update now? Press 1 for Yes and 2 for No: > "))
        if choice == 1:
            print("Downloading new version now!")
            newVersion = requests.get("https://github.com/obeywasabi/python-testing-grounds/raw/main/python-stuff/Password%20Manager/PasswordManagerCLI.exe")
            with open("PasswordManagerCLI.exe", "wb") as f:
                f.write(newVersion.content)
                f.close()
                print("New version downloaded, shutting in 3 seconds!")
                time.sleep(3)
                quit()

        if choice == 2:
            clear()
            quit()

        else:
            print("Invalid option!")
            quit()

print("NoFrillsPasswordManager (non-GUI) by Alex A")
print()
input("Press any auth to continue")


def clear():
   #os.system("cls")
   os.system("clear")


def shuffle_pass():
    shuffle = [name, fav_number, color, phrase]
    random.shuffle(shuffle)
    result = ''.join(str(item) for item in shuffle)
    print("Your new password is" + result +"$")


def manifest():
    keygen = input("Enter a 4-digit pin number to associate with your auth file")
    user_key = open("auth.ini", "wb")
    encoded = base64.b64encode(keygen.encode("utf-8"))
    user_key.write(encoded)
    user_key.close()
    gen_vault_key()
    #encrypt_vault_file()
    input("Key file successfully generated, Press enter to return to main menu")
    clear()

## VAULT FUNCTIONS

def gen_vault_key():
    gen_key = Fernet.generate_key()
    with open("enc.key", "wb") as enc:
        enc.write(gen_key)


def load_vault_key():
    return open("enc.key", 'rb').read()


def encrypt_vault_file():
    with open("enc.key", 'rb') as enc:
        key = enc.read()
        fernet = Fernet(key)
    with open("vault.csv", 'rb') as file:
        original = file.read()
        encrypted = fernet.encrypt(original)
    with open("vault.csv", 'wb') as encrypted_vault:
        encrypted_vault.write(encrypted)


def decrypt_vault_file():
    fernet = Fernet(key)
    with open("vault.csv", 'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open("vault.csv", 'wb') as dec_file:
            dec_file.write(decrypted)

#def view_dec_vault():





#def add_pass_enc():


def b64_decode():
   with open("auth.ini", "r") as f:
       result = f.readline()
       decoded = base64.b64decode(result).decode("utf-8")
       global secretKey
       secretKey = decoded
       f.close()
       clear()


menu_prompts = [
    "What would you like to do?\n",
    "(1) Create new password",
    "(2) Store password to Vault",
    "(3) Access password Vault",
    "(4) Check for updates",
    "(5) Quit"
]

choice_prompts = [
    "Press 1 to return to main menu, or press 2 and press Enter to shuffle generated password > ",
    "Press 1 to shuffle again, or press 2 and press Enter to return to main menu > ",

]

newpass_prompts = [
    "USAGE: \nFill in these quick questions to generate a new password, realistically you can input anything "
    "into the lines, and the generator will still generate and shuffle all of your inputs.\n",
    "What is your name? > ",
    "Type a favorite or rememberable number > ",

]

## MAIN variables
menu_choice = ""
exist = os.path.exists("auth.ini")
mainmenu = False
run = True
menu_state = 0
newpassword = False
auth = False
key = Fernet.generate_key()
vault_main = False
did_shuffle = False

## Vault Main variables

#did_consent = False
#did_key_run = 0

#USER Variables
name = ""
fav_number = ""
color = ""
phrase = ""
#username = ""
#pin = ""

# MAIN MENU OPTIONS
while run:
    clear()
    mainmenu = True
    while mainmenu and menu_state == 0:
        print(menu_prompts[0])
        print(menu_prompts[1])
        print(menu_prompts[2])
        print(menu_prompts[3])
        print(menu_prompts[4])
        print(menu_prompts[5])

        try:
            menu_choice = int(input("\n> "))
        except ValueError:
            print("Invalid Option!")
            input("Press enter to continue")
            break

        if menu_choice == 1:
            newpassword = True
            mainmenu = False
            menu_state = menu_state + 1
            clear()

        elif menu_choice == 2:
            clear()
            vault_main = True
            menu_state = menu_state + 5
            mainmenu = False
            run = False

        elif menu_choice == 4:
            getupdate()

        elif menu_choice == 5:
                quit()

        if menu_choice > 5:
            print("Not a valid choice! Press enter to continue")
            input()
            clear()

# NEW PASSWORD STATE
    while newpassword and menu_state == 1:
        menu_choice = ""
        print(newpass_prompts[0])
        name = input(newpass_prompts[1])
        fav_number = input(newpass_prompts[2])
        color = input("Type your favorite color(s) ")
        phrase = input("Type a phrase you'd like to be included in your password ")
        print("Generating....")
        print()
        shuffle_pass()
        print()
        try:
            menu_choice = int(input(choice_prompts[0]))
        except ValueError:
            print("Invalid input! Press enter to return to main menu")
            input()


        if menu_choice == 1:
            menu_state = menu_state - 1
            mainmenu = True
            newpassword = False

        elif menu_choice == 2:
            newpassword = False
            did_shuffle = True
            menu_state = menu_state + 1

        else:
            newpassword = False
            menu_state = menu_state - 1
            mainmenu = True


# WHILE SHUFFLING AGAIN
    while did_shuffle and menu_state == 2:
        clear()
        print("Shuffling....")
        shuffle_pass()
        choice_sub = ""

        try:
            choice_sub = int(input(choice_prompts[1]))
        except ValueError:
            print("Not a valid option, press enter to re-roll")
            input()
            clear()
            break

        if choice_sub == 1:
            clear()
            newpassword = False
            shuffle_pass()

        elif choice_sub == 2:
            clear()
            mainmenu = True
            menu_state = menu_state - 2
            did_shuffle = False

        else:
            print("Invalid option!")
            input("Press enter to shuffle again")
            clear()

did_gen_key = exist


## Main Vault menu

while vault_main and menu_state == 5:

    if did_gen_key:
        auth = True

    else:
        clear()
        print("You do not have a auth file, to access the vault, please create one.")
        input("Press enter to create one")
        did_gen_key = True
        clear()
        manifest()

    while auth:
        clear()
        print("Welcome to Your Vault")
        #print()
        print("(1) View Passwords")
        print("(2) Store new Passwords")
        print("(3) Generate a new Storage auth")
        print("(4) Delete Entries")
        print("(5) Return to Main Menu")
        print("(6) Quit")
        print()
        vault_choice = int(input("> "))

        if vault_choice == 1:
            clear()
            b64_decode()
            try:
                pin_check = int(input("Enter your pin: > "))
            except:
                print("Please enter a valid option")
                input("Press enter to continue...")
                clear()
                break
            if pin_check == int(secretKey):
                clear()
                with open("vault.csv", 'r') as view:
                    print(view.read())
                input("\nPress any key to return to main menu..")
            else:
                print("Pin does not match set pin!")

        else:
            "No valid authentication file found! Please generate one, or generate a new one"


        if vault_choice == 2:
            clear()
            add_pass_enc()
            input("\nPassword successfully stored\n Press Enter to return to vault menu")
            break


        if vault_choice == 3:
            manifest()