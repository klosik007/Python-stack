def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))
    
def addToInventory(inventory, addedItems):
    num = 0
    for i in range(len(addedItems)):
        #print(addedItems[i])
        num = inventory.get(addedItems[i], 0) + 1
        inventory[addedItems[i]] = num
        #print(inventory.items())
    return inventory
    
        
        

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

#print (inv)
displayInventory(inv)
