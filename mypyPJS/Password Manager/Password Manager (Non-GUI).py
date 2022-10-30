## Password Generator - Non-GUI Based, Alex Arias 10.27.2022
import random
import os

print("Password manager (non-gui) v.0.3a by Alex A")
print()
input("Press any key to continue")

#def clear():
#   os.system("cls")

run = True
mainmenu = False
menu_state = 0
newpassword = False
vault = False
did_reroll = False
menu_choice = ""

#USER Variables
origin = ""
fav_number = ""
color = ""
phrase = ""
did_consent = False
is_IDValid = False
has_ID = False


def regen():
    re_roll = [origin,fav_number,color,phrase]
    random.shuffle(re_roll)
    result = ''.join(str(item) for item in re_roll)
    print("Your new password is" + result,"$")

def getvault():
    print("Checking if key file exits....")
    result = os.path.exists('key.txt')

    if result:
        print("Welcome back!")

    elif result == False:
        print("No key file found!")


# MAIN MENU OPTIONS
while run:
    mainmenu = True
    while mainmenu and menu_state == 0:
        print("What would you like to do?")
        print()
        print("(1) Create New Password")
        print("(2) Store Password to Vault (Coming Soon)")
        print("(3) Access Password Vault (Coming Soon)")
        print("(4) Quit")
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

        elif menu_choice == 2:
            vault = True
            menu_state = menu_state + 5
            mainmenu = False

        elif menu_choice == 4:
            quit()

        if menu_choice > 4:
            print("Not a valid choice! Press enter to continue")
            input()

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
        regen()
        print()
        try:
            menu_choice = int(input("Type 1 to return to main menu , or, type 2 and press enter to re-roll "))
        except ValueError:
            print("Invalid input! Press enter to return to main menu")
            input()


        if menu_choice == 1:
            menu_state = menu_state - 1
            mainmenu = True
            newpassword = False

        elif menu_choice == 2:
            newpassword = False
            did_reroll = True
            menu_state = menu_state + 1

        else:
            newpassword = False
            menu_state = menu_state - 1
            mainmenu = True


# WHILE RE-ROLLING
    while did_reroll and menu_state == 2:
        print("Re-rolling....")
        regen()
        choice_sub = ""

        try:
            choice_sub = int(input("Type 1 to re-roll or type 2 to return to main menu "))
        except ValueError:
            print("Not a valid option, press enter to re-roll")
            input()
            break

        if choice_sub == 1:
            newpassword = False
            regen()

        elif choice_sub == 2:
            mainmenu = True
            menu_state = menu_state - 2
            did_reroll = False

        else:
            print("Invalid option!")
            input("Press enter to re-roll")

## WHILE IN VAULT

    while vault and menu_state == 5:
        getvault()
        vault_choice = int(input("Type 1 to create a new key, or press 2 to return to main menu:> "))

        if vault_choice == 1:
            key = random.seed(10)
            file = open('key.txt', 'w')
            file.write("key")
            file.close()
            print("Key successfully generated!")
            input("Press Enter to continue to Password Vault")

        elif vault_choice == 2:
            vault = False
            menu_state = menu_state - 5
            mainmenu = True


