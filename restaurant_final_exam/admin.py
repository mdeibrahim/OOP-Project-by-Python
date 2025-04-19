from customer import Customer
from restautant import Restaurant

class Admin:
    def __init__(self, name):
        self.name = name

    def log_in(self):
        find,username =Customer.log_in(self)
        return find,username

    def add_customer(self):
        Customer.add_customer(self)

    def view_customers(self):
        Customer.view_customers(self)
    
    def remove_customer(self):
        Customer.remove_customer(self)
    
    def add_item_to_menu(self):
        Restaurant.add_item_to_menu(self)
    
    def remove_item_from_menu(self):
        Restaurant.remove_item_from_menu(self)

    def update_item_in_menu(self):
        Restaurant.update_item_in_menu(self)
    
    def view_menu(self):
        Restaurant.view_menu(self)








#=================================================================================================
# a1=Admin("Boss")
# a1.add_customer()
# a1.view_customers()
# a1.add_customer()
# print("\n")
# a1.view_customers()
# a1.remove_customer()
# print("\n")
# a1.view_customers()

