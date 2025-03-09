"""
resale_shop.py

Author: Sophie
Date: 2025.3
"""

from computer import Computer

class ResaleShop:

    # What attributes will it need?
    # buy computer
    # sell computer
    # change computer information
    # check inverntory
    
    inventory = [] 

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    Methods:
    - __init__(): Initializes an empty inventory.
    - buy(computer: Computer) -> str: 
    - sell(description: str)
    - refurbish(description: str, new_os: str)
    - print_inventory()

    """

    def __init__(self):
        self.inventory = [] 

    def buy(self, computer: Computer):
        self.inventory.append(computer) 
        print(f"Added {computer.description} to inventory.")
        return computer.description 

    def sell(self, description):
        for computer in self.inventory:
            if computer.description == description:
                self.inventory.remove(computer)
                print(f"{description} has been sold.")
                return
        print(f"There is no {description} in the inventory.")

    def refurbish(self, description, new_os):
        for computer in self.inventory:
            if computer.description == description:
                computer.operating_system = new_os
                print(f"Refurbished {computer.description}, new OS: {computer.operating_system}")
                return
        print(f"Error: No computer found with description '{description}'")

    def print_inventory(self):
        for computer in self.inventory:
            print(f"{computer.description}: {computer.operating_system}")

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
    computer_id = shop.buy(computer1)  # ✅ 现在 `computer_id` 仍然是 description

    # Print inventory
    shop.print_inventory()

    # Refurbish the computer
    print("\nRefurbishing computer1...")
    shop.refurbish(computer_id, "MacOS Monterey")  # ✅ 仍然传 description

    # Print inventory after refurbishing
    shop.print_inventory()

    # Sell the computer
    print("\nSelling computer1...")
    shop.sell(computer_id)

    # Print inventory after selling
    shop.print_inventory()

if __name__ == "__main__":
    main()
