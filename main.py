#INVENTORY MANAGEMENT
#library where the products are stored and has determined 5 burned products
products = {
    #5 burnt products
    'ps4': {'price': 100, 'amount': 70},
    'ps5': {'price': 500, 'amount': 20},
    'xbox one': {'price': 300, 'amount': 20},
    'xbox series s': {'price': 400, 'amount': 20},
    'nintendo switch': {'price': 320, 'amount': 30},
}

#Function for the user to enter a product by searching the library that does not yet exist and using try except to avoid errors
def add_product():
    while True:
        try:
            print("///ADD PRODUCT///")
            name = input("Add the product name: ").lower()
            #we confirm if it exists
            if name in products:
                print("Error, the product already exists")
                continue
            price = int(input("add the product price: "))
            #we confirm that the data is valid
            if price < 0:
                print("Error,the product price must be greater than 0.00")
                continue
            amount = int(input("Add the product amount: "))
            if amount < 1:
                print("Error,the product amount must be greater than 0.00")
                continue
            #It is saved in the product library as a library with the key being the name of the product
            products[name] = {
                "price" : price,
                "amount" : amount
                }
            print("product added successfully")
            return False
        except ValueError:
            print("Error, enter a valid value")
            
#Function to search for a product by name where the product data is printed and using try except to avoid errors
def search_product():
    while True:
        try:
            print("///SEARCH PRODUCT///")
            name_search = str(input("add name to search for product: ")).lower()
            product = products.get(name_search)
            #we confirm if it exists
            if not product:
                print("Product does not exist")
                continue
            print(f"Name: {name_search}\n Price: ${product['price']}\n Amount: {product['amount']}")
            return False
        except ValueError:
            print("Error, enter a valid value")
            
#Function to update the product price by searching for it by name and using try except to avoid errors
def update_product():
    while True:
        try:
            print("///UPDATE PRODUCT///")
            name_search = str(input("add name to search for product: ")).lower()
            product = products.get(name_search)
            #we confirm if it exists
            if not product:
                print("product does not exist")
                continue
            print(f"Name: {name_search}\n Price: ${product['price']}\n Amount: {product['amount']}")
            price_change = int(input("add new price: "))
            #we confirm that the data is valid
            if price_change < 1 or price_change == product['price']:
                print("Enter a new or valid price")          
                continue
            product["price"] = price_change
            print("updated product price")   
            print(f"Name: {name_search}\n Price: ${product['price']}\n Amount: {product['amount']}")
            return False
        except ValueError:
            print(f"Error {ValueError}, enter a valid value")
            
#Function to delete product by name, if the product exists you must confirm if you want to delete it
def deleted_product():
    while True: 
        try: 
            print("///DELETED PRODUCT///")
            name_search = str(input("add name to search for product: ")).lower()
            product = products.get(name_search)
            #we confirm if it exists
            if not product:
                print("product does not exist")
                continue
            print("Product found")
            print(f"Name: {name_search}\nPrice: ${product['price']}\nAmount: {product['amount']}")
            confirmation = input("Do you want to delete the product? enter (y) as if and (n) as not:").lower()
            #we confirm that the data is valid
            if confirmation == "y":
                del products[name_search]
                print("product removed")
                return False
            elif confirmation == "n":
                print("cancel")
                continue 
            elif "y" != confirmation  != "n":
                print("please, enter a valid opcion")      
                continue
        except ValueError:
            print(f"Error, enter a valid value")
    
#Function that calculates the total value of the inventory and prints the total price with 2 decimal places to the user.
def total_inventary():
    print("///CALCULATE INVENTORY VALUE///")
    #With a lambda function we make the total of the products with the quantity
    total = sum(map(lambda product: product['price'] * product['amount'], products.values()))
    #we convert the total to float
    total_float = float(total) 
    print(f"The calculation of the total value of the inventory is:\n ${total_float:.2f}")    
    
#menu function so that the user has the function options and selects the one they want to execute
def menu():
    opcion = {
        "1": add_product,
        "2": search_product,
        "3": update_product,
        "4": deleted_product,
        "5": total_inventary,
        "6": exit
    }

    while True:
        print("-------------------------------")
        print("Inventory management")
        print("1. Add product")
        print("2. Search product")
        print("3. Update price product")
        print("4. Deleted product")
        print("5. calculate inventory value")
        print("6. Exit")
        print("-------------------------------")

        action = input("Choose an option: ").strip()
        if action in opcion:
            opcion[action]()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
#@quiro66