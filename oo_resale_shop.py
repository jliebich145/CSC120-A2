from computer import Computer
from typing import Optional

class ResaleShop():

    # What attributes will it need?
    inventory = []
    itemID = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID

    # What methods will you need?
    def buy(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.itemID += 1
        item = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.insert(self.itemID, item)
        return self

    def sell(self, ID):
        if ID <= self.itemID:
            if self.inventory[ID]!= "sold":
                self.inventory[ID] = "sold"
                print = "Computer Sold!"
            else:
                print("Computer ", ID, " not found. Please select another computer to sell.")
        else:
            print("Computer ", ID, " not found. Please select another computer to sell.")

    def refurbish(self):
        pass

test = ResaleShop([],0)
test.buy("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
test.sell(1)