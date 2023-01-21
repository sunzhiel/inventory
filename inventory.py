# This program is an inventory system for a fictional Nike warehouse.
# It reads product information from a text file, provides the facility
# to manipulate the data in a variety of ways and can also write
# information back to the textfile.

# Import required module.
from tabulate import tabulate

#========The beginning of the class==========
# Initialize Shoe class with the parameters country, code, product, cost, quantity.
# Define the necessary functions.

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        return self.country
    
    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return (f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n").upper()
    
    def set_quantity(self, restock_qty):
        self.quantity = restock_qty


#=============Shoe list===========
# Create empty lists for shoe list and object list.
shoe_list = []
shoe_object = []

# Define functions outside of class to perform various operations.
# Use exception blocks throughout to defend against errors.
# Fetch data for each product (as necessary) using get_() class methods.

# Define function to read each line from the text file.
# Append items to shoe list.
# Create objects from each item and append to object list.
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as check_inventory:
            for line in check_inventory:
                strip_line = line.strip("\n")
                split_line = strip_line.split(",")
                shoe_list.append(split_line)

            for i in range(1, len(shoe_list)):
                array = shoe_list[i]
                shoe =  Shoe(array[0], array[1], array[2], array[3], int(array[4]))
                shoe_object.append(shoe)

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

# Define function to get input from user for new products.
# Create objects from each item and append to object list.
def capture_shoes():
    try:
        item_country = input("Please enter the origin country of the new item:\n")
        item_code = input("Please enter the item code:\n")
        item_name = input("Please enter the item name:\n")
        item_cost = int(input("Please enter the unit cost of the item, in numbers only. E.g. 123\n"))
        item_quantity = int(input("Please enter the batch quantity of the item, in numbers only. E.g. 40\n"))

        new_item = Shoe(item_country,item_code, item_name, item_cost, item_quantity)
        shoe_object.append(new_item)

        with open("inventory.txt", "a+") as change_inventory:
            change_inventory.write(f'\n{item_country},{item_code},{item_name},{item_cost},{item_quantity}')
            print("\nThank you, new item added to inventory!\n")

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

# Define function for displaying all items in stock.
# Display using tabulate.
def view_all():
    try:

        print("\n---------------------------------------------INVENTORY------------------------------------------\n")

        country = []
        code = []
        product = []
        cost = []
        quantity = []
        table  = []

        for lines in shoe_object:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt = 'fancy_grid'))

        print("\n---------------------------------------------END-------------------------------------------------\n")

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

# Define function to display the 5 items with the lowest quantity, using sort().
# Display using tabulate.
# Get user input for new stock quantity and write to text file.
def re_stock():
    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
        shoe_object.sort(key=lambda x:x.quantity)

        for i in range(1,6):
            restock_list.append(shoe_object[i])
    
        print("\n----------------------------Lowest stock items:----------------------------\n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt ='fancy_grid', showindex = range(1,6)))
        
        print("\n---------------------------------------------------------------------------\n")

        restock_item = int(input("\nPlease enter the index of the product you want to restock:\n"))
        restock_qty = int(input("\nPlease enter the new quantity:\n"))
        shoe_object[restock_item].set_quantity(restock_qty)

        output = ''
        for item in shoe_object:
            output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

        with open("inventory.txt", "w") as restock:
            restock.write(output)
        
        print("\nInventory has been updated!")

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

# Define function to search for specific items & display associated information.
def search_shoe():
    try:
        find_shoe = input("\nPlease enter the code you are searching for:\n\n")

        for line in shoe_object:
            if line.get_code() == find_shoe:
                print(f'\n {line}')

        print("\nPlease select another option from the menu below\n")

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

# Define function to display total stock value per product line.
def value_per_item():
    try:
        for line in shoe_object:
            value = int(line.get_cost()) * int(line.get_quantity())
            print(f'{line.get_code()} Total stock value: R{value}\n')

        print("\nPlease select another option from the menu below\n")

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

# Define function to display the item with the highest quantity.
# Create an empty list for quantity values & append values to list.
# Display using max() & mark item for sale.
def highest_qty():
    try:
        highest_qty = []

        for line in shoe_object:
            highest_qty.append(line)

        print("\n----------------------------Highest quantity item:----------------------------\n")

        print(max(shoe_object, key=lambda item: item.quantity))
        print("\nThis item has now been marked for sale\n")
        print("\nPlease select an option from the menu below")

    except FileNotFoundError as error:
        print("\nSorry, that file does not exist!\n")
        print(error)

#==========Main Menu=============
# Wrap code in while loop 
# Display menu options & prompt for user input.
# Use an exception block to defend against errors.
read_shoes_data()
while True:

    try:
        menu = int(input('''\n
               ----- Nike Inventory System ----- 
            Please enter a number from the menu below:
            1. Add item to inventory
            2. View all products
            3. Restock item
            4. Product search
            5. View item values
            6. View sale items
            7. Exit
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            re_stock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_qty()
        
        elif menu == 7:
            exit()
        
        else:
            print("\nYou have selected an invalid option. Please try again. Choose from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again. Enter a number.\n")