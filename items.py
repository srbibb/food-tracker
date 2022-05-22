from os.path import exists

def handleInput(rawInput):
    processedInput = []
    for i in range(len(rawInput)):
        if rawInput[i] != "" and rawInput[i] != "\n":
            processedInput.append(rawInput[i].lower().strip())
    return processedInput

def createPantryList(itemsList):
    pantryItems = handleInput(itemsList.split('\n'))
    return pantryItems

def addItems(pantryItems):
    writePantry(pantryItems)

def removeItems(pantryItems):
    if exists("pantry.csv"):
        pantryFile = open("pantry.csv", "r")
        pantry = pantryFile.read().split(",")

        for i in range(len(pantryItems)):
            if pantryItems[i] in pantry:
                pantry.remove(pantryItems[i])
    
        writePantry(pantry)

def writePantry(items): 
    pantryFile = open("pantry.csv", "w")
    for i in range(len(items)):
        if items[i] != "": 
            pantryFile.write(items[i] + ",")

def createShopList(neededItems):
    toBuy = []
    if exists("pantry.csv"):
        pantryFile = open("pantry.csv", "r")
        pantry = pantryFile.read().split(",")

    for i in neededItems:
        if i not in pantry:
            toBuy.append(i)
    return toBuy
