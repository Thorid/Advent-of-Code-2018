puzzleInput = open('AoC 2018 Day 5 - input.txt').read()

letterSet = set()
polymerLen = []
for letter in puzzleInput:
    letterSet.add(letter.lower())

letterArray = list(letterSet)
for letter in letterArray:
    tempPuzzleInput = puzzleInput
    tempPuzzleInput = tempPuzzleInput.replace(letter,'')
    tempPuzzleInput = tempPuzzleInput.replace(letter.upper(),'')
    i = 0
    while i < len(tempPuzzleInput)-1:
        if tempPuzzleInput[i].casefold() == tempPuzzleInput[i+1].casefold():
            if tempPuzzleInput[i] != tempPuzzleInput[i+1]:
                tempPuzzleInput = tempPuzzleInput.replace(tempPuzzleInput[i] + tempPuzzleInput[i+1],'')
                i = 0
        i += 1          
    polymerLen.append(len(tempPuzzleInput))
print(min(polymerLen))


