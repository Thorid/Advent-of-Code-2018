def parseFile(file):
    fileArray = open(file).read().split('\n')
    fileArray[0] = fileArray[0][fileArray[0].find(': ')+2:]
    del fileArray[1]
    for i in range(len(fileArray)):
        fileArray[i] = fileArray[i].replace('#','1')
        fileArray[i] = fileArray[i].replace('.','0')
    startingPosition = fileArray[0]
    del fileArray[0]
    inputDict = {}
    for j in range(len(fileArray)):
        inputDict[fileArray[j][:fileArray[j].find(' =')]] = fileArray[j][fileArray[j].find('> ')+2:]
    return inputDict, startingPosition

def nextGeneration(initialState, puzzleInput, start, end):
    if initialState[:5] != '00000':
        initialState = '00000' + initialState
        start -= 3
    else:
        start += 2
    if initialState[-5:] != '00000':
        initialState += '00000'
        end += 3
    else:
        end -= 2
    nextState = ''
    for i in range(2,len(initialState)-2):
        if initialState[i-2:i+3] in puzzleInput.keys():
            nextState += puzzleInput[initialState[i-2:i+3]]
        else:
            nextState += '0'
    return nextState, start, end

def calculateScore(currentState, start, end):
    score = 0
    for i in range(start,end):
        score += i * int(currentState[i-start])
    return score
    
puzzleInput, currentState = parseFile('AoC 2018 Day 12 - input.txt')
start = 0
end = len(currentState)
counter = 0
previousState = ''
previousStart = 0
previousEnd = 0
while True:
    if counter % 100 == 0:
        previousState = currentState
        previousStart = start
        previousEnd = end
    currentState, start, end = nextGeneration(currentState, puzzleInput, start, end)
    counter += 1
    if currentState == previousState and end - start == previousEnd - previousStart:
        break
startDiff = counter - start
endDiff = end - counter

score = calculateScore(currentState,50000000000 - startDiff,50000000000 + endDiff)
print(score)

