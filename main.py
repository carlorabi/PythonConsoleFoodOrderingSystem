from menu import Menu, display_menu
from menu_item import MenuItem
from customer import Customer
from order import Order
from banner import print_banner, print_exit_banner
from receipt import print_receipt
import os



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def place_order(menu, customer):
    order = Order()

    print(f"Welcome {customer.name} to Order it!")
    display_menu(menu)

    while True:
        choice = input("Enter the name of the item you want to order (or 'q' to quit): ")

        if choice == 'q':
            break

        item = menu.find_item(choice)
        if item:
            quantity = int(input("Enter the quantity: "))
            order.add_item(item, quantity)
            print(f"{item.name}: ₱{item.price:.2f} x {quantity} added to your order.")
        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            add_another = input("Do you want to add another item? (y/n): ")
            if add_another.lower() == 'n':
                break
            elif add_another.lower() != 'y':
                print("Invalid input. Please enter 'y' or 'n'.")
            else:
                break

    print("Your order:")
    for index, order_item in enumerate(order.items):
        print(f"{index+1}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} | Quantity: {order_item.quantity}")

    total_cost = order.calculate_total_cost()
    print(f"Total cost: ₱{total_cost:.2f}")

    while True:
        print("\nDo you want to make any changes to your order?")
        print_menu_button("1. Change Item")
        print_menu_button("2. Change Quantity")
        print_menu_button("3. Delete Item") 
        print_menu_button("4. Continue")

        action = input("\nEnter your choice: ")
        if action == '1':
            cls()
            print("Current order:")
            for index, item in enumerate(order.items, start=1):
                print(f"{index}. {item.menu_item.name}: ₱{item.menu_item.price:.2f} x Quantity {item.quantity}")
            item_name = input("\nEnter the name of the item you want to change: ")
            found_item = False
            for order_item in order.items:
                if order_item.menu_item.name.lower() == item_name.lower():
                    display_menu(menu)
                    new_item_name = input("\nEnter the new item name: ")
                    new_item_quantity = int(input("Enter the quantity: "))
                    new_item = menu.find_item(new_item_name)
                    if new_item:
                        order_item.menu_item = new_item
                        order_item.quantity = new_item_quantity
                        print("Item updated successfully.")
                        print("\nUpdated order:") # Print the updated order
                        for index, order_item in enumerate(order.items, start=1):
                            print(f"{index}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} x Quantity {order_item.quantity}")

                    else:
                        print("Invalid item name. Item not updated.")
                    found_item = True
                    break
            if not found_item:
                print("Item not found in the order.")

        elif action == '2':
            cls()
            print("Current order:")
            for index, item in enumerate(order.items, start=1):
                print(f"{index}. {item.menu_item.name}: ₱{item.menu_item.price:.2f} x Quantity {item.quantity}")
            item_name = input("Enter the name of the item you want to change quantity: ")
            found_item = False
            for order_item in order.items:
                if order_item.menu_item.name.lower() == item_name.lower():
                    new_quantity = int(input("\nEnter the new quantity: "))
                    if new_quantity > 0:
                        order_item.quantity = new_quantity
                        print("Quantity updated successfully.")
                        print("\nUpdated order:") # Print the updated order
                        for index, order_item in enumerate(order.items, start=1):
                            print(f"{index}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} x Quantity {order_item.quantity}")

                    else:
                        print("Invalid quantity. Quantity not updated.")
                    found_item = True
                    break

            if not found_item:
                print("Item not found in the order.")
            

        elif action == '3':
            cls()
            print("Current order:")
            for index, item in enumerate(order.items, start=1):
                print(f"{index}. {item.menu_item.name}: ₱{item.menu_item.price:.2f} x Quantity {item.quantity}")
            item_name = input("Enter the name of the item you want to delete: ")
            found_item = False
            for order_item in order.items:
                if order_item.menu_item.name.lower() == item_name.lower():
                    order.items.remove(order_item)
                    print(f"{order_item} deleted from the order.")
                    print("\nUpdated order:") # Print the updated order
                    for index, order_item in enumerate(order.items, start=1):
                        print(f"{index}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} x Quantity {order_item.quantity}")
                    found_item = True
                    break
            if not found_item:
                print("Item not found in the order.")

            # Check if the order items list is empty
            if not order.items:
                print("No order found.")

        elif action == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        customer.add_order(order)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac



