## MANTRA GUI Edition by Alex Arias
## EPOCH = Fri Nov 25th 3:15 AM

from vault import *
from tkinter import *

version = '0.1-dev'

intro = ["\nThank you for using my program, this program can safely be used\n"
"to store any or all your passwords, it uses AES/264-Bit Encryption using the\n"
"Fernet API. I am still a new dev learning the ropes so any bugs you encounter\n"
"please report them to my Github <obeywasabi>."


]

root = Tk() ## Main loop function
root.geometry("300x300")
root.title("MANTRA")

def continued():
    pass ## Clear screen
    ## Next window



welcome = Label(root, text=f"MANTRA Password Manager\nby Alex Arias\n{intro}", wraplength=290, relief=SUNKEN, bd=3)
welcome.grid(row=5, column=5, padx= 2, pady= 59) ## Adds padding around the label

accept = Button(root, text="Continue", command=continued)

#welcome.grid(row=0, column=0) 
#welcome1.grid(row=1, column=0)
accept.grid(row=50, column=5, pady = 10)

root.mainloop()
