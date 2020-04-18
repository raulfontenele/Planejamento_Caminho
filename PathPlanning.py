from Node import Node

class PathPlanning:

    def __init__(self, maze , node_start, node_goal):
        self.map = maze
        self.node_start = node_start
        self.node_goal = node_goal
        self.openList = []
        self.closeList = []

    def calculateHCost(self,node_current):
        h = abs(node_current.coord[0] - self.node_goal.coord[0]) + abs(node_current.coord[1] - self.node_goal.coord[1])
        return h

    def checkOpenList(self,node_current):
        for node in self.openList:
            if node.coord == node_current.coord:
                return True

        return False

    def checkCloseList(self,node_current):
        for node in self.closeList:
            if node.coord == node_current.coord:
                return True

        return False
    
    def findNeighborhood(self,node_current):
        neighbor = []
        coorX = node_current.coord[0]
        coorY = node_current.coord[1]
        
        if self.map[coorX + 1][coorY] != 1:
            neighbor.append( Node([coorX + 1,coorY]) )
        if self.map[coorX - 1][coorY] != 1 and coorX - 1 > 0:
            neighbor.append( Node([coorX - 1,coorY]) )
        if self.map[coorX ][coorY + 1] != 1:
            neighbor.append( Node([coorX,coorY + 1]) )    
        if self.map[coorX ][coorY - 1] != 1 and coorY - 1 > 0:
            neighbor.append( Node([coorX,coorY - 1]) ) 

        return neighbor


    def AStarAlgorithm(self):

        self.openList.append(self.node_start)

        while True:
            self.openList = sorted(self.openList,key=Node.getFcode)
            node_current = self.openList[0]
            self.closeList.append(self.openList[0])
            self.openList.pop(0)

            if node_current.coord == self.node_goal.coord:
                break
        
            neighborhood = self.findNeighborhood(node_current)

            for neighbor in neighborhood:
                if self.checkCloseList(neighbor):
                    continue
                elif self.checkOpenList(neighbor) == False:
                    neighbor.parent = node_current
                    neighbor.hcost = self.calculateHCost(neighbor)
                    neighbor.calculateGCost()
                    neighbor.calculateFCost()
                    self.openList.append(neighbor)
                elif self.checkOpenList(neighbor) :
                    neighbor = [node for node in self.openList if node.coord == neighbor.coord][0]
                    if ( node_current.gcost + 10 < neighbor.gcost ):                      
                        neighbor.parent = node_current
                        neighbor.calculateGCost()
                        neighbor.calculateFCost()

            if len(self.openList) == 0:
                print("deu merda")
                break

        route = []

        ## Mostrar a rota
        while node_current != None:
            route.append(node_current.coord)
            print(node_current.coord)
            node_current = node_current.parent

        return route