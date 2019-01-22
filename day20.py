import copy

def parseFile(file):
    fileInput = open(file).read()
    return fileInput

def getRoomsDoorsCoords(directions):
    x,y = 0,0
    rooms = [(x,y)]
    doors = []
    savedPositions = []
    for direction in directions:
        if direction == 'N':
            y -= 1
            doors.append((x,y))
            y -= 1
            rooms.append((x,y))
        elif direction == 'S':
            y += 1
            doors.append((x,y))
            y += 1
            rooms.append((x,y))
        elif direction == 'E':
            x += 1
            doors.append((x,y))
            x += 1
            rooms.append((x,y))
        elif direction == 'W':
            x -= 1
            doors.append((x,y))
            x -= 1
            rooms.append((x,y))
        elif direction == '(':
            savedPositions.append((x,y))
        elif direction == '|':
            x,y = savedPositions[-1][0],savedPositions[-1][1]
        elif direction == ')':
            del savedPositions[-1]
    return rooms,doors

def printMap(rooms, doors):
    minX,minY,maxX,maxY = 0,0,0,0
    for room in rooms:
        if room[0] < minX:
            minX = room[0]
        if room[0] > maxX:
            maxX = room[0]
        if room[1] < minY:
            minY = room[1]
        if room[1] > maxY:
            maxY = room[1]
    minX -= 1
    minY -= 1
    maxX += 2
    maxY += 2
    for y in range(minY,maxY):
        lineToPrint = ''
        for x in range(minX,maxX):
            if (x,y) == (0,0):
                lineToPrint += 'X'
            elif (x,y) in rooms:
                lineToPrint += '.'
            elif (x,y) in doors:
                lineToPrint += '/'
            else:
                lineToPrint += '#'
        print(lineToPrint)

def calculateDistance(doors):
    roomsToCheck = [(0,0)]
    distance = 0
    distanceDict = {(0,0) : distance}
    while roomsToCheck != []:
        newRoomsToCheck = []
        distance += 1
        for i in range(len(roomsToCheck)):
            x = roomsToCheck[i][0]
            y = roomsToCheck[i][1]
            if (x+1,y) in doors and (x+2,y) not in distanceDict.keys():
                newRoomsToCheck.append((x+2,y))
                distanceDict[(x+2,y)] = distance
            if (x-1,y) in doors and (x-2,y) not in distanceDict.keys():
                newRoomsToCheck.append((x-2,y))
                distanceDict[(x-2,y)] = distance
            if (x,y+1) in doors and (x,y+2) not in distanceDict.keys():
                newRoomsToCheck.append((x,y+2))
                distanceDict[(x,y+2)] = distance
            if (x,y-1) in doors and (x,y-2) not in distanceDict.keys():
                newRoomsToCheck.append((x,y-2))
                distanceDict[(x,y-2)] = distance
        roomsToCheck = copy.copy(newRoomsToCheck)
    return max(distanceDict.values())
        

directions = parseFile('input.txt')
rooms,doors = getRoomsDoorsCoords(directions)
print(calculateDistance(doors))
