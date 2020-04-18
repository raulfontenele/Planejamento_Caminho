def txtToMatrix(txtFile):

    maze = []

    arquivo = open(txtFile,'r')

    for line in arquivo.read().split():
        d = list(map(int, line.split("-")[0:len(line.split("-")) - 1])) 
        maze.append(d)

    return maze

