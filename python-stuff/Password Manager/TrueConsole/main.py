## MANTRA - PasswordManager by Alex A - Nov 2022
## Written to look like a true console-only program

import curses
import npyscreen
from vault import *



import npyscreen
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()















#def main(stdscr):
    #stdscr.clear() ## Clears console
    #stdscr.addstr("Press 'ESC' to go back/quit")
    #stdscr.addstr(1, 0, "User 'ENTER' key to select choice")
    #win = curses.newwin(100, 100, 13, 40) ## (HEIGHT, WIDTH, ROW(u/d), COLUMN(l/r)) (YES Y CORDINATES FIRST FOR SOME REASON)
    #curses.textpad.rectangle(win, 0, 0, 2, 2)
    #box = Textbox(win)
    #pad.addstr("MANTRA Password Manager", curses.A_BOLD)
    #rectangle(stdscr, 10, 10, 25, 40)
    #stdscr.refresh()
    #stdscr.addstr(15, 45, "by Alex Arias", curses.A_BOLD)
    #stdscr.addstr(20, 45, "Press any key to continue...", curses.A_STANDOUT)
    #stdscr.getch()
    #curses.beep()
    #stdscr.clear()


    #stdscr.refresh()    ## Refreshes the current screen
    #stdscr.getch()      ## Waits for any keypress and gives us the ordinal value of what was typed in

#wrapper(main)
