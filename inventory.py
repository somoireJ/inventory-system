import csv

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, quantity, price):
        item = InventoryItem(name, quantity, price)
        self.inventory.append(item)
        print("Item added to inventory.")

    def remove_item(self, name):
        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)
                print("Item removed from inventory.")
                return
        print("Item not found in inventory.")

    def update_item(self, name, quantity=None, price=None):
        for item in self.inventory:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                print("Item updated in inventory.")
                return
        print("Item not found in inventory.")

    def display_inventory(self):
        for item in self.inventory:
            print(f"{item.name}: {item.quantity} x ${item.price}")

    def load_inventory(self, filename):
        with open(filename, "r", encoding="windows-1252") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name, quantity, price = row
                item = InventoryItem(name, int(quantity), float(price))
                self.inventory.append(item)
        print("Inventory loaded from file.")

    def save_inventory(self, filename):
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            for item in self.inventory:
                writer.writerow([item.name, item.quantity, item.price])
        print("Inventory saved to file.")

def main():
    inventory_system = InventoryManagementSystem()
    inventory_system.load_inventory("inventory.csv")

    while True:
        print("Welcome to the inventory management system!")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Display inventory")
        print("5. Save inventory")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory_system.add_item(name, quantity, price)

        elif choice == "2":
            name = input("Enter item name: ")
            inventory_system.remove_item(name)

        elif choice == "3":
            name = input("Enter item name: ")
            quantity = input("Enter new quantity (leave blank to not update): ")
            price = input("Enter new price (leave blank to not update): ")
            if quantity:
                quantity = int(quantity)
            if price:
                price = float(price)
            inventory_system.update_item(name, quantity, price)

        elif choice == "4":
            inventory_system.display_inventory()

        elif choice == "5":
            inventory_system.save_inventory("inventory.csv")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
