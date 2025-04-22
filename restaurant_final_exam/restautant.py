

class Restaurant:
    menu = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_item_to_menu(self):
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        item = Restaurant(item_name,item_price, item_quantity)
        Restaurant.menu.append(item)
        print(f"\nSuccessfully Add Item in Menu: Name: {item_name} price: {item_price} quantity: {item_quantity}\n")

    def remove_item_from_menu(self):
        item_name = input("Enter item name to remove:")
        found = False
        for item in Restaurant.menu:
            if item.name == item_name:
                Restaurant.menu.remove(item)
                found = True
                break
        if found:
            print(f"Item {item_name} removed from menu successfully.")
        else:
            print(f"*Item {item_name} not found in menu.")
        
    def update_item_in_menu(self):
        item_name = input("Enter item name to update:")
        found = False
        for item in Restaurant.menu:
            if item.name == item_name:
                found = True
                print("\n----*Item found----")
                while True:
                    print("1. Update name\n2. Update price\n3. Update quantity\n4. Cancel")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        new_name = input("Enter new name: ")
                        item.name = new_name
                        print(f"***Item name updated to {new_name} succcessfuly.")
                    elif choice ==2:
                        new_price = input("Enter new price: ")
                        item.price = new_price
                        print(f"\n***Item price updated to ${new_price} succcessfuly.\n")
                    elif choice == 3:
                        new_quantity = int(input("Enter new quantity: "))
                        item.quantity += new_quantity
                        print(f"\n***Item quantity increased {new_quantity} units succcessfuly.")
                    elif choice == 4:
                        print("\n")
                        return
                    else:
                        print("\n-----Invalid option! Please enter right option-----")
                break
        if not found:
            print("\n** Item Not found! Please enter right name.\n")
    
    
    def view_menu(self):
        if Restaurant.menu == []:
            print("\n***Menu is empty!\n")
        else:
            print("\n-----Menu-----")
            for item in Restaurant.menu:
                print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")
            print("\n")
    
    def replica(self):
        print("\n  --------Restaurent Menu-------")
        print("  Item_Name\tPrice\t   Ststus")
        if len(Restaurant.menu)==0:
            print("\n--Sorry Have No Item to Place Order-- \n")
        for i, item in enumerate(Restaurant.menu, start=1):
            status="Not Available" if item.quantity==0 else "Available"
            print(f"  {i}. {item.name}        ${item.price}\t{status}")
            
        print("------------------------------------\n")

    