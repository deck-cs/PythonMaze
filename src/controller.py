def makeAmazingMazes(sizeX,sizeY):
    mazeArray = [[1]*sizeX]*sizeY
    for x in range(len(mazeArray)):
        line = ""
        for y in range(len(mazeArray[x])):
            line += str(mazeArray[x][y])+" "
        print(line)

    

makeAmazingMazes(8,6)
