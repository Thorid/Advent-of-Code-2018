def parseFile(file):
    inputArray = []
    for i in range(len(file)):
        tempInputArray = []
        startX = file[i][file[i].find('@ ')+2:file[i].rfind(',')]
        startY = file[i][file[i].find(',')+1:file[i].rfind(':')]
        sizeX = file[i][file[i].find(': ')+2:file[i].rfind('x')]
        sizeY = file[i][file[i].find('x')+1:]
        tempInputArray.append(startX)
        tempInputArray.append(startY)
        tempInputArray.append(sizeX)
        tempInputArray.append(sizeY)
        inputArray.append(tempInputArray)
    return inputArray


puzzleInput = open('AoC 2018 Day 3 - input.txt').read().split('\n')
fabricDict = {}
fabricArray = parseFile(puzzleInput)


for i in range(len(fabricArray)):
    for j in range(int(fabricArray[i][0]),int(fabricArray[i][0]) + int(fabricArray[i][2])):
        for k in range(int(fabricArray[i][1]),int(fabricArray[i][1]) + int(fabricArray[i][3])):
            xy = [j,k]
            if str(xy) in fabricDict.keys():
                fabricDict[str(xy)] += 1
            else:
                fabricDict[str(xy)] = 1


for i in range(len(fabricArray)):
    overlapping = 0
    for j in range(int(fabricArray[i][0]),int(fabricArray[i][0]) + int(fabricArray[i][2])):
        for k in range(int(fabricArray[i][1]),int(fabricArray[i][1]) + int(fabricArray[i][3])):
            xy = [j,k]
            if fabricDict[str(xy)] > 1:
                overlapping += 1
    if overlapping == 0:
        print(i+1)
        break
    
        

        


