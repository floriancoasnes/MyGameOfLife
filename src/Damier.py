from tkinter import *
import numpy as np

class Damier:

    def __init__(self,witdthofacell, numberOfLine, numberOfColumn,):
        self.witdthofacell= witdthofacell
        self.numberOfLine=numberOfLine
        self.numberOfColumn=numberOfColumn
        self.cells=np.zeros((numberOfLine, numberOfColumn))

