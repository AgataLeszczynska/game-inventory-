import json
from tabulate import tabulate

inventory = {"gold coin": 45, "arrow": 12, "torch": 6, "dagger": 50, "rope": 1, "ruby": 1}

dictionary = {}


def display_inventory(inventory):

    password = "password"
    start = input("Please type in 'password' and enter the inventory: ")
    print(start)

    if password == "password":
        print(json.dumps(inventory, indent=4,  separators=(',\n', ': ')))
    else:
        print("Please try again")

#display_inventory(inventory)
#display_inventory(dictionary)


def add_to_inventory(inventory, *added_items):
    for element in added_items:
        #print(element)
        if element in inventory:
            inventory[element] += 1
        else:
            inventory.update({element: 1})


add_to_inventory(inventory, "super_jump", "thor mode", "thor mode", "flying", "super jump")
#print(json.dumps(inventory, indent=4,  separators=(',\n', ': ')))


def remove_from_inventory(inventory, *removed_items):
    for element in removed_items:
        #print(element)
        if element in inventory:
            inventory[element] -= 1
            if inventory[element] == 0:
                del inventory[element]
        else:
            pass


remove_from_inventory(inventory, "super_jump", "thor mode")
# print(json.dumps(inventory, indent=4,  separators=(',\n', ': ')))


def print_table(inventory, order):
    rows = ["Item", "Counter"]
    #`count,asc
    if order == "count_asc":  
        print(tabulate(sorted(inventory.items(), key=lambda x: x[1]), headers=rows))
        #`count,dsc
    elif order == "count_dsc":
        print(tabulate(sorted(inventory.items(), key=lambda x: x[1], reverse=True), headers=rows))
    #empty
    elif order == "empty":
        print(tabulate(inventory.items(), headers=rows))

print_table(inventory, "count_dsc")

import csv 
rows = ["Item", "Counter"]
#inventory = {"rope" : 1}
def import_inventory(inventory, filename = None):
    if filename == None:
        filename == "items.csv"
    with open('items.csv', mode='r') as file:
        reader = csv.reader(file)
        inventory1 = {rows[0]:rows[1] for rows in reader}
        for element in inventory1:
            if element in inventory:
                inventory[element] +=1
            else:
                inventory.update({element : 1})
    return inventory
inventory = import_inventory(inventory)
print(tabulate(inventory.items(), headers=rows))

def export_inventory(inventory, filename = None):
    if filename == None:
        filename == "exported.csv"
    with open('exported.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = rows)
        writer.writeheader()
        for key in inventory.keys():
            if inventory[key] > 1:
                file.write("%s, %s\n" % (key, inventory[key]))

export_inventory(inventory,)