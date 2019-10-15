
def makeRoomsInMaze(mArray):
    for x in range(len(mArray)):
        if x > 0 and x < len(mArray)-1 and x%2==1:
            for y in range(len(mArray[x])):
                if y > 0 and y < len(mArray[x])-1 and y%2==1:
                    mArray[x][y] = 0
    return mArray

def makeAmazingMazes(sizeX,sizeY):
    sizeX = sizeX*2+1
    sizeY = sizeY*2+1
    mazeArray = [[1 for x in range(sizeX)] for y in range(sizeY)]
    mazeArray = makeRoomsInMaze(mazeArray)
    for x in mazeArray:
        line = ""
        for y in x:
            line += str(y)+" "
        print(line)



makeAmazingMazes(4,4)
