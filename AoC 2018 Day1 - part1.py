puzzleInput = open('AoC 2018 Day 1 - input.txt').read().split('\n')


def calculateResultingFrequency(calibrationInstructions):
    result = 0
    for instruction in calibrationInstructions:
        number = int(instruction[1:])
        if instruction[0] == '+':
            result += number
        else:
            result -= number
    return result
    
print(calculateResultingFrequency(puzzleInput))
