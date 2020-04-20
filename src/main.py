from src.Damier import Damier
from src.Rule import Rule
from src.Window import Window

witdthofacell=10
numberOfLine=40
numberOfColumn=40

mondamier=Damier(witdthofacell, numberOfLine, numberOfColumn)
regles=Rule('classic')
myWindow=Window(mondamier,regles)