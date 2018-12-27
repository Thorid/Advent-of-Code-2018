import ast

def parseInput(file):
    fileArray = open(file).read().split('\n')
    beforeArray, instructionsArray, afterArray = [], [], []
    for line in fileArray:
        if 'Before' in line:
            tempLine = line[line.index(':')+2:]
            tempLine = ast.literal_eval(tempLine)
            beforeArray.append(tuple(tempLine))
        elif 'After' in line:
            tempLine = line[line.index(':')+3:]
            tempLine = ast.literal_eval(tempLine)
            afterArray.append(tuple(tempLine))
        elif len(instructionsArray) < len(beforeArray):
            tempLine = line.split(' ')
            tempLine = list(map(int, tempLine))
            instructionsArray.append(tuple(tempLine))
    return beforeArray, instructionsArray, afterArray

def addr(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] + array[B]
    return tuple(array)

def addi(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] + B
    return tuple(array)

def mulr(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] * array[B]
    return tuple(array)

def muli(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] * B
    return tuple(array)

def banr(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] & array[B]
    return tuple(array)

def bani(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] & B
    return tuple(array)

def borr(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] | array[B]
    return tuple(array)

def bori(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    array[C] = array[A] | B
    return tuple(array)

def setr(array, instruction):
    array = list(array)
    A = instruction[1]
    C = instruction[3]
    array[C] = array[A]
    return tuple(array)

def seti(array, instruction):
    array = list(array)
    A = instruction[1]
    C = instruction[3]
    array[C] = A
    return tuple(array)

def gtir(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    if A > array[B]:
        array[C] = 1
    else:
        array[C] = 0
    return tuple(array)

def gtri(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    if array[A] > B:
        array[C] = 1
    else:
        array[C] = 0
    return tuple(array)

def gtrr(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    if array[A] > array[B]:
        array[C] = 1
    else:
        array[C] = 0
    return tuple(array)

def eqir(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    if A == array[B]:
        array[C] = 1
    else:
        array[C] = 0
    return tuple(array)

def eqri(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    if array[A] == B:
        array[C] = 1
    else:
        array[C] = 0
    return tuple(array)

def eqrr(array, instruction):
    array = list(array)
    A = instruction[1] 
    B = instruction[2]
    C = instruction[3]
    if array[A] == array[B]:
        array[C] = 1
    else:
        array[C] = 0
    return tuple(array)

def checkPossibleInstrutions(before, instruction, after):
    possibleInstructions = 0
    if after == addr(before, instruction):
        possibleInstructions += 1
    if after == addi(before, instruction):
        possibleInstructions += 1
    if after == mulr(before, instruction):
        possibleInstructions += 1
    if after == muli(before, instruction):
        possibleInstructions += 1
    if after == banr(before, instruction):
        possibleInstructions += 1
    if after == bani(before, instruction):
        possibleInstructions += 1
    if after == borr(before, instruction):
        possibleInstructions += 1
    if after == bori(before, instruction):
        possibleInstructions += 1
    if after == setr(before, instruction):
        possibleInstructions += 1
    if after == seti(before, instruction):
        possibleInstructions += 1
    if after == gtir(before, instruction):
        possibleInstructions += 1
    if after == gtri(before, instruction):
        possibleInstructions += 1
    if after == gtrr(before, instruction):
        possibleInstructions += 1
    if after == eqir(before, instruction):
        possibleInstructions += 1
    if after == eqri(before, instruction):
        possibleInstructions += 1
    if after == eqrr(before, instruction):
        possibleInstructions += 1
    return possibleInstructions


beforeArray, instructionsArray, afterArray = parseInput('AoC 2018 Day 16 - input.txt')
result = 0
for i in range(len(beforeArray)):
    possibleInstructions = checkPossibleInstrutions(beforeArray[i],instructionsArray[i],afterArray[i])
    if possibleInstructions >= 3:
        result += 1
print(result)

