depth = 510
targetX = 10
targetY = 10
erosionLevelModuloDict = {}
currentX = 0
currentY = 0

while currentX <= targetX or currentY <= targetY:
    if currentX <= targetX:
        x = currentX    
    for y in range(targetY + 1):
        if x != 0 and y != 0:
            if erosionLevelModuloDict[(x-1,y)] % 3 == 0 or erosionLevelModuloDict[(x,y-1)] % 3 == 0:
                erosionLevelModuloDict[(x,y)] = 0
            elif erosionLevelModuloDict[(x-1,y)] % 3 == erosionLevelModuloDict[(x,y-1)] % 3:
                erosionLevelModuloDict[(x,y)] = 1
            else:
                erosionLevelModuloDict[(x,y)] = 0
        elif x != 0 and y == 0:
            erosionLevelModuloDict[(x,y)] = (x * 16807 + depth) % 20183 % 3
        elif x == 0 and y != 0:
            erosionLevelModuloDict[(x,y)] = (y * 48271 + depth) % 20183 % 3
        else:
            erosionLevelModuloDict[(x,y)] = (0 + depth) % 20183 % 3
        #print(erosionLevelModuloDict[(x,y)])
    currentX += 1

    if currentY <= targetY:
        y = currentY
    for x in range(targetX +1):
        if x != 0 and y != 0:
            if erosionLevelModuloDict[(x-1,y)] % 3 == 0 or erosionLevelModuloDict[(x,y-1)] % 3 == 0:
                erosionLevelModuloDict[(x,y)] = 0
            elif erosionLevelModuloDict[(x-1,y)] % 3 == erosionLevelModuloDict[(x,y-1)] % 3:
                erosionLevelModuloDict[(x,y)] = 1
            else:
                erosionLevelModuloDict[(x,y)] = 0
        elif x != 0 and y == 0:
            erosionLevelModuloDict[(x,y)] = (x * 16807 + depth) % 20183 % 3
        elif x == 0 and y != 0:
            erosionLevelModuloDict[(x,y)] = (y * 48271 + depth) % 20183 % 3
        else:
            erosionLevelModuloDict[(x,y)] = (0 + depth) % 20183 % 3
        #print(erosionLevelModuloDict[(x,y)])
    currentY += 1

        

for y in range(targetY + 1):
    lineToPrint = ''
    for x in range(targetX + 1):
        if erosionLevelModuloDict[(x,y)] == 0:
            lineToPrint += '.'
        elif erosionLevelModuloDict[(x,y)] == 1:
            lineToPrint += '='
        elif erosionLevelModuloDict[(x,y)] == 2:
            lineToPrint += '|'
    print(lineToPrint)
