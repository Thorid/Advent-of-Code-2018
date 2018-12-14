def parseFile(file):
    fileArray = open(file).read().split('\n')
    parsedInput = []
    for i in range(len(fileArray)):
        tempArray = []
        first = fileArray[i][fileArray[i].find('Step ')+5:fileArray[i].rfind(' must')]
        second = fileArray[i][fileArray[i].find('step ')+5:fileArray[i].rfind(' can')]
        tempArray.append(first)
        tempArray.append(second)
        parsedInput.append(tempArray)
    return parsedInput

def calculateWorkTime(puzzleInputArray):
    allLetters = set()
    for k in range(len(puzzleInputArray)):
        allLetters.add(puzzleInputArray[k][0])
        allLetters.add(puzzleInputArray[k][1])
    allLetters = list(allLetters)
    allLetters.sort()
    assemblyTimeDict = {}
    for t in range(len(allLetters)):
        assemblyTimeDict[allLetters[t]] = t + 61
    workDoneDict = assemblyTimeDict.fromkeys(assemblyTimeDict.keys(), 0)
    possibleNextSteps = set()
    finishedStep = ''
    workTime = 0
    doneArray = []
    while True:
        possibleNextSteps = set(possibleNextSteps)
        i = 0
        while i < len(puzzleInputArray):
            try:
                if puzzleInputArray[i][0] == finishedStep:
                    del puzzleInputArray[i]
                    i = 0
                else:
                    i += 1
            except:
                break
        finishedStep = ''
        leftLetters, rightLetters = [],set()
        for i in range(len(puzzleInputArray)):
            leftLetters.append(puzzleInputArray[i][0])
            rightLetters.add(puzzleInputArray[i][1])
        for j in range(len(leftLetters)):
            if leftLetters[j] not in rightLetters:
                possibleNextSteps.add(leftLetters[j])
        possibleNextSteps = list(possibleNextSteps)
        if len(doneArray) == len(allLetters):
            return workTime
        elif possibleNextSteps == []:
            for letter in allLetters:
                if letter not in doneArray:
                    possibleNextSteps.append(letter)
        while finishedStep == '':
            workTime += 1
            for step in possibleNextSteps:
                workDoneDict[step] += 1 
                if workDoneDict[step] == assemblyTimeDict[step]:
                    finishedStep = step 
        possibleNextSteps.remove(finishedStep)
        doneArray.append(finishedStep)



puzzleInput = parseFile('AoC 2018 Day 7 - input.txt')
print(calculateWorkTime(puzzleInput))

