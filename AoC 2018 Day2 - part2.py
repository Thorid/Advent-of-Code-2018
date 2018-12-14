puzzleInput = open('AoC 2018 Day 2 - input.txt').read().split('\n')

def commonLetters(boxesID):
    diffCount = 0
    similarArray = []
    result = ''
    for i in range(len(boxesID)):
        for k in range(len(boxesID)):
            if i == k:
                break
            for j in range(len(boxesID[i])):
                if boxesID[i][j] != boxesID[k][j]:
                    diffCount += 1
            if diffCount == 1:
                similarArray.append(boxesID[i])
                similarArray.append(boxesID[k])
            diffCount = 0
    for m in range(len(similarArray[0])):
        if similarArray[0][m] == similarArray[1][m]:
            result += similarArray[0][m]
    return result
        

        

print(commonLetters(puzzleInput))
