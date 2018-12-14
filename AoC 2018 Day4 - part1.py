puzzleInput = open('AoC 2018 Day 4 - input.txt').read().split('\n')
puzzleInput.sort()
guardNapTime = {}

# look for guard that has slept for most time
for i in range(len(puzzleInput)):
    if 'Guard' in puzzleInput[i]:
        guardID = puzzleInput[i][puzzleInput[i].index('#')+1:puzzleInput[i].index(' b')]
    elif 'asleep' in puzzleInput[i]:
        sleepStart = puzzleInput[i][puzzleInput[i].index(':')+1:puzzleInput[i].index(']')]
    elif 'wakes' in puzzleInput[i]:
        sleepEnd = puzzleInput[i][puzzleInput[i].index(':')+1:puzzleInput[i].index(']')]
        napTime = int(sleepEnd) - int(sleepStart)
        if guardID in guardNapTime.keys():
            guardNapTime[guardID] += napTime
        else:
            guardNapTime[guardID] = napTime
for key,value in guardNapTime.items():
    if value == max(guardNapTime.values()):
        laziestGuard = key

#look for minute in which chosen guard was most often asleep        
asleepMinutes = {}
for j in range(len(puzzleInput)):
    if 'Guard #' + laziestGuard in puzzleInput[j]:
        laziestGuardAction = True
    elif 'asleep' in puzzleInput[j] and laziestGuardAction == True:
        sleepStart = puzzleInput[j][puzzleInput[j].index(':')+1:puzzleInput[j].index(']')]
    elif 'wakes' in puzzleInput[j] and laziestGuardAction == True:
        sleepEnd = puzzleInput[j][puzzleInput[j].index(':')+1:puzzleInput[j].index(']')]
        for k in range(int(sleepStart),int(sleepEnd)):
            if k in asleepMinutes.keys():
                asleepMinutes[k] += 1
            else:
                asleepMinutes[k] = 1
    else:
        laziestGuardAction = False
for key,value in asleepMinutes.items():
    if value == max(asleepMinutes.values()):
        mostAsleepMinute = key

result = int(laziestGuard) * mostAsleepMinute
print(result)



