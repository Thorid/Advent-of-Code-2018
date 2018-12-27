class Unit():
    def __init__(self, coordinates, side, iden, ap):
        self.hp = 200
        self.attackPower = ap
        self.position = coordinates
        self.race = side
        self.name = str(self.race) + '#' + str(iden)

    def __repr__(self):
        return self.name

def parseMap(file):
    fileArray = open(file).read().split('\n')
    mapDict = {}
    for y in range(len(fileArray)):
        for x in range(len(fileArray[y])):
            if fileArray[y][x] == 'G' or fileArray[y][x] == 'E':
                mapDict[(x,y)] = '.'
            else:
                mapDict[(x,y)] = fileArray[y][x]
    return mapDict

def parseUnits(file, elfAP):
    fileArray = open(file).read().split('\n')
    goblinCounter = 1
    elfCounter = 1
    unitsArray = []
    for y in range(len(fileArray)):
        for x in range(len(fileArray[y])):
            if fileArray[y][x] == 'G':
                unitsArray.append(Unit([x,y],'Goblin', goblinCounter, 3))
                goblinCounter += 1
            elif fileArray[y][x] == 'E':
                unitsArray.append(Unit([x,y],'Elf', elfCounter, elfAP))
                elfCounter += 1
    return unitsArray

def printCurrentMap(currentMap):
    maxX = 0
    maxY = 0
    for key in currentMap.keys():
        if key[0] > maxX:
            maxX = key[0]
        if key[1] > maxY:
            maxY = key[1]
    for y in range(maxY+1):
        lineToPrint = ''
        for x in range(maxX+1):
            lineToPrint += currentMap[(x,y)]
        print(lineToPrint)

def updateMap(mapDict,unitsArray):
    currentMap = mapDict.copy()
    for unit in unitsArray:
        if unit.race == 'Goblin' and unit.hp > 0:
            currentMap[tuple(unit.position)] = 'G'
        elif unit.race == 'Elf' and unit.hp > 0:
            currentMap[tuple(unit.position)] = 'E'
    return currentMap
        

def getPossibleTargets(currentMap, activeUnit, unitsArray):
    possibleTargetArray = []
    currentPosition = activeUnit.position
    for unit in unitsArray:
        if unit.race != activeUnit.race and unit.hp > 0:
            x = unit.position[0]
            y = unit.position[1]
            if currentMap[(x+1,y)] == '.':
                possibleTargetArray.append([x+1,y])
            if currentMap[(x-1,y)] == '.':
                possibleTargetArray.append([x-1,y])
            if currentMap[(x,y+1)] == '.':
                possibleTargetArray.append([x,y+1])
            if currentMap[(x,y-1)] == '.':
                possibleTargetArray.append([x,y-1])
    return possibleTargetArray
                                           
def getClosestReachableTargets(currentMap, activeUnit, possibleTargetArray):
    start = activeUnit.position
    reachableTargetDict = {}
    for target in possibleTargetArray:
        distance = 0
        path = [target]
        stopSearching = False
        while stopSearching == False:
            distance += 1
            stopSearching = True
            newPath = path.copy()
            for i in range(len(path)):
                x = path[i][0]
                y = path[i][1]
                if [x+1,y] == start or [x-1,y] == start or [x,y+1] == start or [x,y-1] == start:
                    reachableTargetDict[tuple(target)] = distance
                    stopSearching = True
                    break
                if currentMap[(x+1,y)] == '.' and [x+1,y] not in newPath:
                    newPath.append([x+1,y])
                    stopSearching = False
                if currentMap[(x-1,y)] == '.' and [x-1,y] not in newPath:
                    newPath.append([x-1,y])
                    stopSearching = False
                if currentMap[(x,y+1)] == '.' and [x,y+1] not in newPath:
                    newPath.append([x,y+1])
                    stopSearching = False
                if currentMap[(x,y-1)] == '.' and [x,y-1] not in newPath:
                    newPath.append([x,y-1])
                    stopSearching = False
            path = newPath.copy()
    closestReachableTargetArray = []
    if reachableTargetDict != {}:
        shortestDistance = min(reachableTargetDict.values())            
        for k,v in reachableTargetDict.items():
            if v == shortestDistance:
                closestReachableTargetArray.append(k) 
    return closestReachableTargetArray
        
def pickTargetFromReachable(closestReachableTargetArray):
    if len(closestReachableTargetArray) == 0:
        chosenTarget = ()
    elif len(closestReachableTargetArray) == 1:
        chosenTarget = closestReachableTargetArray[0]
    else:
        tempArray = []
        minY = 999
        for target in closestReachableTargetArray:            
            if target[1] < minY:
                minY = target[1]
        for target in closestReachableTargetArray:
            if target[1] == minY:
                tempArray.append(target)
        if len(tempArray) == 1:
            chosenTarget = tempArray[0]
        else:
            minX = 999
            for target in tempArray:
                if target[0] < minX:
                    minX = target[0]
            for target in tempArray:
                if target[0] == minX:
                    chosenTarget = target
    return chosenTarget

def chooseTarget(currentMap, unit, unitsArray):
    possibleTargetArray = getPossibleTargets(currentMap, unit, unitsArray)
    closestReachableTargetArray = getClosestReachableTargets(currentMap, unit, possibleTargetArray)
    chosenTarget = pickTargetFromReachable(closestReachableTargetArray)
    return chosenTarget

