'''T06 - Practical Task 1'''
# Calculates user's total holiday cost (plane, hotel and car rental cost).
# Get input for each item price.
# Define each city's flight price.
# Create four functions: hotel_cost(), plane_cost(), car_rental() and holiday_cost(), with each corresponding input as paramenter.
# Calculate total price multiplied by days/nights in each relevant function.
# creat holiday_cost() function to calculate total cost, taking num_nights, city_flight and rental_days as arguments.
# Print out all the details about function in a readable way.
# Test different combinations.

cities_destinations = ["Palermo", "Florence", "Rome", "Naples",]    # List of cities

print("Welcome!\nPlease choose one of the recommended destinations: ")
for city in cities_destinations:    # Displays city options
    print(city)

while True:
    city_flight = str((input("Which city are you flying to? \n")))     # City selection
    if city_flight in cities_destinations:
        break
    else:
        print("City not available. Please select from the available destinations. Make sure initial of city is uppercase.")
    

num_nights = int(input(f"How many nights are you staying in {city_flight}? \n"))    # Total stay
rental_days = int(input("How many days are you renting the car for? \n"))       # Total car rental days
    
def hotel_cost(num_nights):    # This function calculates total cost of hotel.
    price_hotel = 35
    bill_hotel = price_hotel * num_nights
    return bill_hotel

def plane_cost(city_flight):    # This function returns cost of flight depending on user answer.
    if city_flight == "Palermo":
        flight_cost = 50
    elif city_flight == "Florence":
        flight_cost = 140
    elif city_flight == "Rome":
        flight_cost = 150
    elif city_flight == "Naples":
        flight_cost = 80
    return flight_cost
    
def car_rental(rental_days):    # This function returns total cost of the car rental. 
    rental_cost = 50
    bill_car = rental_cost * rental_days
    return bill_car

def holiday_cost(num_nights, city_flight, rental_days): # This function prints summary of costs and total expense for holiday.
   hotel_expense = hotel_cost(num_nights)
   flight_expense = plane_cost(city_flight)
   rental_expense = car_rental(rental_days)
   sum_bills = hotel_expense + flight_expense + rental_expense
   print(f"Here's your summary:\nThe cost of your flight to {city_flight} is £{flight_expense}.")
   print(f"You are staying here for {num_nights} nights and the price of the hotel is £{hotel_expense}.")
   print(f"You are renting a car for {rental_days} days, the total price is £{rental_expense}.")
   print(f"The total cost of your holiday is: {sum_bills}")

car_rental(rental_days)
plane_cost(city_flight)
hotel_cost(num_nights)
holiday_cost(num_nights, city_flight, rental_days)