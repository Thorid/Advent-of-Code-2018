def parseRailsMap(file):
    fileArray = open(file).read().split('\n')
    railsMap = {}
    for y in range(len(fileArray)):
        for x in range(len(fileArray[y])):
            if fileArray[y][x] != '^' and fileArray[y][x] != 'v' and fileArray[y][x] != '<' and fileArray[y][x] != '>':
                railsMap[(x,y)] = fileArray[y][x]
    for y in range(len(fileArray)):
        for x in range(len(fileArray[y])):                
            if fileArray[y][x] == '^':
                if railsMap.get((x-1,y)) not in ('-','+') and railsMap.get((x+1,y)) not in ('-','+'):
                    railsMap[(x,y)] = '|'
                elif railsMap.get((x-1,y)) in ('-','+') and railsMap.get((x+1,y)) not in ('-','+'):
                    railsMap[(x,y)] = '/'
                elif railsMap.get((x-1,y)) not in ('-','+') and railsMap.get((x+1,y)) in ('-','+'):
                    railsMap[(x,y)] = '\\'
                elif railsMap.get((x-1,y)) in ('-','+') and railsMap.get((x+1,y)) in ('-','+'):
                    railsMap[(x,y)] = '+'
            elif fileArray[y][x] == 'v':
                if railsMap.get((x-1,y)) not in ('-','+') and railsMap.get((x+1,y)) not in ('-','+'):
                    railsMap[(x,y)] = '|'
                elif railsMap.get((x-1,y)) in ('-','+') and railsMap.get((x+1,y)) not in ('-','+'):
                    railsMap[(x,y)] = '\\'
                elif railsMap.get((x-1,y)) not in ('-','+') and railsMap.get((x+1,y)) in ('-','+'):
                    railsMap[(x,y)] = '/'
                elif railsMap.get((x-1,y)) in ('-','+') and railsMap.get((x+1,y)) in ('-','+'):
                    railsMap[(x,y)] = '+'
            elif fileArray[y][x] == '>':
                if railsMap.get((x,y-1)) not in ('|','+') and railsMap.get((x,y+1)) not in ('|','+'):
                    railsMap[(x,y)] = '-'
                elif railsMap.get((x,y-1)) in ('|','+') and railsMap.get((x,y+1)) in ('|','+'):
                    railsMap[(x,y)] = '+'
                elif railsMap.get((x,y-1)) in ('|','+') and railsMap.get((x,y+1)) not in ('|','+'):
                    railsMap[(x,y)] = '\\'
                elif railsMap.get((x,y-1)) not in ('|','+') and railsMap.get((x,y+1)) in ('|','+'):
                    railsMap[(x,y)] = '/'
            elif fileArray[y][x] == '<':
                if railsMap.get((x,y-1)) not in ('|','+') and railsMap.get((x,y+1)) not in ('|','+'):
                    railsMap[(x,y)] = '-'
                elif railsMap.get((x,y-1)) in ('|','+') and railsMap.get((x,y+1)) in ('|','+'):
                    railsMap[(x,y)] = '+'
                elif railsMap.get((x,y-1)) in ('|','+') and railsMap.get((x,y+1)) not in ('|','+'):
                    railsMap[(x,y)] = '/'
                elif railsMap.get((x,y-1)) not in ('|','+') and railsMap.get((x,y+1)) in ('|','+'):
                    railsMap[(x,y)] = '\\'            
    return railsMap

def parseCartsParameters(file):
    fileArray = open(file).read().split('\n')
    cartsPositions = {}
    cartsDirections = {}
    cartsXroads = {}
    cartID = 1
    for y in range(len(fileArray)):
        for x in range(len(fileArray[y])):
            if fileArray[y][x] == '^':
                cartsDirections['Cart' + str(cartID)] = '^'
                cartsPositions['Cart' + str(cartID)] = (x,y)
                cartsXroads['Cart' + str(cartID)] = 'L'
                cartID += 1
            elif fileArray[y][x] == 'v':
                cartsDirections['Cart' + str(cartID)] = 'v'
                cartsPositions['Cart' + str(cartID)] = (x,y)
                cartsXroads['Cart' + str(cartID)] = 'L'
                cartID += 1
            elif fileArray[y][x] == '<':
                cartsDirections['Cart' + str(cartID)] = '<'
                cartsPositions['Cart' + str(cartID)] = (x,y)
                cartsXroads['Cart' + str(cartID)] = 'L'
                cartID += 1
            elif fileArray[y][x] == '>':
                cartsDirections['Cart' + str(cartID)] = '>'
                cartsPositions['Cart' + str(cartID)] = (x,y)
                cartsXroads['Cart' + str(cartID)] = 'L'
                cartID += 1
    return cartsPositions, cartsDirections, cartsXroads


def findKey(inputDict, value):
    return next((k for k, v in inputDict.items() if v == value), None)

