def createRecipes(recipesArray, elf1Position, elf2Position):
    nextRecipes = recipesArray[elf1Position] + recipesArray[elf2Position]
    if nextRecipes > 9:
        nextRecipes = str(nextRecipes)
        nextRecipe1 = int(nextRecipes[0])
        nextRecipe2 = int(nextRecipes[1])
        recipesArray.append(nextRecipe1)
        recipesArray.append(nextRecipe2)
        numberOfNewRecipes = 2
    else:
        recipesArray.append(nextRecipes)
        numberOfNewRecipes = 1
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
    return recipesArray, elf1Position, elf2Position, numberOfNewRecipes

recipesArray = [3,7]
elf1Position = 0
elf2Position = 1
recipesInput = '157901'
recipesString = '37'
while True:
    recipesArray, elf1Position, elf2Position, numberOfNewRecipes = createRecipes(recipesArray, elf1Position, elf2Position)
    if numberOfNewRecipes == 1:
        recipesString += str(recipesArray[-1])
    elif numberOfNewRecipes == 2:
        recipesString += str(recipesArray[-2])
        recipesString += str(recipesArray[-1])
    if recipesInput == recipesString[-len(recipesInput):]:
        result = len(recipesString.replace(recipesInput,''))
        break
    elif recipesInput == recipesString[-len(recipesInput)-1:-1]:
        result = len(recipesString.replace(recipesInput,'')) - 1
        break
print(result)

