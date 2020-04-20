from tkinter import *
import numpy as np

from src.Damier import Damier


class Window:

    def __init__(self, damier,regles):
        self.flag = 0
        self.vitesse=50
        self.damier = damier
        self.padding=10
        self.window_width = damier.numberOfColumn * damier.witdthofacell
        self.window_height = damier.numberOfLine * damier.witdthofacell

        self.rules=regles
        self.fen1 = Tk()
        self.can1 = Canvas(self.fen1, width=self.window_width + self.padding, height=self.window_height + self.padding,
                      bg='white')

        self.createthewindow()

    def createthewindow(self):

        self.can1.pack(side=TOP, padx=5, pady=5)

        b1 = Button(self.fen1, text='Go!', command=self.go)
        b2 = Button(self.fen1, text='Stop', command=self.stop)
        b1.pack(side=LEFT, padx=3, pady=3)
        b2.pack(side=LEFT, padx=3, pady=3)
        b3 = Button(self.fen1, text='step >', command=self.stepByStep)
        b3.pack(side=LEFT, padx=3, pady=3)
        b4 = Button(self.fen1, text='Reset', command=self.reset)
        b4.pack(side=LEFT, padx=3, pady=3)

        entree = Entry(self.fen1)
        entree.pack(side=RIGHT)
        chaine = Label(self.fen1)
        chaine.configure(text="Attente entre chaque Ã©tape (ms) :")
        chaine.pack(side=RIGHT)

        self.drawthelines(self.can1, self.damier.witdthofacell, self.damier.numberOfLine, self.damier.numberOfColumn)

        self.bindcanevent()
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
        coordx=int((x-self.padding/2) / self.damier.witdthofacell)
        coordy=int((y-self.padding/2) / self.damier.witdthofacell)
        if(coordx>=0 and coordy>=0 and coordx<self.damier.numberOfLine and coordy<self.damier.numberOfColumn):
            self.damier.cells[coordy][coordx]=1
            self.can1.create_rectangle(x, y, x + self.damier.witdthofacell, y + self.damier.witdthofacell, fill='black')

    def click_droit(self,
                     event):  # fonction rendant vivante la cellule cliquÃ©e donc met la valeur 1 pour la cellule cliquÃ©e au dico_case
        x = event.x - ((event.x - self.padding / 2) % self.damier.witdthofacell)
        y = event.y - ((event.y - self.padding / 2) % self.damier.witdthofacell)
        coordx = int((x - self.padding / 2) / self.damier.witdthofacell)
        coordy = int((y - self.padding / 2) / self.damier.witdthofacell)

        self.damier.cells[coordy][coordx] = 0
        self.can1.create_rectangle(x, y, x + self.damier.witdthofacell, y + self.damier.witdthofacell, fill='white')

    def bindcanevent(self):
        self.can1.bind("<B1-Motion>", self.click_gauche)
        self.can1.bind("<Button-1>", self.click_gauche)

        self.can1.bind("<B3-Motion>", self.click_droit)
        self.can1.bind("<Button-3>", self.click_droit)

        self.can1.bind()



    def drawcell(self, color, coordx,coordy):
        x=(self.damier.witdthofacell*(coordx)+self.padding/2)
        y=(self.damier.witdthofacell*(coordy)+self.padding/2)


        if (color==0):
            self.can1.create_rectangle(x, y, x + self.damier.witdthofacell, y + self.damier.witdthofacell, fill='white')
        elif (color==1):
            self.can1.create_rectangle(x, y, x + self.damier.witdthofacell, y + self.damier.witdthofacell, fill='black')

        del x,y,coordx,coordy,color

    def go(self):
        if self.flag == 0:
            self.flag = 1
            self.play()

    def stop(self):
        self.flag=0

    def stepByStep(self):
        self.flag=1
        self.playByStep()

    def reset(self):
        self.damier=Damier(self.damier.witdthofacell, self.damier.numberOfLine, self.damier.numberOfColumn)
        v = 0
        while v != self.damier.numberOfColumn:
            w = 0
            while w != self.damier.numberOfLine:
                self.drawcell(self.damier.cells[w][v], v, w)
                w+=1
            v += 1

        del v
        del w
        self.flag=0


    def play(self):  # fonction comptant le nombre de cellules vivantes autour de chaque cellule
        self.can1.delete(ALL)
        v = 0
        while v != self.damier.numberOfColumn:
            w = 0
            while w != self.damier.numberOfLine:
                self.rules.ruledecision(self.damier, v, w)
                self.drawcell(self.damier.cells[w][v], v, w)
                w += 1
            v += 1

        self.damier.cells=self.damier.nextcells
        self.damier.setToZerosNextCells()

        del v
        del w

        if self.flag > 0:
            self.fen1.after(self.vitesse, self.play)
            self.flag+=1


    def playByStep(self):
        v = 0
        while v != self.damier.numberOfColumn:
            w = 0
            while w != self.damier.numberOfLine:
                self.rules.ruledecision(self.damier, v, w)
                self.drawcell(self.damier.cells[w][v], v, w)
                w += 1
            v += 1

        del v
        del w

        self.damier.cells = self.damier.nextcells
        self.damier.setToZerosNextCells()

        self.flag+=1


