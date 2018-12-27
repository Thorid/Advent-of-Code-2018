import ast

def parseSamples(file):
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

def parseInstructions(file):
    testProgram = []
    fileArray = open(file).read().split('\n')
    lastEmptyStringIndex = len(fileArray) - 1 - fileArray[::-1].index('')
    tempTestProgram = fileArray[lastEmptyStringIndex + 1:]
    for line in tempTestProgram:
        instruction = line.split(' ')
        instruction = list(map(int, instruction))
        testProgram.append(tuple(instruction))
    return testProgram

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

def checkOpcodesNumbers(before, instruction, after, opcodesDict):
    possibleInstructionsArray = []
    if after == addr(before, instruction) and 'addr' not in opcodesDict.values():
        possibleInstructionsArray.append('addr')
    if after == addi(before, instruction) and 'addi' not in opcodesDict.values():
        possibleInstructionsArray.append('addi')
    if after == mulr(before, instruction) and 'mulr' not in opcodesDict.values():
        possibleInstructionsArray.append('mulr')
    if after == muli(before, instruction) and 'muli' not in opcodesDict.values():
        possibleInstructionsArray.append('muli')
    if after == banr(before, instruction) and 'banr' not in opcodesDict.values():
        possibleInstructionsArray.append('banr')
    if after == bani(before, instruction) and 'bani' not in opcodesDict.values():
        possibleInstructionsArray.append('bani')
    if after == borr(before, instruction) and 'borr' not in opcodesDict.values():
        possibleInstructionsArray.append('borr')
    if after == bori(before, instruction) and 'bori' not in opcodesDict.values():
        possibleInstructionsArray.append('bori')
    if after == setr(before, instruction) and 'setr' not in opcodesDict.values():
        possibleInstructionsArray.append('setr')
    if after == seti(before, instruction) and 'seti' not in opcodesDict.values():
        possibleInstructionsArray.append('seti')
    if after == gtir(before, instruction) and 'gtir' not in opcodesDict.values():
        possibleInstructionsArray.append('gtir')
    if after == gtri(before, instruction) and 'gtri' not in opcodesDict.values():
        possibleInstructionsArray.append('gtri')
    if after == gtrr(before, instruction) and 'gtrr' not in opcodesDict.values():
        possibleInstructionsArray.append('gtrr')
    if after == eqir(before, instruction) and 'eqir' not in opcodesDict.values():
        possibleInstructionsArray.append('eqir')
    if after == eqri(before, instruction) and 'eqri' not in opcodesDict.values():
        possibleInstructionsArray.append('eqri')
    if after == eqrr(before, instruction) and 'eqrr' not in opcodesDict.values():
        possibleInstructionsArray.append('eqrr')
    if len(possibleInstructionsArray) == 1:
        opcodesDict[instruction[0]] = possibleInstructionsArray[0]
    return opcodesDict

def executeInstruction(register, instruction, opcodesDict):
    opcode = opcodesDict[instruction[0]]
    if opcode == 'addr':
        newRegister = addr(register, instruction)
    elif opcode == 'addi':
        newRegister = addi(register, instruction)
    elif opcode == 'mulr':
        newRegister = mulr(register, instruction)
    elif opcode == 'muli':
        newRegister = muli(register, instruction)
    elif opcode == 'banr':
        newRegister = banr(register, instruction)
    elif opcode == 'bani':
        newRegister = bani(register, instruction)
    elif opcode == 'borr':
        newRegister = borr(register, instruction)
    elif opcode == 'bori':
        newRegister = bori(register, instruction)
    elif opcode == 'setr':
        newRegister = setr(register, instruction)
    elif opcode == 'seti':
        newRegister = seti(register, instruction)
    elif opcode == 'gtir':
        newRegister = gtir(register, instruction)
    elif opcode == 'gtri':
        newRegister = gtri(register, instruction)
    elif opcode == 'gtrr':
        newRegister = gtrr(register, instruction)
    elif opcode == 'eqir':
        newRegister = eqir(register, instruction)
    elif opcode == 'eqri':
        newRegister = eqri(register, instruction)
    elif opcode == 'eqrr':
        newRegister = eqrr(register, instruction)
    return newRegister

opcodesDict = {}
register = [0, 0, 0, 0]
beforeArray, instructionsArray, afterArray = parseSamples('AoC 2018 Day 16 - input.txt')
testProgram = parseInstructions('AoC 2018 Day 16 - input.txt')
while len(opcodesDict) < 16:
    for i in range(len(beforeArray)):
        opcodesDict = checkOpcodesNumbers(beforeArray[i],instructionsArray[i],afterArray[i], opcodesDict)
for instruction in testProgram:
    register = executeInstruction(register, instruction, opcodesDict)
print(register[0])


