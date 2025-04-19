import restautant

class Customer:
    all_customers = []
    # all_customers_login = []
    cart=[]
    walet_balance = float(0)
    total=float(0)
    previous_total=float(0)

    def __init__(self, name,email, address,username,password):
        self.name = name
        self.email = email
        self.address = address
        self.username =username
        self.password =password

    def log_in(self):
        username=input("\nEnter Customer Username: ")
        password=input("Enter Customer Password: ")
        for user in Customer.all_customers:
            if user.username == username and user.password == password:
                return True,username
        return False
    
    def add_customer(self):
        name=input("Enter customer name: ")
        email = input("Enter customer email: ")
        address = input("Enter customer address: ")
        username = input("Enter customer usernsme:")
        password = input("Enter customer password: ")
        
        for e_mail in Customer.all_customers:
            if e_mail.email == email:
                print("\n**Customer already exists!!")
                return

        usernames = [u.username for u in Customer.all_customers]      
        while username in usernames:
            print("\n**Username mached with another customer!! Please try another!")
            username = input("New username:")    

        # Customer.all_customers_login.append((username,password))
        c1= Customer(name, email,address,username,password)
        Customer.all_customers.append(c1)

    def view_customers(self):
        if Customer.all_customers == []:
            print("\nHave no registered customers yet.")
        else:
            print("\n-----Registered Customers-----")
            for customer in Customer.all_customers:
                print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}, Username: {customer.username}, Password: {customer.password}")

    def remove_customer(self):
        if Customer.all_customers == []:
            print("\nHave no registered customers to remove.")
            return

        
        while True:
            print("\n****Remove Customer****")
            print("1. By Username\n2. By Email\n3. Cancel")
            choice=int(input("Enter your choice: "))
            if choice == 1:
                username = input("Enter customer username to remove: ")
                found=False
                for custo_mer in Customer.all_customers:
                    if custo_mer.username == username:
                        found = True
                        Customer.all_customers.remove(custo_mer)
                        break
                # for custo_mer in Customer.all_customers_login:
                #     if custo_mer[0] == username:
                #         Customer.all_customers_login.remove(custo_mer)
                #         break
                if found:
                    print("\nCustomer removed successfully.")
                    break

            elif choice==2:
                email = input("Enter customer email to remove: ")
                user_name=""
                found = False
                for custo_mer in Customer.all_customers:
                    if custo_mer.email == email:
                        user_name = custo_mer.username
                        found = True
                        Customer.all_customers.remove(custo_mer)
                        break
                # for custo_mer in Customer.all_customers_login:
                #     if custo_mer[0] == user_name:
                #         Customer.all_customers_login.remove(custo_mer)
                #         break
                if found:
                    print("\nCustomer removed successfully.")
                    break

            elif choice == 3:
                return
            else:
                print("\n*Invalid choice!")
                print("Please try again!")

    def add_balance_to_walet(self):
        print("\n---Add balance in walet---")
        print("From 1. Bkash \t2. Nagad\t3. Rocket")
        option=int(input("Enter an option: "))
        if option == 1 or option == 2:
            while True:
                if option == 1:
                    phone=int(input("Enter Bkash phone Number: +880"))
                else:
                    phone=int(input("Enter Nagad phone Number: +880"))
                if phone<1299999999 or phone>2000000000:
                    print("\n ---Invalid Number! Please enter right number.")
                else:
                    while True:
                        amount=int(input("Enter amount to add Balance: "))
                        if amount<=0:
                            print("\n----Amount must be greater then 0. Please try again----\n ")
                        else:
                            self.walet_balance+=amount
                            print(f"\n----${amount} Successfully added in Balance.----")
                            if self.total>0:
                                if self.total>amount:
                                    self.walet_balance=0
                                    self.total-=amount
                                    self.previous_total+=amount
                                    print(f"\n-- ${amount} has been creadited from your Balance because of due. Your current due is ${self.total}")
                                else:
                                    print(f"\n-- ${self.total} has been creadited from your Balance. ")
                                    self.walet_balance-=self.total
                                    self.previous_total+=self.total
                                    self.total=0
                                    break
                            break
                    break
        elif option == 3:
            while True:
                phone=int(input("Enter Rocket phone Number: +880"))
                if phone<12999999999 or phone>20000000000:
                    print("\n ---Invalid Number! Rocket Number must be 12 digit including first 0.\n")
                else:
                    while True:
                        amount=int(input("Enter amount to add Balance: "))
                        if amount<=0:
                            print("\n----Amount must be greater then 0. Please try again---- \n")
                        else:
                            self.walet_balance+=amount
                            print(f"\n----${amount} Successfully added in Balance ----\n")
                            if self.total>0:
                                if self.total>amount:
                                    self.walet_balance=0
                                    self.total-=amount
                                    self.previous_total+=amount
                                    print(f"\n-- ${amount} has been creadited from your Balance because of due. Your current due is ${self.total}")
                                else:
                                    print(f"-- ${self.total} has been creadited from your Balance. ")
                                    self.walet_balance-=self.total
                                    self.previous_total+=self.total
                                    self.total=0
                                    break
                            break
                    break
        return

    def view_balance(self):
        print(f"\n-----Current Balance  ${self.walet_balance}.-----")

    def add_cart(self):
        restautant.Restaurant.replica(restautant)
        find = len(restautant.Restaurant.menu)
        if find:
            print("Enter Item Name and Quantity togather separated by one space.")
            name,quantity=input().split()
            quantity=int(quantity)
            found=False
            for item in restautant.Restaurant.menu:
                if item.name==name:
                    found=True
                    if item.quantity>=quantity:
                        sub_total=quantity*item.price
                        self.total+=sub_total
                        self.cart.append((name,quantity,sub_total))
                        item.quantity-=quantity
                        print(f"\nOrder placed -_- Your sub_total ${self.total}")
                        break
                    else:
                        print(f"\n--Sorry {name} has only {item.quantity} units")
                        break
            if not found:
                print(f"\n--Sorry {name} is not found in Menu.")
            while True:
                name,quantity=input("Anything else or enter ""NO 0"": ").split()
                quantity=int(quantity)
                if name.upper()=="NO":
                    if self.walet_balance<self.total:
                        print(f"\n-- !!Walet has insufficient Balance. You have due ${self.total}. Please TopUp as soon as possible. ")
                        break
                    else:
                        print(f"\n-- ${self.total} has been creadited from your Balance. ")
                        self.previous_total+=self.total
                        self.total=0
                        break
                found=False
                for item in restautant.Restaurant.menu:
                    if item.name==name:
                        found=True
                        if item.quantity>=quantity:
                            sub_total=quantity*item.price
                            self.cart.append((name,quantity,sub_total))
                            self.total+=sub_total
                            item.quantity-=quantity
                            print(f"\nOrder placed -_- Your sub_total ${self.total}")
                            break
                        else:
                            print(f"\n--Sorry {name} has only {item.quantity} units")
                            break
                if not found:
                    print(f"\n--Sorry {name} is not found in Menu.")
        else:
            return

    def view_cart(self):
        print("\n---Your Past Orders---")
        if self.cart==[]:
            print("**History not found!")
            return
        print("-Item   Quantity   Sub_Total")
        for i, item in enumerate(self.cart, start=1):
            print(f"{i}. {item[0]}\t{item[1]}\t  {item[2]}")
        print("----------------------------------")
        print(f" Total Paid Amount = {self.previous_total}")
        print(f" Total Due Amount = {self.total}")