import csv
from inventory import InventoryManagementSystem


class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


def test_inventory_system():
    # Create a new inventory system
    inventory_system = InventoryManagementSystem()

    # Test adding an item
    inventory_system.add_item("laptop", 10, 20000.00)
    assert len(inventory_system.inventory) == 1
    assert inventory_system.inventory[0].name == "laptop"
    assert inventory_system.inventory[0].quantity == 10
    assert inventory_system.inventory[0].price == 20000.00

    # Test removing an item
    inventory_system.remove_item("laptop")
    assert len(inventory_system.inventory) == 0

    # Test updating an item
    inventory_system.add_item("smartphone", 5, 10000.50)
    inventory_system.update_item("smartphone", quantity=10, price=10000.50)
    assert inventory_system.inventory[0].quantity == 10
    assert inventory_system.inventory[0].price == 10000.50

    # Test displaying the inventory
    inventory_system.display_inventory()

    # Test saving and loading the inventory
    inventory_system.save_inventory("test_inventory.csv")
    inventory_system.load_inventory("test_inventory.csv")
    assert len(inventory_system.inventory) == 1
    assert inventory_system.inventory[0].name == "smartphone"
    assert inventory_system.inventory[0].quantity == 10
    assert inventory_system.inventory[0].price == 10000.50

    # Test updating an item with no changes
    inventory_system.update_item("smartphone")
    assert inventory_system.inventory[0].quantity == 10
    assert inventory_system.inventory[0].price == 10000.50

    print("All tests pass.")


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
            while True:
                name = input("Enter item name (or 'done' to finish adding items): ")
                if name == "done":
                    break
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
    test_inventory_system()
    main()
