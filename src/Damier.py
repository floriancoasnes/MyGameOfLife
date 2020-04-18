from tkinter import *
import numpy as np
import array as arr

class Damier:

    def __init__(self,witdthofacell, numberOfLine, numberOfColumn,):
        self.witdthofacell= witdthofacell
        self.numberOfLine=numberOfLine
        self.numberOfColumn=numberOfColumn
        self.cells=np.zeros((numberOfColumn, numberOfLine))
        self.coordalivecell=[]

