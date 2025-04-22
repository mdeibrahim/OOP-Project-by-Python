from admin import Admin
from customer import Customer
from restautant import Restaurant

print("---Welcome to the Restaurant Management System---\n")
while True:
    print("----- Admin Menu -----")
    print("1. Admin Login\n2. Customer Login\n3. Exit")
    option = int(input("Select an option: "))
    if option == 1:
        admin=input("Enter Admin name: ")
        a1=Admin(admin)
        print(f"\n-----Welcime Admin {admin}-----")
        while True:
            print("\n-----Admin Menu-----")
            print("1. Create Customer Account\n2. Remove Customer Account\n3. Viwe All Customers\n4. Manage Restaurent Menu\n5 Logout")
            option = int(input("Select an option: "))
            if option == 1:
                a1.add_customer()
            elif option == 2:
                a1.remove_customer()
            elif option == 3:
                a1.view_customers()
            elif option == 4:
                while True:
                    print(f"\n----- Manage Restaurent Menu ----- ")
                    print("1. Add Item in Menu\n2. Remove Item to Menu\n3. Update Menu Item\n4. View Menu\n5. Exit")
                    option = int(input("Select an option: "))
                    if option == 1:
                        a1.add_item_to_menu()
                    elif option == 2:
                        a1.remove_item_from_menu()
                    elif option == 3:
                        a1.update_item_in_menu()
                    elif option == 4:
                        a1.view_menu()
                    elif option == 5:
                        print("-----Exit Successfull----\n")
                        break
                    else:
                        print("\n** Invalid Input! Please try again.")
            elif option == 5:
                print("----Logout Successfull----\n")
                break
            else:
                print("\n** Invalid Input! Please try again.")
    elif option == 2:
        find,username=a1.log_in()
        if find:
            print(f"\n----Welcome {username}----")
            while True:
                print(f"\n---- {username}'s Menu ----")
                print("1. View Restaurent Menu\n2. View Balance\n3. TopUp Balance\n4. Place Order\n5. View Past order\n6. Logout")
                option = int (input("Select an option: "))
                if option == 1:
                    Restaurant.replica(Restaurant)
                elif option == 2:
                    Customer.view_balance(Customer)
                elif option == 3:
                    Customer.add_balance_to_walet(Customer)
                elif option == 4:
                    Customer.add_cart(Customer)
                elif option == 5:
                    Customer.view_cart(Customer)
                elif option == 6:
                    break
                else:
                    print("\n** Invalid Input! Please try again.")
        else:
            print("\n   !! Incorrect Username or Password. Please try again.\n")
    else:
        break
    
