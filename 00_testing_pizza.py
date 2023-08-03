import random
from datetime import date

class bcolors:
    # ... (color codes for printing)

# Lists to hold pizza details
pizza_types = [
    {"name": "Cheese", "price": 4},
    {"name": "Pepperoni", "price": 5},
    {"name": "Ham & Cheese", "price": 5},
    {"name": "Hawaiian", "price": 5},
    {"name": "Vegan", "price": 6}
]

# Functions go here

# Shows instructions
def show_instructions():
    # ... (instructions)

# Checks that user response is not blank
def not_blank(question):
    # ... (input validation)

# Checks users enter an integer to a given question
def num_check(question):
    # ... (input validation)

# Checks that user enters a valid response based on a list of options
def string_checker(question, valid_responses):
    # ... (input validation)

# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Main routine starts here

show_instructions()

while True:
    pizza_wanted = num_check("Enter the number of pizzas wanted (max 5): ")
    if pizza_wanted > 5:
        print(bcolors.FAIL + "The maximum number of pizzas that can be ordered at a time is 5" + bcolors.ENDC)
    elif pizza_wanted < 1:
        print(bcolors.FAIL + "You must order at least 1 pizza to continue" + bcolors.ENDC)
    else:
        break

# Loop to sell pizzas
pizza_ordered = 0
selected_pizzas = []

while pizza_ordered < pizza_wanted:
    print("List of Pizzas:")
    for index, pizza in enumerate(pizza_types, start=1):
        print("{}. {} - ${}".format(index, pizza["name"], pizza["price"]))

    pizza_inputed = num_check("Select a Pizza (1-5) or '0' to stop ordering: ")

    if pizza_inputed == 0:
        break
    elif 1 <= pizza_inputed <= 5:
        selected_pizza = pizza_types[pizza_inputed - 1]
        cost += selected_pizza["price"]
        pizza_ordered += 1
        selected_pizzas.append(selected_pizza["name"])
        print("You selected: {}".format(selected_pizza["name"]))
    else:
        print(bcolors.FAIL + "Please enter a valid number (1-5)" + bcolors.ENDC)

print("\n***** Order Summary *****")
print("Total Pizzas Ordered:", pizza_ordered)

# Print selected pizzas with modifications
if selected_pizzas:
    print("Selected Pizzas:")
    for pizza in selected_pizzas:
        print("- " + pizza)

print("Total Cost: {}".format(currency(cost)))

# Rest of the code for delivery, payment, and writing to file can be added here based on your requirements.
