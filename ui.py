import tkinter as tk
from tkinter.constants import END
from items import createList, createShopList, writeEssentials, writePantry
from os.path import exists 

pantryItems = [] 
if exists("pantry.txt"):
    pantryFile = open("pantry.txt", "r")
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
    pantryItems = createList(itemsList)
    writePantry(pantryItems)

def retrieveEssentials(textBox):
    essentials = textBox.get("1.0",'end-1c')
    essentialsList = createList(essentials)
    writeEssentials(essentialsList)

def neededItems(textBox,toBuyWindow):
    itemsList = textBox.get("1.0",'end-1c')
    neededItems = createList(itemsList)
    toBuy = createShopList(neededItems)

    pantryFile = open("shopping list.txt", "w")
    for i in range(len(toBuy)):
        if toBuy[i] != "":
            pantryFile.write(toBuy[i] + ",")

    toBuyWindow.withdraw()
    shopListWindow(toBuy)

def pantryWindow():
    pantryWindow = tk.Toplevel(root)
    #pantryWindow.geometry('500x600+0+0')
    pantryLabel = tk.Label(pantryWindow, text = "Pantry items")
    pantryLabel.pack()
    pantryText = tk.Text(pantryWindow, height = 25, width = 52)
    pantryText.pack(padx=10,pady=10)
    if exists("pantry.txt"):
        pantryFile = open("pantry.txt", "r")
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

def essentialsWindow():
    essentialsWindow = tk.Toplevel(root)
    essentialsLabel = tk.Label(essentialsWindow, text = "Essential items")
    essentialsLabel.pack()
    essentialsText = tk.Text(essentialsWindow, height = 25, width = 52)
    essentialsText.pack(padx=10,pady=10)
    if exists("essentials.txt"):
        essentialFile = open("essentials.txt", "r")
        items = essentialFile.read().split(",")
        for x in items:
            essentialsText.insert(END, x + '\n')
    essentialsInput = tk.Button(essentialsWindow, text = "Update list",command=lambda:[retrieveEssentials(essentialsText),back(essentialsWindow,root)])
    essentialsInput.pack(pady=10)
    backBtn = tk.Button(essentialsWindow, text="Back",command=lambda:back(essentialsWindow,root))
    backBtn.pack(pady=10)

root = tk.Tk()
viewBtn = tk.Button(root, text="View and edit pantry", command=pantryWindow)
viewBtn.pack(pady=10)
createListBtn = tk.Button(root, text="Create shopping list", command=toBuyWindow)
createListBtn.pack(pady=10)
essentialsBtn = tk.Button(root, text="View and edit essentials list", command=essentialsWindow)
essentialsBtn.pack(padx = 25, pady=10)
quitBtn = tk.Button(root, text="Quit",command=quit)
quitBtn.pack(pady=10)

root.mainloop()