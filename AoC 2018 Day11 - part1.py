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
    for y in range(1,299):
        for x in range(1,299):
            currentTotalPower = fuelCellMap[(x,y)] + fuelCellMap[(x+1,y)] + fuelCellMap[(x+2,y)] + fuelCellMap[(x,y+1)] + fuelCellMap[(x+1,y+1)] + fuelCellMap[(x+2,y+1)] + fuelCellMap[(x,y+2)] + fuelCellMap[(x+1,y+2)] + fuelCellMap[(x+2,y+2)]
            if currentTotalPower > totalPower:
                totalPower = currentTotalPower
                topLeftCell = (x,y)
    return topLeftCell

serialNumber = 4455
fuelCellMap = generateFuelCellMap(serialNumber)
print(findCellMaxTotalPower(fuelCellMap))


