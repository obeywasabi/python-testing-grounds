## MANTRA - Non-GUI Based, Alex Arias 10.27.2022

import requests
import urllib.request
import vault
import time
from rich.console import Console
from rich.align import Align
from rich import print
from rich.prompt import Confirm
from rich.table import Table
from rich.panel import Panel
from vault import *

currentVersion = '0.8.9-dev'
console = Console()

def get_update():
    URL = urllib.request.urlopen('https://raw.githubusercontent.com/obeywasabi/python-testing-grounds/main/python-stuff/Password%20Manager/version.txt')
    data = URL.read().decode('utf-8')

    if (data == currentVersion):
        console.print("[green]Up to date![/] :checkmark: ")
        quit()

    else:
        print("App is not up to date! You are on version " + currentVersion + " but you could be on version " + data + "!")
        choice = int(input("Do you want to update now? Press 1 for Yes and 2 for No: > "))
        if choice == 1:
            print("Downloading new version now, program will quit on its own, please delete OLD executable.")
            newVersion = requests.get("https://github.com/obeywasabi/python-testing-grounds/raw/main/python-stuff/Password%20Manager/PasswordManagerCLI.exe")
            with open("PasswordManager"+ data + ".exe", "wb") as push:
                push.write(newVersion.content)
                quit()

        if choice == 2:
            clear()
            quit()

        else:
            print("Invalid option!")
            quit()

console.print("[red]MANTRA Password Manager(CLI)[/] :key: by Alex A", style="bold", justify="center")
print()
console.print("[r][b]Press enter to continue[/]", justify="center")
input()


menu_prompts = [
    "[b]Select an option[/]\n"
    "\n(1) Generate a new password\n"
    "(2) Enter Vault\n"
    "(3) Check for updates\n"
    "(4) Quit"
]

vault_prompts = [
    "(1) View Passwords\n"
    "(2) Store new Passwords\n"
    "(3) Generate a new Storage key\n"
    "(4) Delete Entries\n"
    "(5) Return to Main Menu\n"
    "(6) Quit",

    "[b][red]A valid keyfile was not found, to access the vault securely, please create one.[/]\n\nPress [b][green]Enter[/] to generate a key",

]

choice_prompts = [
    "Return to main menu? Choosing 'No' will shuffle generated password again",
    "Press Y to return to main menu, or N to shuffle again",

]

newpass_prompts = [
    "[b][green]USAGE: \nFill in a few questions to generate a new password, realistically you can input anything "
    "into the lines, and the generator will still generate and shuffle all of your inputs. You can also choose to leave"
    " any of the sections blank to generate a shorter and or longer password.[/]\n",
    "[b][yellow][r]What is your name?: >[/] ",
    "[b][yellow][r]Type a favorite or rememberable number: >[/] ",
    "[b][yellow][r]Enter a favorite color(s) or any desired input: >[/] ",
    "[b][yellow][r]Enter a phrase or word you want to be included in the password: >[/] "

]

## Runtime Vars
menu_choice = ""
exist = os.path.exists("stub.ini")
does_manifest_exist = os.path.exists('manifest.obey')
does_stub_exist = exist ## Returns boolean value
main = True
key = False
menu_stage = 0

                                ## menu stages
                                # 0 = main menu
                                # 1 = newpassword stage
                                # 2 = shuffle stage
                                # 3 = UNASSIGNED
                                # 4 = UNASSIGNED
                                # 5 = vault stage

##--MAIN MENU STAGE--##
while main:
    clear()
    print(Panel.fit(menu_prompts[0], title="Main Menu", subtitle="v0.8.9-dev", padding=(2, 25)))
    
    menu_choice = int()
    
    try:
        menu_choice = int(console.input("[b][yellow][r]Choice: >[/] "))

    except ValueError:
        print("Invalid Option!")
        input("Press enter to continue")

    if menu_choice == 1:
        menu_stage = menu_stage + 1
        clear()

    elif menu_choice == 2:
        clear()
        menu_stage = menu_stage + 5

    elif menu_choice == 3:
        get_update()

    elif menu_choice == 4:
        quit()

    else:
        print("Not a valid choice! Press enter to continue")
        input()
        clear()

    # IF NEW PASSWORD, AND GENERATE
    while menu_stage == 1:
        print(Panel.fit(newpass_prompts[0], title="Generate a new password", padding=(2, 1)))
        vault.name = console.input(newpass_prompts[1])
        vault.fav_number = console.input(newpass_prompts[2])
        vault.color = console.input(newpass_prompts[3])
        vault.phrase = console.input(newpass_prompts[4])
        console.print("\n[b][green]Generating...[/]")
        time.sleep(0.5)
        gen()
        
        menu_choice = Confirm.ask(choice_prompts[0])
    

        if menu_choice:
            menu_stage = menu_stage - 1
            break

        elif menu_choice is not True:
            menu_stage = menu_stage + 1
            break



##---SHUFFLE STAGE---##
    while menu_stage == 2:
        clear()
        print("Shuffling....")
        gen()
        shuffle_sub = int()

        shuffle_sub = Confirm.ask(choice_prompts[1])


        if shuffle_sub:
            clear()
            menu_stage = menu_stage - 2

        elif shuffle_sub is not True:
            clear()
            gen()



##---VAULT MAIN MENU AND KEY CHECK---#

    while menu_stage == 5:

        if does_stub_exist:
            key = True

        else:
            clear()
            console.input(Panel(vault_prompts[1], title="Unauthorized Access!", padding=(2, 20)))
            key = True
            clear()
            gen_key()

        while key:
            clear()
            print(Panel(vault_prompts[0], title="Vault Menu", padding=(2, 25), box=box.ASCII_DOUBLE_HEAD, highlight=True, style="red"))

            try:
                vault_choice = int(console.input("[b][yellow][r]Choice: >[/] "))

            except ValueError:
                input("Invalid choice! Press enter to continue")
                break

            if vault_choice == 1:
                clear()
                b64_decode()
                
                pin_check = console.input("Enter your [b][red]pin[/] or [b][red]secret phrase[/]: > ")

                if pin_check == (vault.secretKey):
                    clear()
                    decrypt()
                    print()
                    input("\nPress enter to return to main menu..")

                else:
                    clear()
                    console.input(Panel.fit("[b][red]Input did not match the set pin/passphrase![/]\n\nPress enter to continue", title="Invalid Pin or Passphrase", padding=(2, 25)))
                    #input("Pin does not match the set pin! Press enter to continue")

            elif vault_choice == 2:
                clear()
                vault_add_Pass()
                print(Panel.fit("[b][green]Password successfully stored![/] Returning to vault menu...", box=box.ASCII))
                time.sleep(3)


            elif vault_choice == 3:
                os.remove('manifest.obey')
                os.remove('vault.key')
                os.remove('stub.ini')
                gen_key()


            elif vault_choice == 4:
                turnicate_entry()


            elif vault_choice == 5:
                clear()
                key = False
                menu_stage = menu_stage - 5
                break


            elif vault_choice == 6:
                quit()

            else:
                input("Not a valid option, press any key to return to main menu")
