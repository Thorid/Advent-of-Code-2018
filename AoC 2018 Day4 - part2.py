puzzleInput = open('AoC 2018 Day 4 - input.txt').read().split('\n')
puzzleInput.sort()
countAsleepMinute = 0
guardsArray = []

# put every guard to list
for i in range(len(puzzleInput)):
    if 'Guard' in puzzleInput[i]:
        guardID = puzzleInput[i][puzzleInput[i].index('#')+1:puzzleInput[i].index(' b')]
        if guardID not in guardsArray:
            guardsArray.append(guardID)

# look for guard which has slept most times on certain minute
for guard in guardsArray:
    asleepMinutes = {}
    currentGuard = False
    for i in range(len(puzzleInput)):
        if 'Guard #' + guard in puzzleInput[i]:
            tempGuardID = puzzleInput[i][puzzleInput[i].index('#')+1:puzzleInput[i].index(' b')]
            currentGuard = True
        elif 'asleep' in puzzleInput[i] and currentGuard == True:
            sleepStart = puzzleInput[i][puzzleInput[i].index(':')+1:puzzleInput[i].index(']')]
        elif 'wakes' in puzzleInput[i] and currentGuard == True:
            sleepEnd = puzzleInput[i][puzzleInput[i].index(':')+1:puzzleInput[i].index(']')]
            for k in range(int(sleepStart),int(sleepEnd)):
                if k in asleepMinutes.keys():
                    asleepMinutes[k] += 1
                else:
                    asleepMinutes[k] = 1
        else:
            currentGuard = False
    try:
        tempCountAsleepMinute = max(asleepMinutes.values())
    except:
        tempCountAsleepMinute = 0
    if tempCountAsleepMinute > countAsleepMinute:
        countAsleepMinute = tempCountAsleepMinute
        GuardID = tempGuardID

# look for minute chosen guard has slept most times
asleepMinutes = {}
currentGuard = False
for j in range(len(puzzleInput)):
    if 'Guard #' + GuardID in puzzleInput[j]:
        currentGuard = True
    elif 'asleep' in puzzleInput[j] and currentGuard == True:
        sleepStart = puzzleInput[j][puzzleInput[j].index(':')+1:puzzleInput[j].index(']')]
    elif 'wakes' in puzzleInput[j] and currentGuard == True:
        sleepEnd = puzzleInput[j][puzzleInput[j].index(':')+1:puzzleInput[j].index(']')]
        for k in range(int(sleepStart),int(sleepEnd)):
            if k in asleepMinutes.keys():
                asleepMinutes[k] += 1
            else:
                asleepMinutes[k] = 1
    else:
        currentGuard = False
for key,value in asleepMinutes.items():
    if value == max(asleepMinutes.values()):
        mostAsleepMinute = key

result = int(GuardID) * mostAsleepMinute
print(result)





