class Coffee: #initialize coffee with a name and the price. classes use this case "class Coffee" pascal? or camel?
    def __init__(self, name, price): #is __init__ a dunder method? I need to study up on dunder methods
        self.name = name
        self.price = price

class Order:
    def __init__(self): #The order class needs to have an empty list
        self.items = []

    def add_item(self, coffee): #here we add the coffee to the order
        self.items.append(coffee)
        print(f"{coffee.name} was added to your order.") #f string to tie it together

    def total(self):
        return sum(item.price for item in self.items) #this should calculate the total

    def show_order(self):
        if not self.items:
            print("No items in order.")
            return
        print("\nYour Order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - KES{item.price}")
        print(f"Total: KES{self.total()}\n")

    def checkout(self): #initiate the checkout process 
        if not self.items:
            print("Your cart is empty.")
            return 
        self.show_order()
        confirm = input("proceed to checkout?(yes/no): ").strip().lower()
        if confirm == "yes":
            print("Order confirmed. Have a great day!") 
            self.items.clear()

        else:
            print("Your order was cancelled.")

def main(): #we're creating the menu and user input. 
        menu= [
            Coffee("1. Espresso", 250),
            Coffee("2. Latte", 350),
            Coffee("3. Capuccino", 300),
            Coffee("4. Americano", 200),
        ] 
        order = Order()

        while True:
            print("\n-----Coffee Menu-----")
            for i, coffee in enumerate(menu, 1):
                print(f"{i}. {coffee.name} - {coffee.price}")
                print("5. View Order")
                print("6. Checkout")
                print("7. Exit")

                choice = input("choose an option:" )
                if choice in ["1","2","3","4"]:
                    order.add_item(menu[int(choice) - 1])

                elif choice == "5":
                    order.show_order()
                elif choice == "6":
                    order.checkout()
                elif choice == "7":
                    print("Thanks for checking us out. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()