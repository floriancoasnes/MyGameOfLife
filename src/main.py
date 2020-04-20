from src.Damier import Damier
from src.Rule import Rule
from src.Window import Window

witdthofacell=30
numberOfLine=10
numberOfColumn=20

mondamier=Damier(witdthofacell, numberOfLine, numberOfColumn)
regles=Rule('classic')
myWindow=Window(mondamier,regles)