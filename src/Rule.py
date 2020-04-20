class Rule:

    def __init__(self,type):
        self.type=type

    def classicRule(self, damier, positioninit):

        x = positioninit[1]
        y = positioninit[0]

        if (x == 0 and y == 0):
            numberofclosealivecell = damier.cells[x + 1][y] + damier.cells[x][y + 1] + damier.cells[x + 1][y + 1]

        elif (x == damier.numberOfLine - 1 and y == 0):
            numberofclosealivecell = damier.cells[x - 1][y] + damier.cells[x][y + 1] + damier.cells[x - 1][y + 1]

        elif (x == 0 and y == damier.numberOfColumn - 1):
            numberofclosealivecell = damier.cells[x][y - 1] + damier.cells[x + 1][y] + damier.cells[x + 1][y - 1]

        elif (x == damier.numberOfLine - 1 and y == damier.numberOfColumn - 1):
            numberofclosealivecell = damier.cells[x - 1][y - 1] + damier.cells[x][y - 1] + damier.cells[x - 1][y]

        elif (y == 0):
            numberofclosealivecell = damier.cells[x + 1][y] + damier.cells[x][y + 1] + damier.cells[x + 1][y + 1] + \
                                     damier.cells[x - 1][y + 1] + damier.cells[x - 1][y]

        elif (x == 0):
            numberofclosealivecell = damier.cells[x + 1][y] + damier.cells[x][y + 1] + damier.cells[x + 1][y + 1] + \
                                     damier.cells[x][y - 1] + damier.cells[x + 1][y - 1]

        elif (y == damier.numberOfColumn - 1):
            numberofclosealivecell = damier.cells[x - 1][y - 1] + damier.cells[x][y - 1] + damier.cells[x - 1][y] + \
                                     damier.cells[x + 1][y] + damier.cells[x + 1][y - 1]


        elif (x == damier.numberOfLine - 1):
            numberofclosealivecell = damier.cells[x - 1][y] + damier.cells[x][y + 1] + damier.cells[x - 1][y + 1] + \
                                     damier.cells[x][y - 1] + damier.cells[x - 1][y - 1]
        else:
            numberofclosealivecell = damier.cells[x - 1][y - 1] + damier.cells[x][y - 1] + damier.cells[x - 1][y] + \
                                     damier.cells[x + 1][y] + damier.cells[x + 1][y - 1] + damier.cells[x - 1][y + 1] + \
                                     damier.cells[x][y + 1] + damier.cells[x + 1][y + 1]
        del x
        del y
        del positioninit
        return numberofclosealivecell

    def ruledecision(self,damier,x,y):
        numberofclosecell=self.classicRule(damier,[x,y])
        if ((numberofclosecell==3) and (damier.cells[y][x]==0)):
            damier.nextcells[y][x]=1
        elif ((numberofclosecell!=3) and (numberofclosecell!=2) and (damier.cells[y][x]==1)):
            damier.nextcells[y][x]=0
        else:
            damier.nextcells[y][x]=damier.cells[y][x]

        del numberofclosecell
        del x
        del y