# Main program
menu = Menu()

item1 = MenuItem("Burger", 25.00)
item2 = MenuItem("Pizza", 75.00)
item3 = MenuItem("Fries", 25.00)
item4 = MenuItem("Takoyaki", 40.00)
item5 = MenuItem("Ice Cream", 20.00)

menu.add_item(item1)
menu.add_item(item2)
menu.add_item(item3)
menu.add_item(item4)
menu.add_item(item5)

customers = []


def print_menu_button(label):
    print(f"  \u25A0 {label} ")


while True:
    clear_screen() #for cls
    print_banner()
    print()
    print_menu_button("1. Show Menu")
    print_menu_button("2. Add Item to Menu")
    print_menu_button("3. Remove Item from Menu")
    print_menu_button("4. Place Order")
    print_menu_button("5. Total Orders for Customer")
    print_menu_button("6. Exit")

    choice = input("\nEnter the number of your choice: ")


    #if chose 1
    if choice == '1':
        clear_screen()
        display_menu(menu)
        input("Press Enter to continue...")


    #if chose 2
    elif choice == '2':
        while True:
            clear_screen()
            item_name = input("Enter the name of the item: ")
            while True:
                try:
                    item_price = float(input("Enter the price of the item: ₱"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            new_item = MenuItem(item_name, item_price)
            menu.add_item(new_item)
            print(f"{item_name} added to the menu.")
            while True:
                add_another = input("Do you want to add another item? (y/n): ")
                if add_another.lower() == 'n':
                    break
                elif add_another.lower() == 'y':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            if add_another.lower() == 'n':
                break
            elif add_another.lower() != 'y':
                continue


    #if chose 3
    elif choice == '3':
        clear_screen()
        display_menu(menu)
        item_name = input("Enter the name of the item you want to remove: ")
        if menu.remove_item(item_name):
            print(f"{item_name} removed from the menu.")
        else:
            print("Item not found in the menu.")
        input("Press Enter to continue...")

    #if chose 4
    elif choice == '4': 
        clear_screen()
        customer_name = input("Enter your name: ")
        customer = None
        for c in customers:
            if c.name.lower() == customer_name.lower():
                customer = c
                break
        if not customer:
            customer = Customer(customer_name)
            customers.append(customer)
        place_order(menu, customer)
        input("Press Enter to continue...")


    #if chose 5
    elif choice == '5':
        if not customers:
            print("\nNo customer(s) yet.")  #shows when no customer added
            input("Press Enter to continue...")
            continue

        print("Customers:")
        for customer in customers:
            print(customer.name)

        customer_name = input("\nEnter the name of the customer: ")
        for customer in customers:
            if customer.name.lower() == customer_name.lower():
                total_spent = customer.calculate_total_spent()
                print(f"Total spent by {customer.name}: ₱{total_spent:.2f}")
                has_orders = False
                for order in customer.orders:
                    print("\nOrder(s):")
                    for index, order_item in enumerate(order.items, start=1):
                        print(f"{index}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} x Quantity {order_item.quantity}")
                if not has_orders:
                    print(f"No orders found for {customer.name}.")
                    input("Press Enter to continue...")
                    break  # Exit the loop if no orders found.
                while True:
                    bill_amount = input("Enter the bill amount: ₱")
                    try:
                        bill_amount = float(bill_amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                remaining_balance = bill_amount - total_spent
                print(f"Change for {customer.name}: ₱{remaining_balance:.2f}")
                customers.remove(customer) # Remove the customer from the list
                print_receipt(customer, bill_amount, remaining_balance)
                input("Press Enter to continue...")
                break

        else:
            print("Customer not found.")
            input("Press Enter to continue...")


    #if chose 6
    elif choice == '6':
        print_exit_banner()

        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
