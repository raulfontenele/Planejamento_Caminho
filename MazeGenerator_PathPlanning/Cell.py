class Cell:
    def __init__(self,coord,wall = [1,1,1,1],parent = None):
        self.coord = coord
        self.wall = wall #up-down-left-right
        self.parent = parent
        