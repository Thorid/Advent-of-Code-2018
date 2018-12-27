def parseInput(file):
    fileArray = open(file).read().replace(', ','\n').split('\n')
    clayCoordinates = set()
    while fileArray != []:
        for i in range(2):
            if 'x' in fileArray[i] and '.' not in fileArray[i]:
                x = fileArray[i].replace('x=','')
                x = int(x)
            elif 'y' in fileArray[i] and '.' not in fileArray[i]:
                y = fileArray[i].replace('y=','')
                y = int(y)
            elif 'x' in fileArray[i] and '.' in fileArray[i]:
                tempArray = fileArray[i].replace('x=','').split('..')
                for x in range(int(tempArray[0]),int(tempArray[1]) + 1):
                    clayCoordinates.add((int(x), y))
            elif 'y' in fileArray[i] and '.' in fileArray[i]:
                tempArray = fileArray[i].replace('y=','').split('..')
                for y in range(int(tempArray[0]),int(tempArray[1]) + 1):
                    clayCoordinates.add((x, int(y)))
        del fileArray[0]
        del fileArray[0]
    return clayCoordinates

def getYBorders(clayCoordinates):
    minY = 999999
    maxY = 0
    for coordinate in clayCoordinates:
        if coordinate[1] < minY:
            minY = coordinate[1]
        if coordinate[1] > maxY:
            maxY = coordinate[1]
    return minY, maxY

def waterFlow(spring, clayCoordinates, minY, maxY):
    currentPositions = [spring]
    waterFlowArray = set()
    waterStandArray = set()
    overMaxPositions = 0
    while overMaxPositions < 50: 
        newCurrentPositions = []
        for i in range(len(currentPositions)):
            x = currentPositions[i][0]
            y = currentPositions[i][1]
            if (x,y+1) not in clayCoordinates and (x,y+1) not in waterStandArray and y+1 <= maxY+1:
                newCurrentPositions.append((x,y+1))
                waterFlowArray.add(tuple(currentPositions[i]))
            elif y+1 > maxY+1:
                overMaxPositions += 1
            else:
                tempWaterStandArray = []
                leaking = False
                while (x,y) not in clayCoordinates:
                    if (x,y+1) in clayCoordinates or (x,y+1) in waterStandArray:
                        tempWaterStandArray.append((x,y))
                        x -= 1
                    else:
                        leaking = True
                        break
                x = currentPositions[i][0]
                while (x,y) not in clayCoordinates:
                    if (x,y+1) in clayCoordinates or (x,y+1) in waterStandArray:
                        tempWaterStandArray.append((x,y))
                        x += 1
                    else:
                        leaking = True
                        break
                if leaking != True:
                    for coordinate in tempWaterStandArray:
                        waterStandArray.add(coordinate)
                else:
                    x = currentPositions[i][0]
                    if (x-1,y) not in clayCoordinates and (x-1,y) not in waterFlowArray:
                        newCurrentPositions.append((x-1,y))
                        waterFlowArray.add(currentPositions[i])
                    else:
                        waterFlowArray.add(currentPositions[i])
                    if (x+1,y) not in clayCoordinates and (x+1,y) not in waterFlowArray:
                        newCurrentPositions.append((x+1,y))
                        waterFlowArray.add(currentPositions[i])
                    else:
                        waterFlowArray.add(currentPositions[i])
        if newCurrentPositions == []:
            currentPositions = [spring]
            if overMaxPositions < 50:
                waterFlowArray = set()
        else:      
            currentPositions = newCurrentPositions.copy()
    j = 0
    waterFlowArray = list(waterFlowArray)
    while j < len(waterFlowArray):
        if waterFlowArray[j][1] < minY:
            del waterFlowArray[j]
            j = 0
        else:
            j += 1
    return waterStandArray, waterFlowArray

def printMap(clayCoordinates, waterFlowArray, waterStandArray, maxY):
    for y in range(maxY+1):
        line = ''
        for x in range(460,680):
            if (x,y) in clayCoordinates:
                line += '#'
            elif (x,y) in waterStandArray:
                line += '~'
            elif (x,y) in waterFlowArray:
                line += '|'
            else:
                line += '.'
        print(line)
    

spring = (500, 0)
clayCoordinates = parseInput('AoC 2018 Day 17 - input.txt')
minY, maxY = getYBorders(clayCoordinates)
waterStandArray, waterFlowArray = waterFlow(spring, clayCoordinates, minY, maxY)
#printMap(clayCoordinates, waterFlowArray, waterStandArray, maxY)
print('Part 1 answer: ' + str(len(waterFlowArray) + len(waterStandArray)))
print('Part 2 answer: ' + str(len(waterStandArray)))
