from pygame.locals import *
import pygame
from txtToMatrix import txtToMatrix
from txtToMatrix import txtToMatrix

class Maze:
    def __init__(self,maze):

        self.maze = maze

        self.squareSize = 20

        self.columns = len(self.maze[0])
        self.rows = len(self.maze)

        self.windowWidth  = len(self.maze[0])*self.squareSize
        self.windowHeight = len(self.maze)*self.squareSize
                        
        self.screen = self.createScreen()

    def createScreen(self):
        pygame.init()
        screen = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        screen.fill((255,255,255))
        return screen
        
    def draw(self, path, result):

        background = pygame.Surface((self.windowWidth,self.windowHeight))
        background.fill((0,0,0))
        for row in range(self.rows):
            for column in range(self.columns):
                if self.maze[ row ][column] == 0:
                    pygame.draw.rect(background,(255,255,255),(column*self.squareSize,row*self.squareSize,self.squareSize,self.squareSize))

        if result == True:
            for coor in path:
                pygame.draw.rect(background,(255,0,0),(coor[1]*self.squareSize,coor[0]*self.squareSize,self.squareSize,self.squareSize))
        
        self.screen.blit(background,(0,0))

        #### Update the the display and wait ####
        pygame.display.flip()
        pygame.image.save(self.screen,"maze.png")
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        #### Update the the display and wait ####

        pygame.quit()

     

