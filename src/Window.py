from tkinter import *


class Window:

    def __init__(self, damier):
        self.damier = damier
        self.padding=10
        self.window_width = damier.numberOfColumn * damier.witdthofacell
        self.window_height = damier.numberOfLine * damier.witdthofacell

        self.fen1 = Tk()
        self.can1 = Canvas(self.fen1, width=self.window_width + self.padding, height=self.window_height + self.padding,
                      bg='white')
        self.bindcanevent()
        self.createthewindow()
        print(damier.cells)

    def createthewindow(self):

        self.can1.pack(side=TOP, padx=5, pady=5)

        b1 = Button(self.fen1, text='Go!')
        b2 = Button(self.fen1, text='Stop')
        b1.pack(side=LEFT, padx=3, pady=3)
        b2.pack(side=LEFT, padx=3, pady=3)
        b3 = Button(self.fen1, text='Canon planeur')
        b3.pack(side=LEFT, padx=3, pady=3)

        entree = Entry(self.fen1)
        entree.pack(side=RIGHT)
        chaine = Label(self.fen1)
        chaine.configure(text="Attente entre chaque Ã©tape (ms) :")
        chaine.pack(side=RIGHT)

        self.drawthelines(self.can1, self.damier.witdthofacell, self.damier.numberOfLine, self.damier.numberOfColumn)

        self.fen1.mainloop()

    def drawthelines(self, can1, widthofacell, numberOfLine, numberOfColumn):

        c_x = 0
        c_y = 0
        paddingforline=self.padding/2

        while c_x != numberOfColumn+1:
            can1.create_line(c_x * widthofacell + paddingforline, paddingforline, c_x * widthofacell + paddingforline, self.window_height + paddingforline, width=1, fill='black')
            c_x += 1

        while c_y != numberOfLine+1:
            can1.create_line(paddingforline, c_y * widthofacell + paddingforline, self.window_width + paddingforline, c_y * widthofacell + paddingforline, width=1, fill='black')
            c_y += 1

    def click_gauche(self, event):  # fonction rendant vivante la cellule cliquÃ©e donc met la valeur 1 pour la cellule cliquÃ©e au dico_case
        x = event.x - ((event.x-self.padding/2) % self.damier.witdthofacell)
        y = event.y- ((event.y-self.padding/2) % self.damier.witdthofacell)
        print("event", event.x-self.padding/2,event.y-self.padding/2)
        print(x,y)
        self.can1.create_rectangle(x, y, x + self.damier.witdthofacell, y + self.damier.witdthofacell, fill='black')

    def bindcanevent(self):
        self.can1.bind("<B1-Motion>", self.click_gauche)


