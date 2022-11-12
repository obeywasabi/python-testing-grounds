## NoFrillsPasswordManager - Non-GUI Based, Alex Arias 10.27.2022

import requests
import urllib.request
import time
import vault
from vault import *

currentVersion = '0.7.9'

def get_update():
    URL = urllib.request.urlopen('https://raw.githubusercontent.com/obeywasabi/python-testing-grounds/main/python-stuff/Password%20Manager/version.txt')
    data = URL.read().decode('utf-8')

    if (data == currentVersion):
        print("Up to date!")
        quit()

    else:
        print("App is not up to date! You are on version " + currentVersion + " but you could be on version " + data + "!")
        choice = int(input("Do you want to update now? Press 1 for Yes and 2 for No: > "))
        if choice == 1:
            print("Downloading new version now, program will quit on its own, please delete OLD executable.")
            newVersion = requests.get("https://github.com/obeywasabi/python-testing-grounds/raw/main/python-stuff/Password%20Manager/PasswordManagerCLI.exe")
            with open(str(data) + ".exe", "wb") as push:
                push.write(newVersion.content)
                quit()

        if choice == 2:
            clear()
            quit()

        else:
            print("Invalid option!")
            quit()

print("NoFrillsPasswordManager (non-GUI) by Alex A")
print()
input("Press any key to continue")


menu_prompts = [
    "What would you like to do?\n",
    "(1) Generate a new password",
    "(2) Enter Vault",
    "(3) Check for updates",
    "(4) Quit"
]

choice_prompts = [
    "Press 1 to return to main menu, or press 2 and press Enter to shuffle generated password: > ",
    "Press 1 to shuffle again, or press 2 and press Enter to return to main menu: > ",

]

newpass_prompts = [
    "USAGE: \nFill in a few questions to generate a new password, realistically you can input anything "
    "into the lines, and the generator will still generate and shuffle all of your inputs. You can also choose to leave"
    "any of the sections blank to generate a shorter or longer password.\n",
    "What is your name?: > ",
    "Type a favorite or rememberable number: > ",
    "Enter a favorite color(s) or any desired input: > ",
    "Enter a phrase or word you want to be included in the password: > "

]

## MAIN Vars
menu_choice = ""
exist = os.path.exists("stub.ini")
mainmenu = False
run = True
menu_state = 0
newpassword = False
key = False
vault_main = False
did_shuffle = False


# WHILE MAIN MENU & OPTIONS
while run:
    clear()
    mainmenu = True
    while mainmenu and menu_state == 0:
        print(menu_prompts[0])
        print(menu_prompts[1])
        print(menu_prompts[2])
        print(menu_prompts[3])
        print(menu_prompts[4])

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


        elif menu_choice == 3:
            get_update()

        elif menu_choice == 4:
                quit()

        if menu_choice > 4:
            print("Not a valid choice! Press enter to continue")
            input()
            clear()

# IF NEW PASSWORD, AND GENERATE
    while newpassword and menu_state == 1:
        menu_choice = ""
        print(newpass_prompts[0])
        vault.name = input(newpass_prompts[1])
        vault.fav_number = input(newpass_prompts[2])
        vault.color = input(newpass_prompts[3])
        vault.phrase = input(newpass_prompts[4])
        print("Generating....")
        print()
        gen()
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


#IF DID SHUFFLE PASSWORD STATE
    while did_shuffle and menu_state == 2:
        clear()
        print("Shuffling....")
        gen()
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
            gen()

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

## VAULT MAIN MENU AND KEY CHECK

while vault_main and menu_state == 5:

    if did_gen_key:
        key = True

    else:
        clear()
        print("You do not have a key file, to access the vault securely, please create one.")
        input("Press enter to create one")
        did_gen_key = True
        clear()
        gen_key()

    while key:
        clear()
        print("Welcome to Your Vault")

        print("(1) View Passwords")
        print("(2) Store new Passwords")
        print("(3) Generate a new Storage key")
        print("(4) Delete Entries")
        print("(5) Return to Main Menu")
        print("(6) Quit")
        print()

        try:
            vault_choice = int(input("Enter a choice: > "))

        except ValueError:
            input("Invalid choice! Press enter to continue")
            break

        if vault_choice == 1:
            clear()
            b64_decode()
            try:
                pin_check = int(input("Enter your pin: > "))
            except ValueError:
                input("Invalid option! Press enter to continue...")
                clear()
                break
            if pin_check == int(vault.secretKey):
                clear()
                decrypt()
                print()
                input("\nPress any key to return to main menu..")
                break
            else:
                print("Pin does not match the set pin!")
                clear()
                break


        if vault_choice == 2:
            clear()
            vault_add_Pass()
            input("\nPassword successfully stored\n Press Enter to return to vault menu")
            break


        if vault_choice == 3:
            os.remove('manifest.env')
            os.remove('vault.key')
            os.remove('stub.ini')
            gen_key()

        if vault_choice == 6:
            quit()