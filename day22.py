depth = 9171
targetX = 7
targetY = 721
erosionLevelDict = {}
currentX = 0
currentY = 0

while currentX <= targetX or currentY <= targetY:
    if currentX <= targetX:
        x = currentX    
        for y in range(targetY + 1):
            if x != 0 and y != 0:
                erosionLevelDict[(x,y)] = (erosionLevelDict[(x-1,y)] * erosionLevelDict[(x,y-1)] + depth) % 20183
            elif x != 0 and y == 0:
                erosionLevelDict[(x,y)] = (x * 16807 + depth) % 20183
            elif x == 0 and y != 0:
                erosionLevelDict[(x,y)] = (y * 48271 + depth) % 20183
            else:
                erosionLevelDict[(x,y)] = (0 + depth) % 20183
        currentX += 1

    if currentY <= targetY:
        y = currentY
        for x in range(targetX + 1):
            if x != 0 and y != 0:
                erosionLevelDict[(x,y)] = (erosionLevelDict[(x-1,y)] * erosionLevelDict[(x,y-1)] + depth) % 20183
            elif x != 0 and y == 0:
                erosionLevelDict[(x,y)] = (x * 16807 + depth) % 20183
            elif x == 0 and y != 0:
                erosionLevelDict[(x,y)] = (y * 48271 + depth) % 20183
            else:
                erosionLevelDict[(x,y)] = (0 + depth) % 20183
        currentY += 1

        
result = 0
for y in range(targetY + 1):
    for x in range(targetX + 1):
            result += erosionLevelDict[(x,y)] % 3
print(result)

