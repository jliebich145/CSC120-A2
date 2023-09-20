#Attributes andConstructor written in partnership with Mattea
# Computer Class creates computers
class Computer:

    # attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Constructor
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # Formatting to test computer class in resale shop
    def __str__(self):
        return f"Description: {self.description} \nProcessor Type: {self.processor_type} \nHard Drive Capacity: {self.hard_drive_capacity} \nMemory: {self.memory} \nOperating System: {self.operating_system} \nYear Made: {self.year_made} \nPrice: {self.price}"

    # Methods

    # Updates the price of a computer
    def update_price(self, new_price: int):
        self.price = new_price

    #Updates the operating system of a computer
    def update_os(self, new_os: str):
        self.operating_system = new_os