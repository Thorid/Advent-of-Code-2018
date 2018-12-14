puzzleInput = open('AoC 2018 Day 5 - input.txt').read()
i = 0
while i < len(puzzleInput)-1:
    if puzzleInput[i].casefold() == puzzleInput[i+1].casefold():
        if puzzleInput[i] !=  puzzleInput[i+1]:
            puzzleInput = puzzleInput.replace(puzzleInput[i] + puzzleInput[i+1],'')
            i = 0
    i += 1          
print(len(puzzleInput))