def move(currentMap, activeUnit, chosenTarget):
    if chosenTarget == ():
        return False
    start = activeUnit.position
    distance = 0
    path = {}
    path[chosenTarget] = distance
    stop = False
    while stop == False:
        distance += 1
        newPath = path.copy()
        for k in path.keys():
            x = k[0]
            y = k[1]
            if [x+1,y] == start or [x-1,y] == start or [x,y+1] == start or [x,y-1] == start:
                newPath[tuple(start)] = distance
                stop = True
                break
            if currentMap[(x+1,y)] == '.' and (x+1,y) not in newPath.keys():
                newPath[(x+1,y)] = distance
            if currentMap[(x-1,y)] == '.' and (x-1,y) not in newPath.keys():
                newPath[(x-1,y)] = distance
            if currentMap[(x,y+1)] == '.' and (x,y+1) not in newPath.keys():
                newPath[(x,y+1)] = distance
            if currentMap[(x,y-1)] == '.' and (x,y-1) not in newPath.keys():
                newPath[(x,y-1)] = distance
        path = newPath.copy()
    x = start[0]
    y = start[1]
    if path.get((x,y-1)) == distance - 1:
        newPosition = [x,y-1]
        return newPosition
    elif path.get((x-1,y)) == distance - 1:
        newPosition = [x-1,y]
        return newPosition
    elif path.get((x+1,y)) == distance - 1:
        newPosition = [x+1,y]
        return newPosition
    elif path.get((x,y+1)) == distance - 1:
        newPosition = [x,y+1]
        return newPosition

def checkIfNearEnemy(currentMap, activeUnit):
    x = activeUnit.position[0]
    y = activeUnit.position[1]
    if activeUnit.race == 'Elf':
        enemySymbol = 'G'
    elif activeUnit.race == 'Goblin':
        enemySymbol = 'E'
    if currentMap[(x,y-1)] == enemySymbol or currentMap[(x-1,y)] == enemySymbol or currentMap[(x+1,y)] == enemySymbol or currentMap[(x,y+1)] == enemySymbol:
        return True
    else:
        return False

def updateUnitsStatus(unitsArray,currentMap):
    maxX = 0
    maxY = 0
    for key in currentMap.keys():
        if key[0] > maxX:
            maxX = key[0]
        if key[1] > maxY:
            maxY = key[1]
    updatedUnitsArray = []
    for y in range(maxY+1):
        for x in range(maxX+1):
            for unit in unitsArray:
                if unit.position == [x,y] and unit.hp > 0:
                    updatedUnitsArray.append(unit)
    return updatedUnitsArray

def oneRound(mapDict,unitsArray,currentMap,roundNo):
    battleEnded = False
    for unit in unitsArray:
        if battleEnded == True:
            roundNo -= 1
            break
        nearEnemy = checkIfNearEnemy(currentMap, unit)
        if nearEnemy == False:
            chosenTarget = chooseTarget(currentMap, unit, unitsArray)
            newPosition = move(currentMap, unit, chosenTarget)
            if newPosition != False:
                unit.position = newPosition
            currentMap = updateMap(mapDict,unitsArray)
            nearEnemy = checkIfNearEnemy(currentMap, unit)
        if nearEnemy == True:
            currentMap = updateMap(mapDict,unitsArray)
            attackedUnitPosition = chooseAttackTarget(unit, unitsArray)
            attack(unit,attackedUnitPosition, unitsArray)
        currentMap = updateMap(mapDict,unitsArray)
        battleEnded = checkIfBattleEnded(unitsArray)
    unitsArray = updateUnitsStatus(unitsArray,currentMap)
    currentMap = updateMap(mapDict,unitsArray)
    roundNo += 1
    return unitsArray, currentMap, battleEnded, roundNo

def chooseAttackTarget(activeUnit, unitsArray):
    possibleAttackArray = []
    for unit in unitsArray:      
        x = activeUnit.position[0]
        y = activeUnit.position[1]
        if activeUnit.race != unit.race and unit.hp > 0 and (unit.position == [x,y-1] or unit.position == [x-1,y] or unit.position == [x+1,y] or unit.position == [x,y+1]):
            possibleAttackArray.append(unit)
    if len(possibleAttackArray) == 1:
        attackedUnitPosition = possibleAttackArray[0].position
    else:
        lowestHP = 999
        for unit in possibleAttackArray:
            if unit.hp < lowestHP:
                lowestHP = unit.hp
                attackedUnitPosition = unit.position
    return attackedUnitPosition
            
def attack(activeUnit,attackedUnitPosition, unitsArray):
    for unit in unitsArray:
        if unit.position == attackedUnitPosition and activeUnit.hp > 0:
            unit.hp -= activeUnit.attackPower

def checkIfBattleEnded(unitsArray):
    goblinExists = False
    elfExists = False
    for unit in unitsArray:
        if unit.race == 'Goblin' and unit.hp > 0:
            goblinExists = True
        elif unit.race == 'Elf' and unit.hp > 0:
            elfExists = True
    if goblinExists == True and elfExists == True:
        return False
    else:
        return True

elfAP = 3
while True:
    elfNumber = 0
    elfAP += 1    
    inputFile = 'AoC 2018 Day 15 - input.txt'
    mapDict = parseMap(inputFile)
    unitsArray = parseUnits(inputFile, elfAP)
    for unit in unitsArray:
        if unit.race == 'Elf':
            elfNumber += 1
    currentMap = updateMap(mapDict,unitsArray)
    battleEnded = False
    roundNo = 0
    while True:
        unitsArray, currentMap, battleEnded, roundNo = oneRound(mapDict,unitsArray,currentMap,roundNo)
        elfCount = 0
        for unit in unitsArray:
            if unit.race == 'Elf':
                elfCount += 1
        if elfCount < elfNumber:
            print('Elf died!')
            break        
        if battleEnded == True:
            print('No elves died! :)')
            break
        print('Round ended: ' + str(roundNo))
    if battleEnded == True:
        remainingHp = 0
        for unit in unitsArray:
            remainingHp += unit.hp
        outcome = roundNo * remainingHp
        print(outcome)
        break
