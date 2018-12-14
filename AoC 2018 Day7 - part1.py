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

def findNextStep(puzzleInputArray):
    stepsDone = []
    allLetters = set()
    for k in range(len(puzzleInputArray)):
        allLetters.add(puzzleInputArray[k][0])
        allLetters.add(puzzleInputArray[k][1])
    allLetters = list(allLetters)
    while True:
        possibleNextSteps = []
        i = 0
        while i < len(puzzleInputArray):
            try:
                if puzzleInputArray[i][0] == stepsDone[-1]:
                    del puzzleInputArray[i]
                    i = 0
                else:
                    i += 1
            except:
                break
        leftLetters, rightLetters = [],set()
        for i in range(len(puzzleInputArray)):
            leftLetters.append(puzzleInputArray[i][0])
            rightLetters.add(puzzleInputArray[i][1])
        for j in range(len(leftLetters)):
            if leftLetters[j] not in rightLetters:
                possibleNextSteps.append(leftLetters[j])
        possibleNextSteps.sort()
        if possibleNextSteps != []:
            stepsDone.append(possibleNextSteps[0])
        else:
            for letter in allLetters:
                if letter not in stepsDone:
                    stepsDone.append(letter)
            result = ''
            for step in stepsDone:
                result += step
            return result

puzzleInput = parseFile('AoC 2018 Day 7 - input.txt')
print(findNextStep(puzzleInput))

