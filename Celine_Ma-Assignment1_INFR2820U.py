# # Celine Ma # 100874382
# # INFR 2820U Assignment 1 


import time

# Defining class Product
class Product:
    def __init__(self, ID, Name, Price, Category): # Constructor to initialize attributes
        # Initialize attributes
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category

# # Defining get_product_data function: Load products from file into array
def get_product_data(filename):
    products = [] # Set as an array 
    file = open(filename, "r")  # Open product_data.txt and read the file
    for line in file:  # Iterate over each line in the file
        data = line.strip().split(',') # Split the line into components
        # Load and store given product data (product_data.txt) into arrays
        new_product = Product(int(data[0]), data[1], float(data[2]), data[3])
        products.append(new_product) 
    return products

# # Defining insert_product function: Insert product
def insert_product(products, new_product):
    products.append(new_product)
    return products

# # Defining update_product function: Update product
def update_product(products, update_product_id, new_data):
    for product in products: # Iterate over each product in products
        if product.ID == update_product_id: # Check if the product ID matches the specified ID
            product.Name = new_data[0] # Update the Name attribute of the product
            product.Price = new_data[1] # Update the Price attribute of the product
            product.Category = new_data[2] # Update the Category attribute of the product
            break

# Defining delete_product function: Delete product
def delete_product(products, product_id):
    updated_products = [] # Create new array
    for product in products:
        if product.ID != product_id:
            updated_products.append(product) # Add to array if not equal to deletion
    products[:] = updated_products # Update old product array

 # Defining search_product function: Search product
def search_product(products, key, value):
    result = []
    for product in products:
        if getattr(product, key) == value: # If the value is equal append to result
            result.append(product)
    return result

# Defining bubble_sort function: Bubble sorting by price
def bubble_sort_by_price(products):
    start_time = time.time() # Start the time for bubble sort
    n = len(products) # Get the length of the array
    for i in range(n - 1):  # Iterate over the array
        swapped = False  # The array is not sorted
        for j in range(0, n - i - 1): # Iterate over the array from 0 to n-i-1
            if products[j].Price > products[j + 1].Price:
                # Swap if the element is greater than the next element
                products[j], products[j + 1] = products[j + 1], products[j]
                swapped = True  # Set swapped to True
        if not swapped:  # The array is sorted
                break
    end_time = time.time() # End the time for bubble sort
    time_difference = end_time - start_time # Bubble sort time
    print(f"Bubble Sort Time: {time_difference} seconds")
    print("Bubble Sorting by Price:")
    for b in products:
        print(f"ID: {b.ID}, Name: {b.Name}, Price: {b.Price}, Category: {b.Category}")

# Defining insertion_sort function
def insertion_sort_by_price(products):
    start_time = time.time() # Start the time for insertion sort
    n = len(products)  # Get the length of the array
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
    for i in range(1, n):  # Iterate over array starting from the second element
        key = products[i]  # Store current element to key to be inserted in the right position
        j = i - 1
        while j >= 0 and key.Price < products[j].Price:
            # Move elements greater one position ahead of the key
            products[j + 1] = products[j]  # Shift to the right
            j -= 1
        products[j + 1] = key  # Insert the key in the correct position
    end_time = time.time() # End the time for insertion sort
    time_difference = end_time - start_time # Insertion sort time
    print(f"\nInsertion Sort Time: {time_difference} seconds")
    print("Insertion by Price:")
    for b in products:
        print(f"ID: {b.ID}, Name: {b.Name}, Price: {b.Price}, Category: {b.Category}")


# It executes the code found in the script
if __name__ == "__main__":

    # 1 | Load product Data
    products = get_product_data("product_data.txt") # Load file
    for a in products:
        print(f"ID: {a.ID}, Name: {a.Name}, Price: {a.Price}, Category: {a.Category}")

    # 2 | Operations
    new_product = Product(111, 'Sun glasses', 99.99, 'Vision') # Set product
    insert_product(products, new_product) # Add product
    for a in products:
        print(f"ID: {a.ID}, Name: {a.Name}, Price: {a.Price}, Category: {a.Category}")

    update_product(products, 34863, ('Updated Product', 75.0, 'Updated Category')) # Update product: 34863, Biography XPESK, 287.31, Books
    for a in products:
        print(f"ID: {a.ID}, Name: {a.Name}, Price: {a.Price}, Category: {a.Category}")    
    
    delete_product(products, 18086) # Delete product (line 4 from file): 18086, Shirt ZQLTI, 439.07, Clothing
    for a in products:
        print(f"ID: {a.ID}, Name: {a.Name}, Price: {a.Price}, Category: {a.Category}") 

    # Search function
    results = search_product(products, 'Name', ' Smartphone ILGCU') # To search Name you need to put a space ahead
    print("Search Result:")
    for a in results:
        print(f"ID: {a.ID}, Name: {a.Name}, Price: {a.Price}, Category: {a.Category}")

    # 3 and 4 | Sort by Price and Time
    bubble_sort_by_price(products) # Run bubble sort
    insertion_sort_by_price(products) # Run insertion sort


    

