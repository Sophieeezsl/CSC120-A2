from computer import * #import 

class ResaleShop:

    # What attributes will it need?
    # buy computer
    # sell computer
    # change computer information
    # check inverntory
    
#I asked GPT for advice here: instead of using [](list), it suggesed me to use dictionary
#Because I want to quickly find a piece of information stored and maybe delete it. List is too orderly thus not suitable
#Dictionary is orderless but suitable for this task

    inventory = {} 
    computer_count = {} #track amount of computer for each description

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self):
        
        self.inventory = {} 
        self.computer_count = {} #track amount of computer for each description

    # What methods will you need?

    def buy(self, computer: Computer):
        
        # Check if the description already exists in the inventory
        if computer.description in self.inventory:
            self.computer_count[computer.description] += 1  # Increase count
        else:
            self.inventory[computer.description] = computer  # Add a new computer
            self.computer_count[computer.description] = 1  # Start with 1 unit
        print(f"Added {computer.description} to inventory.")
    
    def sell(self, computer: Computer):
        if computer.description in self.inventory:
            self.computer_count[computer.description] -= 1  # Decrease count
            if self.computer_count[computer.description] == 0:
                del self.inventory[computer.description]  # Remove from inventory if count is 0
                del self.computer_count[computer.description]
            print(f"{computer.description} has been sold.")
        else:
            print(f"There is no {computer.description} in the inventory.")

    def print_inventory(self):
        for description, computer in self.inventory.items():
            print(f"{description}: {self.computer_count[description]} in stock")

    
    def refurbish(self, computer:Computer, description):
    # Check if the computer exists in the inventory by description
        if description in self.inventory:
            # Access the computer from inventory
            computer = self.inventory[description]

            # Refurbish the computer based on the year it was made
            if computer.year_made < 2000:
                computer.price = 0  # Too old to sell, donation only
            elif computer.year_made < 2012:
                computer.price = 250  # Heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550  # Discounted price on machines 4-to-10 years old
            else:
                computer.price = 1000  # Recent stuff

            print(f"Refurbished {computer.description}, new price: ${computer.price}")
        else:
            print(f"{description} is not in inventory.")

def main():
    # Create a resale shop instance
    shop = ResaleShop()

    # Create a computer object
    computer1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHz 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Add the computer to the inventory
    print("Buying computer1...")
    computer_id = shop.buy(computer1)

    # Print inventory
    shop.print_inventory()

    # Refurbish the computer
    print("\nRefurbishing computer1...")
    shop.refurbish(computer_id, "MacOS Monterey")

    # Print inventory after refurbishing
    shop.print_inventory()

    # Sell the computer
    print("\nSelling computer1...")
    shop.sell(computer_id)

    # Print inventory after selling
    shop.print_inventory()

if __name__ == "__main__":
    main()