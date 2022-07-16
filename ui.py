import tkinter as tk
from tkinter.constants import END
from items import createPantryList, createShopList, writePantry
from os.path import exists 

pantryItems = [] 
if exists("pantry.csv"):
    pantryFile = open("pantry.csv", "r")
    pantry = pantryFile.read().split(",")
    for i in range(len(pantry)):
        if pantry[i] != "" and pantry[i] != "\n":
            pantryItems.append(pantry[i])

def back(hideWindow,showWindow):
    hideWindow.withdraw()
    showWindow.deiconify() 

def retrieveItems(textBox):
    global pantryItems
    itemsList = textBox.get("1.0",'end-1c')
    pantryItems = createPantryList(itemsList)
    writePantry(pantryItems)

def neededItems(textBox,toBuyWindow):
    itemsList = textBox.get("1.0",'end-1c')
    neededItems = createPantryList(itemsList)
    toBuy = createShopList(neededItems)

    pantryFile = open("shopping list.csv", "w")
    for i in range(len(toBuy)):
        if toBuy[i] != "":
            pantryFile.write(toBuy[i] + ",")

    toBuyWindow.withdraw()
    shopListWindow(toBuy)

def addWindow():
    addWindow = tk.Toplevel(root)
    root.withdraw()
    pantryText = tk.Text(addWindow, height=25, width=50)
    pantryText.pack(padx=10,pady=10)
    pantryInput = tk.Button(addWindow, text = "Enter items",command=lambda:[retrieveItems(pantryText,0),back(addWindow,root)])
    pantryInput.pack(pady=10)
    backBtn = tk.Button(addWindow, text="Back",command=lambda:back(addWindow,root))
    backBtn.pack(pady=10)

def pantryWindow():
    pantryWindow = tk.Toplevel(root)
    pantryLabel = tk.Label(pantryWindow, text = "Pantry items")
    pantryLabel.pack()
    pantryText = tk.Text(pantryWindow, height = 25, width = 52)
    pantryText.pack(padx=10,pady=10)
    if exists("pantry.csv"):
        pantryFile = open("pantry.csv", "r")
        pantry = pantryFile.read().split(",")
        for x in pantry:
            pantryText.insert(END, x + '\n')
    pantryInput = tk.Button(pantryWindow, text = "Update list",command=lambda:[retrieveItems(pantryText),back(pantryWindow,root)])
    pantryInput.pack(pady=10)
    backBtn = tk.Button(pantryWindow, text="Back",command=lambda:back(pantryWindow,root))
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
viewBtn = tk.Button(root, text="View and edit pantry", command=pantryWindow)
viewBtn.pack(padx = 10, pady=10)
createListBtn = tk.Button(root, text="Create shopping list", command=toBuyWindow)
createListBtn.pack(pady=10)
quitBtn = tk.Button(root, text="Quit",command=quit)
quitBtn.pack(pady=10)

root.mainloop()