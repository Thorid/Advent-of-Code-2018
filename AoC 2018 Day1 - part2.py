puzzleInput = open('AoC 2018 Day 1 - input.txt').read().split('\n')


def repeatedFrequency(calibrationInstructions):
    result = 0
    seen = set()
    calculatedInstructions = 0
    while True:
        for instruction in calibrationInstructions:
            number = int(instruction[1:])
            if instruction[0] == '+':
                result += number
            else:
                result -= number
            seen.add(result)
            calculatedInstructions += 1
            if len(seen) != calculatedInstructions:
                return result
    
print(repeatedFrequency(puzzleInput))
