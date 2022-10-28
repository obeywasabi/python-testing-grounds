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
    choice = int(input("> "))

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
            phrase = input("Type a phrase you'd like to be included in your password, something you will always remember ")
            print("Generating....")
            print()
            regen()
            print()
            choice = int(input("Type 1 to return to main menu , or, type 2 and press enter to re-roll "))

            if choice == 1:
                newpassword = False
                mainmenu = True
# IF RE-ROLLING
            elif choice == 2:
                did_reroll = True
                generator = False
                newpassword = False
            else:
                if choice > 2 or choice < 1:
                    print("Invalid Option!")
                choice = int(input("Type 1 to return to main menu , or, type 2 and press enter to re-roll "))
                generator = False
                newpassword = False
                did_reroll = True

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
                choice_sub < 1 or choice_sub > 2
                print("Invalid option!")
                choice_sub = input("Press enter to continue")
                did_reroll = True

#MENU CHOICE 2

    if choice == 4:
        quit()