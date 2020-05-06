import pygame
import numpy as np

def createScreen(windowWidth,windowHeight):
    pygame.init()
    screen = pygame.display.set_mode((windowWidth,windowHeight))
    screen.fill((255,255,255))
    return screen

def transfToList(maze):
    mazeTxt = open("myMaze.txt",'w')
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 0:
                mazeTxt.write("0-")
            elif maze[x][y] == 1:
                mazeTxt.write("1-")
            elif maze[x][y] == 2:
                mazeTxt.write("2-")
            else:
                mazeTxt.write("3-")
        mazeTxt.write("\n")

def SetMaze(maze,coordinates,squareSize,element):
    coord = [int(coordinates[0]/squareSize),int(coordinates[1]/squareSize)]
    if element == 'wall':
        maze[coord[1]][coord[0]] = 1
    elif element == 'way':
        maze[coord[1]][coord[0]] = 0
    elif element == 'start_node':
        maze[coord[1]][coord[0]] = 2
    elif element == 'goal_node':
        maze[coord[1]][coord[0]] = 3

    return maze

def UpdateDrawing(screen,background,coordinates,squareSize,element):
    coord = [int(coordinates[0]/squareSize),int(coordinates[1]/squareSize)]
    if element == 'wall':
        pygame.draw.rect(background,(0,0,0),(coord[0]*squareSize,coord[1]*squareSize,squareSize,squareSize))
    elif element == 'way':
        ##Drawing sqare
        pygame.draw.rect(background,(255,255,255),(coord[0]*squareSize,coord[1]*squareSize,squareSize,squareSize))
        ##Drawing lines around
        pygame.draw.line(background, (0,0,0), [coord[0]*squareSize,coord[1]*squareSize], [coord[0]*squareSize + squareSize , coord[1]*squareSize], 1)
        pygame.draw.line(background, (0,0,0), [coord[0]*squareSize,coord[1]*squareSize], [coord[0]*squareSize , coord[1]*squareSize + squareSize], 1)
        pygame.draw.line(background, (0,0,0), [coord[0]*squareSize + squareSize , coord[1]*squareSize], [coord[0]*squareSize + squareSize , coord[1]*squareSize + squareSize], 1)
        pygame.draw.line(background, (0,0,0), [coord[0]*squareSize , coord[1]*squareSize + squareSize], [coord[0]*squareSize + squareSize , coord[1]*squareSize + squareSize], 1)
    elif element == 'start_node':
        ##Drawing sqare
        pygame.draw.rect(background,(0,0,255),(coord[0]*squareSize,coord[1]*squareSize,squareSize,squareSize))
    elif element == 'goal_node':
        ##Drawing sqare
        pygame.draw.rect(background,(0,255,0),(coord[0]*squareSize,coord[1]*squareSize,squareSize,squareSize))

    screen.blit(background,(0,0))
    pygame.display.flip()

def drawing(x_Axis,y_Axis):

    maze = np.zeros([x_Axis,y_Axis])

    squareSize = 20

    windowWidth = squareSize*x_Axis
    windowHeight = squareSize*y_Axis

    screen = createScreen(windowWidth,windowHeight)

    background = pygame.Surface((windowWidth,windowHeight))
    background.fill((255,255,255))
    for row in range(x_Axis):
        for column in range(y_Axis):
            if row == 0 or column == 0 or row == x_Axis-1 or column == y_Axis-1:
                pygame.draw.rect(background,(0,0,0),(column*squareSize,row*squareSize,squareSize,squareSize))
                maze = SetMaze(maze,[row*squareSize,column*squareSize],squareSize,'wall')

    for row in range(x_Axis):
        if row != 0 and row != x_Axis-1:
            pygame.draw.line(background, (0,0,0), [0,squareSize*row], [windowWidth,squareSize*row], 1)

    for column in range(y_Axis):
        if column != 0 and column != y_Axis-1: 
            pygame.draw.line(background, (0,0,0), [squareSize*column,0], [squareSize*column,windowHeight], 1)

    screen.blit(background,(0,0))

    pygame.display.flip()

    done_option = False

    while not done_option:
        element = input("Choose the option(wall/way/start_node/goal_node/quit):")
        if element == 'quit':
            done_draw = True
            done_option = True
        elif element == 'wall' or element == 'way':
            done_draw = False
            while not done_draw:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done_option = True
                        done_draw = True
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        side = pygame.mouse.get_pressed()[0]
                        if side == 1:
                            coordinates = pygame.mouse.get_pos()
                            print(coordinates)
                            maze = SetMaze(maze,coordinates,squareSize,element)
                            UpdateDrawing(screen,background,coordinates,squareSize,element)
                            break
                        else:
                            done_draw = True
                            break
        elif element == 'start_node' or element == 'goal_node':
            done_draw = False
            while not done_draw:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done_option = True
                        done_draw = True
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        side = pygame.mouse.get_pressed()[0]
                        if side == 1:
                            coordinates = pygame.mouse.get_pos()
                            print(coordinates)
                            maze = SetMaze(maze,coordinates,squareSize,element)
                            UpdateDrawing(screen,background,coordinates,squareSize,element)
                            done_draw = True
                            break
                        else:
                            done_draw = True
                            break
        else:
            print("This option not exist! Choose another.")

    pygame.image.save(screen,"maze.png")
    pygame.quit()
    return maze

def main():
    windowWidth = input("Choose the width of the window (must be odd):")
    windowHeight = input("Choose the heigth of the window (must be odd):")
    print("-----------------------------------------------------------------")
    retorno = drawing(int(windowWidth),int(windowHeight))
    transfToList(retorno)

main()