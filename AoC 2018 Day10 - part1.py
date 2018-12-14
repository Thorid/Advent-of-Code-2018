def parseFilePosition(file):
    fileArray = open(file).read().split('\n')
    parsedInput = []
    for i in range(len(fileArray)):
        tempArray = []
        first = fileArray[i][fileArray[i].find('position=<')+10:fileArray[i].find(', ')]
        second = fileArray[i][fileArray[i].find(', ')+2:fileArray[i].find('> ')]
        tempArray.append(int(first))
        tempArray.append(int(second))
        parsedInput.append(tempArray)
    return parsedInput

def parseFileVelocity(file):
    fileArray = open(file).read().split('\n')
    parsedInput = []
    for i in range(len(fileArray)):
        tempArray = []
        first = fileArray[i][fileArray[i].find('velocity=<')+10:fileArray[i].rfind(', ')]
        second = fileArray[i][fileArray[i].rfind(', ')+2:fileArray[i].rfind('>')]
        tempArray.append(int(first))
        tempArray.append(int(second))
        parsedInput.append(tempArray)
    return parsedInput

def printPoints(minX,minY,maxX,maxY,positionArray):
    for i in range(minY,maxY):
        line = ''
        for j in range(minX,maxX):
            currentPoint = [j,i]
            if currentPoint in positionArray:
                line += '#'
            else:
                line += '.'
        print(line)

def changePosition(positionArray,velocityArray):
    for i in range(len(positionArray)):
        positionArray[i][0] += velocityArray[i][0]
        positionArray[i][1] += velocityArray[i][1]
    return positionArray

positionArray = parseFilePosition('AoC 2018 Day 10 - input.txt')
velocityArray = parseFileVelocity('AoC 2018 Day 10 - input.txt')
while True:
    positionArray = changePosition(positionArray,velocityArray)
    nearOthers = 0
    for i in range(len(positionArray)):
        x = positionArray[i][0]
        y = positionArray[i][1]
        if [x,y+1] in positionArray or [x+1,y+1] in positionArray or [x+1,y] in positionArray or [x+1,y-1] in positionArray or [x,y-1] in positionArray or [x-1,y-1] in positionArray or [x-1,y] in positionArray or [x-1,y+1] in positionArray:
            nearOthers += 1
    if nearOthers == len(positionArray):
        break
printPoints(x-45,y-15,x+45,y+15,positionArray)
