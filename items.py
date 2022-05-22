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
    pantryFile = open("pantry.txt", "a")
    for i in range(len(pantryItems)):
        pantryFile.write(pantryItems[i] + ",")

def removeItems(pantryItems):
    if exists("pantry.txt"):
        pantryFile = open("pantry.txt", "r")
        pantry = pantryFile.read().split(",")

        for i in range(len(pantryItems)):
            if pantryItems[i] in pantry:
                pantry.remove(pantryItems[i])
    
        pantryFile = open("pantry.txt", "w")
        for i in range(len(pantry)):
            if pantry[i] != "":
                pantryFile.write(pantry[i] + ",")

def createShopList(neededItems):
    toBuy = []
    if exists("pantry.txt"):
        pantryFile = open("pantry.txt", "r")
        pantry = pantryFile.read().split(",")

    for i in neededItems:
        if i not in pantry:
            toBuy.append(i)
    return toBuy
