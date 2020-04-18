from Cell import Cell
import numpy as np
import random as rd

class MazeGenerator:
    def __init__(self,maze_len):
        self._maze_len = maze_len
        self.maze = np.ones((self._maze_len[0],self._maze_len[1]))
        self.visitedList = []
        self.cell_start = Cell([0,0],[0,1,1,1,1])
        self.cell_goal = Cell([(self._maze_len[1]-1)/2 -1,(self._maze_len[0] - 1)/2 -1])

    def checkVisited(self,coordinate):
        visited = False
        for cell in self.visitedList:
            if cell.coord == coordinate:
                visited = True
                break
        return visited

    def transfToList(self):
        mazeTxt = open("mazeTxt.txt",'w')
        for x in range(self._maze_len[0]):
            for y in range(self._maze_len[1]):
                if self.maze[x][y] == 0:
                    mazeTxt.write("0-")
                else:
                    mazeTxt.write("1-")
            mazeTxt.write("\n")

    def findNeighbor(self,cell_current):
        coorX = cell_current.coord[0]
        coorY = cell_current.coord[1]
        neighbor = []

        if self.checkVisited([coorX+1,coorY]) == False and coorX+1 < (self._maze_len[0] - 1)/2 :
            neighbor.append( Cell([coorX+1,coorY],[1,1,0,1]) )
        if self.checkVisited([coorX-1,coorY]) == False and coorX-1 >= 0 :
            neighbor.append( Cell([coorX-1,coorY],[1,1,1,0]) )
        if self.checkVisited([coorX,coorY+1]) == False and coorY+1 < (self._maze_len[0] - 1)/2 :
            neighbor.append( Cell([coorX,coorY+1],[0,1,1,1]) )
        if self.checkVisited([coorX,coorY-1]) == False and coorY-1  >= 0:
            neighbor.append( Cell([coorX,coorY-1],[1,0,1,1]) ) 

        if len(neighbor) == 0:
            return None
        else:
            index = rd.randint(0,len(neighbor)-1)
            return neighbor[index] 

    def changeWall(self, cell_current):
        coorX = cell_current.coord[0]
        coorY = cell_current.coord[1]

        if cell_current.wall[0] == 0:
            self.maze[2*coorY][2*coorX+1] = 0
        if cell_current.wall[1] == 0:
            self.maze[2*coorY+2][2*coorX+1] = 0
        if cell_current.wall[2] == 0:
            self.maze[2*coorY+1][2*coorX] = 0
        if cell_current.wall[3] == 0:
            self.maze[2*coorY+1][2*coorX+2] = 0
        
        self.maze[2*coorX+1][2*coorY+1] = 0

 
    def construct(self, cell_current = None):

        if cell_current == None:
            cell_current = self.cell_start

        if cell_current.coord == self.cell_goal.coord:
            cell_current.wall[1] = 0

        self.changeWall(cell_current)
           
        if self.checkVisited(cell_current.coord) == False:
            self.visitedList.append(cell_current)


        neighbor = self.findNeighbor(cell_current)
        
        if neighbor == None and (cell_current.coord != self.visitedList[0].coord):
            self.construct(cell_current.parent)
        
        elif neighbor == None and (cell_current.coord == self.visitedList[0].coord):
            self.transfToList()
            return self.maze

        else:
            neighbor.parent = cell_current
            self.construct(neighbor)







    
    
