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

def getCoordinateOwners(puzzleInput, myMap):
    coordinateOwnerArray = []
    for mapCoordinate in myMap:
        distance = 1000
        mapX = mapCoordinate[0]
        mapY = mapCoordinate[1]
        for coordinateID,inputCoordinate in puzzleInput.items():
            inputX = inputCoordinate[0]
            inputY = inputCoordinate[1]
            newDistance = abs(mapX - inputX) + abs(mapY - inputY)
            if newDistance < distance:
                distance = newDistance
                territoryOwner = coordinateID
            elif newDistance == distance:
                territoryOwner = 0
        coordinateOwnerArray.append(territoryOwner)
    return coordinateOwnerArray

def findInfiniteOwners(myMap, coordinateOwnerArray, maxCoordinate):
    infiniteOwners = set()
    for i in range(len(myMap)):
        if myMap[i][0] == 0 or myMap[i][1] == 0 or myMap[i][0] == maxCoordinate or myMap[i][1] == maxCoordinate:
            infiniteOwners.add(coordinateOwnerArray[i])
    return infiniteOwners

puzzleInput = parseFile('AoC 2018 Day 6 - input.txt')
maxCoordinate = getMaxCoordinate(puzzleInput)
myMap = generateMap(maxCoordinate)
coordinateOwnerArray = getCoordinateOwners(puzzleInput,myMap)
infiniteOwners = findInfiniteOwners(myMap, coordinateOwnerArray, maxCoordinate)
ownedCoordinatesNumber = {}
for owner in coordinateOwnerArray:
    if owner not in infiniteOwners:
        if owner in ownedCoordinatesNumber.keys():
            ownedCoordinatesNumber[owner] += 1
        else:
            ownedCoordinatesNumber[owner] = 1
print(max(ownedCoordinatesNumber.values()))
        


