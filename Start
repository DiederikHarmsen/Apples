#Imports
from tkinter import *
from tkinter import ttk
import os, sqlite3

imagepath = "c:/Users/diede/Documents/Python Scripts/Apples/Images/"

#Key down function

def addTree():
    AppleSort = textentry.get()
    print(AppleSort)
    #Put applesort into database

#A drag and drop system. 

#Window specification:
window = Tk()
window.title("Hof te Apples")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
window.configure(bg="#dce6d8")



#The icons
AppleIcon = PhotoImage(file= os.path.join(imagepath, "Apple.png"))
PearIcon = PhotoImage(file= os.path.join(imagepath, "Pear.png"))
Label (window, image=AppleIcon).grid(row=0, column = 0, sticky = W)
Label (window, image=PearIcon).grid(row=0, column = 0, sticky = W)


#create label
Label(window, text = "Enter the word you would like a definition for", font = "none 12 bold").grid(row=1, column = 0, sticky = W)


#create a text entry box
textentry = Entry(window, width=20)
textentry.grid(row=2, column=0, sticky = W)
#add a submit button
Button (window, text="SUBMIT", width = 6, command=addTree).grid(row=3, column=0, sticky=W)


#create another label
Label (window, text="\nDefinition:", font="none 12 bold").grid(row = 4, column = 0, sticky = W)

#create a text box
output = Text( window, width = 75, height = 6, wrap= WORD, background = "white")
output.grid(row=5, column = 0, columnspan= 2, sticky=W)


#the dictionary
my_compdictionary = {
    'algorithm:': 'Step by step instructions to complete a task', 'bug': 'piece of code that causes a program to fail'
}







#Run the main loop
window.mainloop()









