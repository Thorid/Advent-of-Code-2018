from blist import blist

def marblesGameTurn(currentMarble, currentPosition, marbleArray, currentPlayer, playersScoreDict):
    if currentMarble % 23 == 0:
        for i in range(7):
            currentPosition -= 1
            if currentPosition < 0:
                currentPosition = len(marbleArray) - 1
        playersScoreDict[currentPlayer] += currentMarble + marbleArray[currentPosition]
        del marbleArray[currentPosition]
    else:
        for i in range(2):
            currentPosition += 1
            if currentPosition > len(marbleArray):
                currentPosition = 1
        marbleArray.insert(currentPosition, currentMarble)
    currentMarble += 1
    currentPlayer += 1
    return currentMarble, currentPosition, marbleArray, currentPlayer, playersScoreDict

currentMarble = 1
currentPosition = 0
marbleArray = blist([0])
currentPlayer = 0
numberOfTurns = 71436
numberOfPlayers = 466
playersScoreDict = {}
for i in range(1,numberOfPlayers+1):
    playersScoreDict[i] = 0
for j in range(numberOfTurns):
    currentMarble, currentPosition, marbleArray, currentPlayer, playersScoreDict = marblesGameTurn(currentMarble, currentPosition, marbleArray, currentPlayer, playersScoreDict)
    if currentPlayer > numberOfPlayers:
        currentPlayer = 1
print(max(playersScoreDict.values()))
