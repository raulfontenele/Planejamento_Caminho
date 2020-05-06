from Node import Node
from PathPlanning import PathPlanning
from txtToMatrix import txtToMatrix
from MazeGenerator import MazeGenerator
from Maze import Maze


def main():
    lenX = 101
    lenY = 101

    _maze = MazeGenerator([lenX,lenY])
    _maze.constructNotRecursion()
    maze = txtToMatrix("mazeTxt.txt")
    
    node_start = Node([0,1])
    node_start.gcost = 0

    node_goal = Node([lenX-1,lenY-2])

    path = PathPlanning(maze,node_start,node_goal)
    route = path.DepthFirstSearch()

    desenho = Maze(txtToMatrix("mazeTxt.txt"))
    desenho.draw(route,False)


    
main()