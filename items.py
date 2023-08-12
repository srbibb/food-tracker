from os.path import exists

def handleInput(rawInput):
    processedInput = [] 
    for i in range(len(rawInput)):
        if rawInput[i] != "" and rawInput[i] != "\n":
            processedInput.append(rawInput[i].lower().strip())
    return processedInput

def createList(itemsList):
    items = handleInput(itemsList.split('\n'))
    return items

def writePantry(itemsList): 
    pantryFile = open("pantry.txt", "w")
    items = list(set(itemsList))
    for i in range(len(items)):
        if items[i] != "": 
            pantryFile.write(items[i] + ",")

def writeEssentials(itemsList): 
    essentialsFile = open("essentials.txt", "w")
    items = list(set(itemsList))
    for i in range(len(items)):
        if items[i] != "": 
            essentialsFile.write(items[i] + ",")

def createShopList(neededItems):
    toBuy = []
    if exists("pantry.txt"):
        pantryFile = open("pantry.txt", "r")
        pantry = pantryFile.read().split(",")

    if exists("essentials.txt"):
        essentialsFile = open("essentials.txt", "r")
        essentials = essentialsFile.read().split(",")

    for i in neededItems:
        if i not in pantry and i != "":
            toBuy.append(i)

    for i in essentials:
        if i not in pantry and i not in toBuy and i != "":
            toBuy.append(i)
    return toBuy
