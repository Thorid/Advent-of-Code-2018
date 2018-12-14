puzzleInput = open('AoC 2018 Day 2 - input.txt').read().split('\n')

def checkSum(boxesID):
    countTwo, countThree = 0, 0
    for ID in boxesID:
        numberOfLetters = {}
        for i in range(len(ID)):
            if ID[i] in numberOfLetters:
                numberOfLetters[ID[i]] += 1
            else:
                numberOfLetters[ID[i]] = 1
        if 2 in numberOfLetters.values():
            countTwo += 1
        if 3 in numberOfLetters.values():
            countThree += 1
    result = countTwo * countThree
    return result

print(checkSum(puzzleInput))