def changeXroadsDirection(xRoad):
    if xRoad == 'L':
        xRoad = 'S'
    elif xRoad == 'S':
        xRoad = 'R'
    elif xRoad == 'R':
        xRoad = 'L'
    return xRoad
   
def printCurrentMap(railsMap,cartsPositions,cartsDirections):
    maxX = 0
    maxY = 0
    for key in railsMap.keys():
        if key[0] > maxX:
            maxX = key[0]
        if key[1] > maxY:
            maxY = key[1]
    for y in range(maxY+1):
        lineToPrint = ''
        for x in range(maxX+1):
            if (x,y) in cartsPositions.values():
                cartName = findKey(cartsPositions,(x,y))
                lineToPrint += cartsDirections[cartName]
            elif (x,y) in railsMap.keys():
                lineToPrint += railsMap[(x,y)]
            else:
                lineToPrint += ' '
        print(lineToPrint)

def move(railsMap,cartsPositions,cartsDirections, cartXroads):
    newPositions = {}
    newDirections = {}
    for cart,v in cartsPositions.items():
        x = v[0]
        y = v[1]
        if cartsDirections[cart] == '^':
            if (x,y-1) in newPositions.values():
                return (x,y-1),1,1           
            newPositions[cart] = (x,y-1)
            if railsMap[(x,y-1)] == '|':
                newDirections[cart] = '^'
            elif railsMap[(x,y-1)] == '\\':
                newDirections[cart] = '<'
            elif railsMap[(x,y-1)] == '/':
                newDirections[cart] = '>'
            elif railsMap[(x,y-1)] == '+':
                if cartXroads[cart] == 'L':
                    newDirections[cart] = '<'
                elif cartXroads[cart] == 'S':
                    newDirections[cart] = '^'
                elif cartXroads[cart] == 'R':
                    newDirections[cart] = '>'
                cartXroads[cart] = changeXroadsDirection(cartXroads[cart])
        elif cartsDirections[cart] == 'v':
            if (x,y+1) in newPositions.values():
                return (x,y+1),1,1
            newPositions[cart] = (x,y+1)
            if railsMap[(x,y+1)] == '|':
                newDirections[cart] = 'v'
            elif railsMap[(x,y+1)] == '\\':
                newDirections[cart] = '>'
            elif railsMap[(x,y+1)] == '/':
                newDirections[cart] = '<'
            elif railsMap[(x,y+1)] == '+':
                if cartXroads[cart] == 'L':
                    newDirections[cart] = '>'
                elif cartXroads[cart] == 'S':
                    newDirections[cart] = 'v'
                elif cartXroads[cart] == 'R':
                    newDirections[cart] = '<'
                cartXroads[cart] = changeXroadsDirection(cartXroads[cart])
        elif cartsDirections[cart] == '<':
            if (x-1,y) in newPositions.values():
                return (x-1,y),1,1
            newPositions[cart] = (x-1,y)
            if railsMap[(x-1,y)] == '-':
                newDirections[cart] = '<'
            elif railsMap[(x-1,y)] == '\\':
                newDirections[cart] = '^'
            elif railsMap[(x-1,y)] == '/':
                newDirections[cart] = 'v'
            elif railsMap[(x-1,y)] == '+':
                if cartXroads[cart] == 'L':
                    newDirections[cart] = 'v'
                elif cartXroads[cart] == 'S':
                    newDirections[cart] = '<'
                elif cartXroads[cart] == 'R':
                    newDirections[cart] = '^'
                cartXroads[cart] = changeXroadsDirection(cartXroads[cart])
        elif cartsDirections[cart] == '>':
            if (x+1,y) in newPositions.values():
                return (x+1,y),1,1
            newPositions[cart] = (x+1,y)
            if railsMap[(x+1,y)] == '-':
                newDirections[cart] = '>'
            elif railsMap[(x+1,y)] == '\\':
                newDirections[cart] = 'v'
            elif railsMap[(x+1,y)] == '/':
                newDirections[cart] = '^'
            elif railsMap[(x+1,y)] == '+':
                if cartXroads[cart] == 'L':
                    newDirections[cart] = '^'
                elif cartXroads[cart] == 'S':
                    newDirections[cart] = '>'
                elif cartXroads[cart] == 'R':
                    newDirections[cart] = 'v'
                cartXroads[cart] = changeXroadsDirection(cartXroads[cart])
    return newPositions, newDirections, cartXroads

railsMap = parseRailsMap('AoC 2018 Day 13 - input.txt')
cartsPositions, cartsDirections, cartXroads = parseCartsParameters('AoC 2018 Day 13 - input.txt')                       

while True:
    cartsPositions, cartsDirections, cartXroads = move(railsMap,cartsPositions,cartsDirections,cartXroads)
    if cartsDirections == 1:
        break
print(cartsPositions)
