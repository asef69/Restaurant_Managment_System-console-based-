from menu import Menu
from fooditem import FoodItem
from orders import Order
from resturant import Resturant
from users import Admin,Employee,Customer

restaurant=Resturant("Mayer Dua Restaurant")
def customer_menu():
    name=input("Enter your name:")
    phone=input("Enter your phone number:")
    address=input("Enter your address:")
    email=input("Enter your Email:")
    customer=Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f"Welcome {customer.name} to the restaurant")
        print("1.View Menu")
        print("2.Add to Cart")
        print("3.View Cart")
        print("4.Pay Bill")
        print("5.Exit")

        choice=int(input("Give your choice please:"))

        if choice==1:
            customer.view_menu(restaurant)
        elif choice==2:
            item_name=input("Enter your item:")
            item_quantity=int(input("Enter your item quantity:"))
            customer.add_to_cart(restaurant,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            print("Thank you for coming")
            break
        else:
            print("Invalid Choice")            


def admin_menu():
    name=input("Enter your name:")
    phone=input("Enter your phone number:")
    address=input("Enter your address")
    email=input("Enter your Email:")
    admin=Admin(name=name,phone=phone,email=email,address=address)

    while True:
        print(f"Welcome {admin.name} to the restaurant")
        print("1.Add new item")
        print("2.Add new employee")
        print("3.View Employee")
        print("4.View item")
        print("5.Delete item")
        print("6.Exit")

        choice=int(input("Give your choice please:"))

        if choice==1:
            item=input("Enter your item name:")
            price=int(input("Enter the price:"))
            quantity=int(input("Enter the quantity:"))
            newItem=FoodItem(item,price,quantity)
            admin.add_new(restaurant,newItem)
        elif choice==2:
            name=input("Enter employee name:")
            phone=input("Enter phone number:")
            email=input("Enter email:")
            address=input("Enter address")
            age=input("Enter age:")
            salary=input("Enter salary:")
            designation=input("Enter designation:")
            employee=Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(restaurant,employee)
        elif choice==3:
            admin.view_employee(restaurant)
        elif choice==4:
            admin.view_menu()
        elif choice==5:
            remove=input("Enter item to remove:")
            admin.remove_new(restaurant,remove)
        elif choice==6:
            break    
        else:
            print("Invalid Choice") 
while True:
    print("Welcome!!")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        print("Goodbye!!!")
    else:
        print("Invalid Input")            