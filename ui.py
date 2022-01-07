import tkinter as tk
from tkinter.constants import END
from items import addItems, removeItems, createPantryList, createShopList
from os.path import exists

pantryItems = []
if exists("pantry.txt"):
    pantryFile = open("pantry.txt", "r")
    pantry = pantryFile.read().split(",")
    for i in range(len(pantry)):
        if pantry[i] != "":
            pantryItems.append(pantry[i])

def back(hideWindow,showWindow):
    hideWindow.withdraw()
    showWindow.deiconify()

def retrieveItems(textBox,mode):
    itemsList = textBox.get("1.0",'end-1c')
    newItems = createPantryList(itemsList)
    pantryItems.extend(newItems)
    if mode == 0:
        addItems(newItems)
    elif mode == 1:
        removeItems(newItems)

def neededItems(textBox,toBuyWindow):
    itemsList = textBox.get("1.0",'end-1c')
    neededItems = createPantryList(itemsList)
    toBuy = createShopList(neededItems)
    toBuyWindow.withdraw()
    shopListWindow(toBuy)

def addWindow():
    addWindow = tk.Toplevel(root)
    root.withdraw()
    pantryText = tk.Text(addWindow, height=25, width=50)
    pantryText.pack(padx=10,pady=10)
    pantryInput = tk.Button(addWindow, text = "Enter items",command=lambda:retrieveItems(pantryText,0))
    pantryInput.pack(pady=10)
    backBtn = tk.Button(addWindow, text="Back",command=lambda:back(addWindow,root))
    backBtn.pack(pady=10)

def removeWindow():
    removeWindow = tk.Toplevel(root)
    root.withdraw()
    pantryText = tk.Text(removeWindow, height=25, width=52)
    pantryText.pack(padx=10,pady=10)
    pantryInput = tk.Button(removeWindow, text = "Remove items",command=lambda:retrieveItems(pantryText,1))
    pantryInput.pack(pady=10)
    backBtn = tk.Button(removeWindow, text="Back",command=lambda:back(removeWindow,root))
    backBtn.pack(pady=10)

def pantryWindow():
    viewWindow = tk.Toplevel(root)
    pantryLabel = tk.Label(viewWindow, text = "Pantry items")
    pantryLabel.pack()
    pantryText = tk.Text(viewWindow, height = 25, width = 52)
    pantryText.pack(padx=10,pady=10)
    if exists("pantry.txt"):
        pantryFile = open("pantry.txt", "r")
        pantry = pantryFile.read().split(",")
        for x in pantry:
            pantryText.insert(END, x + '\n')
    backBtn = tk.Button(viewWindow, text="Back",command=lambda:back(viewWindow,root))
    backBtn.pack(pady=10)

def toBuyWindow():
    toBuyWindow = tk.Toplevel(root)
    root.withdraw()
    toBuyLabel = tk.Label(toBuyWindow, text = "Please enter the items you need for this week's meals.")
    toBuyLabel.pack()
    toBuyText = tk.Text(toBuyWindow, height = 25, width = 52)
    toBuyText.pack(padx=10,pady=10)
    toBuyInput = tk.Button(toBuyWindow, text = "Enter items",command=lambda:neededItems(toBuyText,toBuyWindow))
    toBuyInput.pack(pady=10)
    backBtn = tk.Button(toBuyWindow, text="Back",command=lambda:back(toBuyWindow,root))
    backBtn.pack(pady=10)

def shopListWindow(toBuy):
    shopListWindow = tk.Toplevel(root)
    shopListLabel = tk.Label(shopListWindow, text = "Here is your shopping list.")
    shopListLabel.pack()
    shopListText = tk.Text(shopListWindow, height = 5, width = 52)
    shopListText.pack(padx=10,pady=10)
    for x in toBuy:
            shopListText.insert(END, x + '\n')
    closeBtn = tk.Button(shopListWindow, text="Close",command=lambda:back(shopListWindow,root))
    closeBtn.pack(pady=10)

root = tk.Tk()
addBtn = tk.Button(root, text="Add items to pantry", command=addWindow)
addBtn.pack(pady=10)
removeBtn = tk.Button(root, text="Remove items from pantry", command=removeWindow)
removeBtn.pack(padx=10,pady=10)
viewBtn = tk.Button(root, text="View items in pantry", command=pantryWindow)
viewBtn.pack(pady=10)
createListBtn = tk.Button(root, text="Create shopping list", command=toBuyWindow)
createListBtn.pack(pady=10)
quitBtn = tk.Button(root, text="Quit",command=quit)
quitBtn.pack(pady=10)

root.mainloop()