## Password generator - Non-GUI Based, Alex Arias 10.27.2022
import random

print("Password manager (non-gui) v.0.1 by Alex A")
print()
input("Press any key to continue")

#def clear():
 #   os.system("cls")

mainmenu = True
newpassword = False
generator = False
vault = False
did_reroll = False
choice = ""
origin = ""
fav_number = ""
color = ""
phrase = ""

def regen():
    re_roll = [origin,fav_number,color,phrase]
    random.shuffle(re_roll)
    result = ''.join(str(item) for item in re_roll)
    print("Your new password is" + result,"$")

# MAIN MENU OPTIONS

while mainmenu:
    print("What would you like to do?")
    print()
    print("(1) Create New Password")
    print("(2) Store Password to Vault (Coming Soon)")
    print("(3) Access Password Vault (Coming Soon)")
    print("(4) Quit")
    try:
        choice = int(input("> "))
    except ValueError:
        print("Use a number!!")
        input("Press enter to continue")

#MENU CHOICE 1

    if choice == 1:
        newpassword = True
        mainmenu = False

# NEW PASSWORD CONDITION
        while newpassword:
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
                choice = int(input("Type 1 to return to main menu , or, type 2 and press enter to re-roll "))
            except ValueError:
                print("Invalid Choice!")
                input("Press enter to return to main menu")

            if choice == 1:
                newpassword = False
                mainmenu = True

# IF RE-ROLLING
            elif choice == 2:
                did_reroll = True
                generator = False
                newpassword = False

            else:
                print("Invalid Option!")
                generator = False
                newpassword = False
                did_reroll = True
                choice = int(input("Type 1 to return to main menu , or, type 2 and press enter to re-roll "))

# WHILE RE-ROLLING
        while did_reroll:
            print("Re-rolling....")
            regen()
            choice_sub = ""
            choice_sub = int(input("Type 1 to re-roll or type 2 to return to main menu "))

            if choice_sub == 1:
                newpassword = False
                regen()

            elif choice_sub == 2:
                did_reroll = False
                generator = False
                mainmenu = True

            else:
                #choice_sub != 1 or not(2 != choice_sub)
                print("Invalid option!")
                input("Press enter to re-roll")
                #did_reroll = True

did_consent = False
is_IDValid = False
has_ID = False

def getvault():
    os.path.exists('vaultkey.txt')
    if os.path.exists:
        print("Welcome back!")
    elif
    print("No vault key found! Create a new one?")

vault_choice = ""
input("Type Yes or "Y" to create a new key, or press type No or "N" to return to main menu:> ")

def answer

#MENU CHOICE 2

    if choice == 2:
        vault = True
        getvault()



    if choice == 4:
        quit()