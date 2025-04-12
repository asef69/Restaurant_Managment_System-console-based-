from abc import ABC
from orders import Order
class User:
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart=Order()
    def view_menu(self,resturant):
        resturant.menu.show_menu()
    def add_to_cart(self,resturant,item_name,quantity):
        item=resturant.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("Limit Exceeded")
            else:
                item.quantity=quantity
                self.cart.add_item(item)    
            
        else:
            print("Item not found")
    def view_cart(self):
        print("****View Cart****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Cost={self.cart.total_price()}")
    def pay_bill(self):
        print(f"Total Bill: {self.cart.total_price()} is paid successfully")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, email, phone, address,age,salary,designation):
        super().__init__(name, email, phone, address)        
        self.age=age
        self.salary=salary
        self.designation=designation
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        
    def add_employee(self,resturant,employee):
        resturant.add_employee(employee)
    def view_employee(self,resturant):
        resturant.view_employee()
    def add_new(self,resturant,item):
        resturant.menu.add_items(item)
    def remove_new(self,resturant,item):
        resturant.menu.remove_item(item)
    def view_menu(self,resturant):
        resturant.menu.show_menu()






        



        
                        
        