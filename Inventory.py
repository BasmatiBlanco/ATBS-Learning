# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
       item_total += v
       print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x, 0)
        inventory[x] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)