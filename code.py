# this is a list of items available in the vending machine, each with name, price, code, and stock
items = [
    {"name": "Water", "price": 1.50, "code": "001", "stock": 20},
    {"name": "Pepsi", "price": 2.00, "code": "002", "stock": 13},
    {"name": "Coca Cola", "price": 2.00, "code": "003", "stock": 5},
    {"name": "7 Up", "price": 4.00, "code": "004", "stock": 3},
    {"name": "Sprite", "price": 2.00, "code": "005", "stock": 6},
    {"name": "Cobra", "price": 2.50, "code": "006", "stock": 7},
    {"name": "Lipton Ice Tea", "price": 3.00, "code": "007", "stock": 9},
    {"name": "Zoi Ice Tea", "price": 3.50, "code": "008", "stock": 15},
    {"name": "Gatorade", "price": 5.00, "code": "009", "stock": 4},
    {"name": "Lays Chips", "price": 3.00, "code": "010", "stock": 6},
    {"name": "Doritos", "price": 2.50, "code": "011", "stock": 5},
    {"name": "Cheetos", "price": 3.00, "code": "012", "stock": 4},
    {"name": "Snickers", "price": 5.00, "code": "013", "stock": 5},
    {"name": "Twix", "price": 3.05, "code": "014", "stock": 2},
    {"name": "Laban Milk", "price": 7.00, "code": "015", "stock": 9}
]

# function to display all available items with their codes, names, prices, and stock levels
def display_items():
    print("Available items:")
    for item in items:
        print("- " + item["code"] + ": " + item["name"] + " - SAR", item["price"], "(Stock:", item["stock"], ")")

# main function to run the vending machine logic
def vending_machine():
    # displays the items at the start
    display_items()
    
    # starts balance at 0, as money will be inserted per purchase
    balance = 0.0
    
    # main loop for the vending machine operation
    while True:
        # asks the user to enter the product code first
        selection = input("Enter product code (or 'exit' to quit): ")
        if selection == 'exit':
            # if user chooses to exit, return the change back to them
            print("Returning change: SAR", balance)
            break
        
        # this finds the selected item by matching the code
        selected_item = None
        for item in items:
            if item["code"] == selection:
                selected_item = item
                break
        
        # if the code is invalid, prompt again
        if selected_item is None:
            print("Item not available. Try again.")
            continue
        
        # checks if the item is in stock
        if selected_item["stock"] <= 0:
            print("Item out of stock. Try again.")
            continue
        
        # looks at the price of the selected item
        price = selected_item["price"]
        
        # loop to handle money insertion, allowing the user to add more if insufficient
        while balance < price:
            try:
                # asks for money input
                money_input = float(input("Insert money: SAR"))
                if money_input < 0:
                    print("Cannot be a negative number. Try again.")
                    continue
                # adds the input to the balance
                balance += money_input
                print("Current balance: SAR", balance)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # deducts the price from balance and reduce stock
        balance -= price
        selected_item["stock"] -= 1
        print("Dispensing " + selected_item["name"] + ". Remaining balance: SAR", balance)
        
        # asks if the user wants to buy more or get their change back
        while True:
            choice = input("Buy more (y) or get change back 👎? ")
            if choice == 'y':
                # continues to the next purchase, keeping the remaining balance
                break
            elif choice == 'n':
                # returns remaining balance and exit
                print("Returning change: SAR", balance)
                return
            else:
                print("Invalid choice. Enter 'y' or 'n'.")

# calls the main function to start the vending machine
vending_machine()