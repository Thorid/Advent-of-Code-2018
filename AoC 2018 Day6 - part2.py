def parseFile(file):
    fileArray = open(file).read().split('\n')
    parsedInput = {}
    for i in range(len(fileArray)):
        x = int(fileArray[i][:fileArray[i].find(',')])
        y = int(fileArray[i][fileArray[i].find(', ')+2:])
        parsedInput[i+1] = [x,y]
    return parsedInput

def getMaxCoordinate(puzzleInput):
    maxCoordinate = 0
    for value in puzzleInput.values():
        if value[0] > maxCoordinate:
            maxCoordinate = value[0]
        if value[1] > maxCoordinate:
            maxCoordinate = value[1]
    return maxCoordinate

def generateMap(maxCoordinate):
    myMap = []
    for i in range(maxCoordinate+1):
        for j in range(maxCoordinate+1):
            myMap.append([j,i])
    return myMap

def getCoordinateDistance(puzzleInput, myMap):
    coordinateDistanceArray = []
    for mapCoordinate in myMap:
        distance = 0
        mapX = mapCoordinate[0]
        mapY = mapCoordinate[1]
        for coordinateID,inputCoordinate in puzzleInput.items():
            inputX = inputCoordinate[0]
            inputY = inputCoordinate[1]
            distance += abs(mapX - inputX) + abs(mapY - inputY)
        coordinateDistanceArray.append(distance)
    return coordinateDistanceArray


puzzleInput = parseFile('AoC 2018 Day 6 - input.txt')
maxCoordinate = getMaxCoordinate(puzzleInput)
myMap = generateMap(maxCoordinate)
coordinateDistanceArray = getCoordinateDistance(puzzleInput,myMap)
result = 0
for distance in coordinateDistanceArray:
    if distance < 10000:
        result += 1
print(result)
        


