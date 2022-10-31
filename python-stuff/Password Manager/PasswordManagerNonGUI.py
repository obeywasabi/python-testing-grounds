## Password Generator - Non-GUI Based, Alex Arias 10.27.2022
import random
import os

print("Password manager (non-gui) v.0.3c by Alex A")
print()
input("Press any key to continue")

def clear():
   os.system("cls")

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

run = True
mainmenu = False
menu_state = 0
newpassword = False
vault = False
did_shuffle = False
menu_choice = ""

#USER Variables
origin = ""
fav_number = ""
color = ""
phrase = ""
did_consent = False
is_IDValid = False
has_ID = False

def gen():
    shuffle = [origin,fav_number,color,phrase]
    random.shuffle(shuffle)
    result = ''.join(str(item) for item in shuffle)
    print("Your new password is" + result +"$")

def get_key():
    print("Checking if key file exits....")
    result = os.path.exists('key.txt')

    if result:
        print("Welcome back!")

    elif result == False:
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
            vault = True
            menu_state = menu_state + 5
            mainmenu = False
            clear()

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

## WHILE IN VAULT

    while vault and menu_state == 5:
        clear()
        get_key()
        vault_choice = int(input("Press 1 to create a new key, or press 2 to return to main menu > "))

        if vault_choice == 1:
            clear()
            key = random.seed(10)
            file = open('key.txt', 'w')
            file.write("key")
            file.close()
            print("Key successfully generated!")
            input("Press Enter to continue to Password Vault")

        elif vault_choice == 2:
            clear()
            vault = False
            menu_state = menu_state - 5
            mainmenu = True