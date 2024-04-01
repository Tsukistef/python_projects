'''Practical Task 2 - Handling Strings, Lists and Dictionaries'''
# Create a list called 'menu' with 4 items and a dictionary called 'stock' containing the values for each item on menu.
menu = ["Chocolate cake", "Victorian Sponge", "Tiramisu", "Cannoli"]
stock = {
    "Chocolate cake" : 41,
    "Victorian Sponge" : 35,
    "Tiramisu" : 12,
    "Cannoli" : 33
}

# Create another dictionary called 'price', which should contain the prices for each item on the menu.
price = {
    "Chocolate cake" : 6.50,
    "Victorian Sponge" : 5,
    "Tiramisu" : 7,
    "Cannoli" : 3
}

# Calculate in total_stock the total of items worth in the cafe. Loop through appropiate dictionaries and lists to do this.
total_stock = 0
for item in menu: # Loops through menu items and uses the string name to get each key value.
    multiplier = float(stock[item] * price[item])
    total_stock += multiplier
print("total stock value: £" + str(total_stock))