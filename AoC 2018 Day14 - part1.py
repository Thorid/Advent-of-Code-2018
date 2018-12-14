def createRecipes(recipesArray, elf1Position, elf2Position):
    nextRecipes = recipesArray[elf1Position] + recipesArray[elf2Position]
    if nextRecipes > 9:
        nextRecipes = str(nextRecipes)
        nextRecipe1 = int(nextRecipes[0])
        nextRecipe2 = int(nextRecipes[1])
        recipesArray.append(nextRecipe1)
        recipesArray.append(nextRecipe2)
    else:
        recipesArray.append(nextRecipes)
    changePosition1 = recipesArray[elf1Position] + 1
    changePosition2 = recipesArray[elf2Position] + 1
    for i in range(changePosition1):
        elf1Position += 1
        if elf1Position > len(recipesArray) - 1:
            elf1Position = 0
    for j in range(changePosition2):
        elf2Position += 1
        if elf2Position > len(recipesArray) - 1:
            elf2Position = 0
    return recipesArray, elf1Position, elf2Position

def calculateScore(recipesArray, numberOfRecipes):
    score = ''
    for i in range(numberOfRecipes,numberOfRecipes+10):
        score += str(recipesArray[i])
    return score

recipesArray = [3,7]
elf1Position = 0
elf2Position = 1
numberOfRecipes = 157901
while True:
    recipesArray, elf1Position, elf2Position = createRecipes(recipesArray, elf1Position, elf2Position)
    if len(recipesArray) >= numberOfRecipes + 10:
        break
print(calculateScore(recipesArray, numberOfRecipes))
