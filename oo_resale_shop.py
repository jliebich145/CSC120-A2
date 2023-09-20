from computer import Computer
from typing import Optional
#Attributes, Constructor, and Buy Method written in partnership with Mattea
#Creates a Resale Shop
class ResaleShop():

    # Attributes
    inventory = []
    itemID = 0

    # Constructor
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID

    # Methods

    #Creates a computer object, buys the computer, and adds it to the inventory
    def buy(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.itemID += 1
        item = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.insert(self.itemID, item)
        print("New computer bought and added to inventory!\n", item, "\nItem ID:", self.itemID)

    #Sells a computer based on ID
    def sell(self, id):
        if id <= self.itemID:
            if self.inventory[id-1]!= "sold":
                computer = self.inventory[id-1]
                print("Computer Sold! Price:", computer.price)
                self.inventory[id-1] = "sold"
            else:
                print("Computer ", id, " not found. Please select another computer to sell.")
        else:
            print("Computer ", id, " not found. Please select another computer to sell.")

    #Reprices a computer based on its age and optionally updates the operating system
    def refurbish(self, id, new_os: Optional[str]= None):
        if id <= self.itemID and self.inventory[id-1]!= "sold":
            computer = self.inventory[id-1]
            if computer.year_made < 2000:
                computer.update_price(0)
            elif computer.year_made < 2012:
                computer.update_price(250)
            elif computer.year_made < 2018:
                computer.update_price(550)
            else:
                computer.update_price(1000)

            if new_os is not None:
                computer.update_os(new_os) 
        else:
            print("Item", id, "not found. Please select another item to refurbish.")

#Testing
def main():
    store = ResaleShop([],0)
    store.buy("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    store.refurbish(1)
    store.sell(1)

main()