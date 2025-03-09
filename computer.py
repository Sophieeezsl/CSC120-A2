"""
computer.py

Author: Sophie
Date: 2025.3

"""

class Computer:

    # What attributes will it need?
        #store information about the computer:

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    # What methods will you need?
    
    """
    Methods:
    - __init__()
    - update_price(new_price: int)
    - update_OS(new_os: str)
    - print_computer_info()
    """

    def update_price (self,newPrice:int): # ensuring newPrice is int.
        self.price = newPrice # update the price information stored
        print (f"The price is updated to ${self.price}") # pop up a message about change in price

    def update_OS (self,newOS:str): #
        self.operating_system = newOS #
        print (f"This is the new OS: {self.operating_system}")

    def print_computer_info(self):
        #I forgot the fstring so I asked gpt about the printing method.
        print(f"{self.description} \n {self.processor_type} \n {self.hard_drive_capacity}GB \n {self.memory}GB RAM \n {self.operating_system}\n {self.year_made}\n ${self.price}")


def main(): # use the computer (copied from main) to test it out
    computer1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHz 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    
    computer1.print_computer_info()


if __name__ == "__main__":
    main()

