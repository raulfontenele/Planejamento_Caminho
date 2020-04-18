from Node import Node
from PathPlanning import PathPlanning
from txtToMatrix import txtToMatrix
from MazeGenerator import MazeGenerator
from Maze import Maze


def main():

    _maze = MazeGenerator([31,31])
    _maze.construct()
    maze = txtToMatrix("mazeTxt.txt")
    
    node_start = Node([0,1])
    node_start.gcost = 0

    node_goal = Node([30,29])

    path = PathPlanning(maze,node_start,node_goal)
    route = path.AStarAlgorithm()

    desenho = Maze(txtToMatrix("mazeTxt.txt"))
    desenho.draw(route)


    
main()