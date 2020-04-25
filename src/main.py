from src.Damier import Damier
from src.Rule import Rule
from src.Window import Window
from tkinter import *



def goToPlay():
    witdthofacell = 5
    numberOfLine = 100
    numberOfColumn = 100

    mondamier = Damier(witdthofacell, numberOfLine, numberOfColumn)
    regles = Rule('classic')
    myWindow = Window(mondamier, regles)

mainWindow=Tk()

b3 = Button(mainWindow, text='Go', command=goToPlay)
b3.pack(side=LEFT, padx=3, pady=3)

mainWindow.mainloop()
