def generateFuelCellMap(serialNumber):
    fuelCellMap = {}
    for y in range(1,301):
        for x in range(1,301):
            rackID = x + 10
            powerLevelStart = rackID * y
            additionSerialNumber = powerLevelStart + serialNumber
            multiplyRackID = additionSerialNumber * rackID
            hundreds = str(multiplyRackID)[-3]
            fuelCell = int(hundreds) - 5
            fuelCellMap[(x,y)] = fuelCell
    return fuelCellMap


def findCellMaxTotalPower(fuelCellMap):
    totalPower = 0
    for squareSize in range(1,301):
        for y in range(1,301-squareSize):
            for x in range(1,301-squareSize):
                currentTotalPower = 0
                for z in range(squareSize):
                    for w in range(squareSize):
                        currentTotalPower += fuelCellMap[(x+z,y+w)]
                if currentTotalPower > totalPower:
                    totalPower = currentTotalPower
                    topLeftCell = (x,y,squareSize)
    return topLeftCell

serialNumber = 4455
fuelCellMap = generateFuelCellMap(serialNumber)
print(findCellMaxTotalPower(fuelCellMap))
