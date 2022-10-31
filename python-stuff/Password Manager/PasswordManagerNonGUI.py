## NoFrillsPasswordManager - Non-GUI Based, Alex Arias 10.27.2022
import random
import os

print("NoFrillsPasswordManager (non-GUI) v.0.3c by Alex A")
print()
input("Press any key to continue")

def clear():
   os.system("cls")
   os.system("clear")

def gen():
    shuffle = [origin,fav_number,color,phrase]
    random.shuffle(shuffle)
    result = ''.join(str(item) for item in shuffle)
    print("Your new password is" + result +"$")


main_menu_prompts = [
    "What would you like to do?",
    "(1) Create new password",
    "(2) Store password to Vault",
    "(3) Access password Vault",
    "(4) Quit"
]

choice_prompts = [
    "Press 1 to return to main menu, or press 2 and press Enter to shuffle generated password > ",
    "Press 1 to shuffle again, or press 2 and press Enter to return to main menu > ",

]


## MAIN variables
menu_choice = ""
exist = os.path.exists('key.txt')
mainmenu = False
run = True
menu_state = 0
newpassword = False
vault_main = False
did_shuffle = False

#USER Variables
origin = ""
fav_number = ""
color = ""
phrase = ""



def get_key():
    print("Checking if key file exits....")
    print("Does key file exist?: " + str(exist))

    if exist:
        print("Key file found!\nWelcome back!")

    if not exist:
        print("No key file found!")


# MAIN MENU OPTIONS
while run:
    clear()
    mainmenu = True
    while mainmenu and menu_state == 0:
        print(main_menu_prompts[0])
        print()
        print(main_menu_prompts[1])
        print(main_menu_prompts[2])
        print(main_menu_prompts[3])
        print(main_menu_prompts[4])
        print()

        try:
            menu_choice = int(input("> "))
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
            vault_main = True
            menu_state = menu_state + 5
            mainmenu = False
            run = False

        elif menu_choice == 4:
            quit()

        if menu_choice > 4:
            print("Not a valid choice! Press enter to continue")
            input()
            clear()

# NEW PASSWORD STATE
    while newpassword and menu_state == 1:
        menu_choice = ""
        print("Okay, you want to generate a new password, fill in these quick questions to generate")
        origin = input("What is your background? ")
        fav_number = input("Type a favorite number ")
        color = input("Type your favorite color(s) ")
        phrase = input("Type a phrase you'd like to be included in your password ")
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


# WHILE RE-ROLLING
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

## Vault Main variables

did_consent = False
is_keyValid = False
has_Key = False

#Check for key

def check_for_key():
    print("Checking if key file exits....")
    print("Does key file exist?: " + str(exist))

    if exist:
        print("Key file found!\nWelcome back!")
        input("Press enter to access Vault menu")

    if not exist:
        print("No key file found!")
        input("Please generate a new one to securely store passwords.\n Press Enter to continue to Vault menu.")


## Main Vault menu

while vault_main and menu_state == 5:
    clear()
    print("Welcome to Your Vault")
    print()
    print("(1) View Passwords")
    print("(2) Store new Passwords")
    print("(3) Generate new Storage key")
    print("(4) Delete Entries")
    print("(5) Return to Main Menu")
    print("(6) Quit")
    print()
    input("")
    