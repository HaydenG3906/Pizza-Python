import pandas
import random
from datetime import date


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# set variables
cost = 0
addmodification = 100
selectedpizza = 0
formatmod = ""
selectpizza = "null"
cardnum = 0
cashorcred = "null"
pizza_num_cheese = 0
pizza_num_pepperoni = 0
pizza_num_hamcheese = 0
pizza_num_hawaiian = 0
pizza_num_vegan = 0
MAX_TICKETS = 5
tickets_sold = 0
pizza_ordered = 0
order_print_message = "Please Enter The Pizza wanted. Num of Pizza Ordered {}: ".format(pizza_ordered)

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
delivery_list = ["pickup", "delivery"]
cash_cred_list = ["cash", "credit"]

# Lists to hold ticket details
pizza_types_name = []
pizza_types = []
all_names = []
all_ticket_costs = []
all_surcharge = []
stuffed_crust = [0, 0, 0, 0, 0]


# functions go here


# shows instructions
def show_instructions():
    print('''\n
    ***** Instructions *****
    
Ordering Pizza:
    
    - Enter Amount of Pizza wanted
    - Select Wanted Pizza
    - Select Other Items
    
Delivery and Details

    - Select Delivery or Pick Up In Store
    Enter:
    - Name
    - Address (If Delivery)
    - Phone Number
    
Select If paying now with credit or cash (only if pickup) in store

Enter Payment Details if paying with credits (For the assessment instead of entering a real card
enter a 4 digit number as an example for a card)

Your receipt should print in a text file

*******************************''')


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank. Please try again")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer")


# Calculate the ticket price based on the age
# def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
  #  if var_age < 16:
   #     price = 7.5
    # ticket is $10.50 for users between 16 and 64
    #elif var_age <= 64:
     #   price = 10.5
    # ticket price is $6.50 for seniors (65+)
    #else:
    #    price = 6.5
    #return price


# checks that user enters a valid response based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here


# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask the user if they want to see the instructions

want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

if want_instructions == "yes":
    show_instructions()

print()

while True:
    pizza_wanted = num_check("Enter Number Of Pizzas wanted: ")
    if pizza_wanted > 5:
        print(bcolors.FAIL + "The max amount of pizza that can be ordered at a time is 5" + bcolors.ENDC)
    elif pizza_wanted < 1:
        print(bcolors.FAIL + "You must order at least 1 pizza to continue" + bcolors.ENDC)
    else:
        break

# loop to sell tickets

while pizza_ordered < pizza_wanted:
    print('''List of Pizza: 
          1. Cheese                  $4
          2. Pepperoni               $5
          3. Ham & Cheese            $5
          4. Hawaiian                $5
          5. Vegan                   $6''')
    pizza_inputed = num_check(order_print_message)
    if pizza_inputed > 5 or pizza_inputed < 1:
        order_print_message = bcolors.FAIL + "Please enter a number 1-5: " + bcolors.ENDC
    else:
        pizza_ordered = pizza_ordered + 1 # add 1 too pizza ordered
        order_print_message = "Please Enter The Pizza wanted. Num of Pizza Ordered {}: ".format(pizza_ordered)
        if pizza_inputed == 1:
            pizza_num_cheese = pizza_num_cheese + 1
        elif pizza_inputed == 2:
            pizza_num_pepperoni = pizza_num_pepperoni + 1
        elif pizza_inputed == 3:
            pizza_num_hamcheese = pizza_num_hamcheese + 1
        elif pizza_inputed == 4:
            pizza_num_hawaiian = pizza_num_hawaiian + 1
        elif pizza_inputed == 5:
            pizza_num_vegan = pizza_num_vegan + 1
        pizza_types.append(pizza_inputed)  # put the pizza in the list

        if pizza_inputed == 1:
            pizza_name = "Cheese"
            pizza_types_name.append(pizza_name)
        elif pizza_inputed == 2:
            pizza_name = "Pepperoni"
            pizza_types_name.append(pizza_name)
        elif pizza_inputed == 3:
            pizza_name = "Ham & cheese"
            pizza_types_name.append(pizza_name)
        elif pizza_inputed == 4:
            pizza_name = "Hawaiian"
            pizza_types_name.append(pizza_name)
        elif pizza_inputed == 5:
            pizza_name = "Vegan"
            pizza_types_name.append(pizza_name)
        continue


print('''
******************************************************
''')


# Create a list of tuples containing pizza types and quantities
pizza_quantities = [
    ("Cheese", pizza_num_cheese),
    ("Pepperoni", pizza_num_pepperoni),
    ("Ham and Cheese", pizza_num_hamcheese),
    ("Hawaiian", pizza_num_hawaiian),
    ("Vegan", pizza_num_vegan)
]

# Create a list to hold the formatted strings for each pizza type and quantity
formatted_pizzas = ["{}x {}".format(quantity, pizza_types_name) for pizza_types_name, quantity in pizza_quantities if quantity > 0]

# Use the join method to create the final formatted string
pizza_order_string = ", ".join(formatted_pizzas)

# Print the pizza order string
print("Pizza Ordered: " + pizza_order_string)

print('''
******************************************************
''')


if pizza_wanted >= 1:
    formatmod = pizza_types_name[0]
if pizza_wanted >= 2:
    formatmod = formatmod + ", " + pizza_types_name[1]
if pizza_wanted >= 3:
    formatmod = formatmod + ", " + pizza_types_name[2]
if pizza_wanted >= 4:
    formatmod = formatmod + ", " + pizza_types_name[3]
if pizza_wanted >= 5:
    formatmod = formatmod + ", " + pizza_types_name[4]

while selectpizza != "0":
    pizzamodificaton = string_checker("Would you like to modify a pizza? ", 1, yes_no_list)
    while pizzamodificaton == "yes":

        # Split formatmod into a list of pizza types
        pizza_types_selected = formatmod.split(", ")

        print("Pizzas:")
        # Iterate through the selected pizza types and print them with their corresponding index
        for index, pizza_type in enumerate(pizza_types_name, start=1):
            print("{}. {}".format(index, pizza_type))


        selectpizzanum = num_check("Select a Pizza to modify or '0' to stop modifying: ")

        addmodification = 50 # reset

        if selectpizzanum > pizza_wanted:
            print("Please select a valid Number")
        elif selectpizzanum == 1:
            selectedpizza = pizza_types_name[0]
        elif selectpizzanum == 2:
            selectedpizza = pizza_types_name[1]
        elif selectpizzanum == 3:
            selectedpizza = pizza_types_name[2]
        elif selectpizzanum == 4:
            selectedpizza = pizza_types_name[3]
        elif selectpizzanum == 5:
            selectedpizza = pizza_types_name[4]
        elif selectpizzanum == 0:
            break

        while addmodification != 0:
            print("")
            print("Pizza Selected: " + selectedpizza)
            print('''
Options:
1. Meat                $3
2. Cheese              $2
3. Sauce               $1
4. Stuffed Crust       $3''')
            addmodification = num_check("Select What to add to Pizza or '0' to end: ")

            if addmodification == 1:
                selectedpizza = selectedpizza + " + Meat"
                cost = cost + 3
                pizza_types_name[selectpizzanum - 1] = selectedpizza
            elif addmodification == 2:
                selectedpizza = selectedpizza + " + Cheese"
                cost = cost + 2
                pizza_types_name[selectpizzanum - 1] = selectedpizza
            elif addmodification == 3:
                selectedpizza = selectedpizza + " + Sauce"
                cost = cost + 1
                pizza_types_name[selectpizzanum - 1] = selectedpizza
            elif addmodification == 4:
                if stuffed_crust[selectpizzanum - 1] == 0:
                    selectedpizza = selectedpizza + " + Stuffed Crust"
                    cost = cost + 3
                    pizza_types_name[selectpizzanum - 1] = selectedpizza
                    stuffed_crust[selectpizzanum - 1] = 1
                else:
                    print(bcolors.FAIL + "stuffed crust can only be added once" + bcolors.ENDC)
            elif addmodification == 0:
                selectpizza = "0"
                break
            else:
                print(bcolors.FAIL + "Enter a valid modification" + bcolors.ENDC)

    else:
        break
cost = cost + pizza_num_cheese * 4 + pizza_num_pepperoni * 5 + pizza_num_hamcheese * 5 + pizza_num_hawaiian * 5 + pizza_num_vegan * 6

print("current cost: ${}".format(cost))
delivery_method = string_checker("Choose a delivery method Pickup / "
                            "Delivery (+$10): ",
                            1, delivery_list)

if delivery_method == "delivery":
    cashorcred = "credit"
    cost = cost + 10
    addressstreet = not_blank("Enter Street Name: ")
    addressnum = num_check("Enter Street Number: ")
    cardnum = 0
else:
    cashorcred = string_checker("Are you paying with cash or credit: ", 2, cash_cred_list)
    if cashorcred == "credit":
        cardnum = 0


name = not_blank("Please enter your name: ")
while True:
    phonenum = num_check("Please enter your phone number (no spaces): +64 ")
    if phonenum > 9999999999 or phonenum < 999999999:
        print("Please enter a valid Phone number")
    else:
        break

print("Total: ${}".format(cost))

while cardnum == 0:
    if delivery_method == "delivery" or cashorcred == "credit":
        cardnum = num_check("enter credit card number (for assessment enter 4 digits): ")
        if cardnum > 9999 or cardnum < 999:
            cardnum = 0
            print("Please enter a valid card (4 digits cannot start with 0)")
    else:
        break

if cashorcred == "credit":
    strnumber = int(str(cardnum)[0])
    strnumber2 = int(str(cardnum)[1])
    censoredcard = "{}{}**".format(strnumber, strnumber2)
print()
print("***********************************************************")
print()
print(bcolors.BOLD + "Details:" + bcolors.ENDC)
print("Name: {}".format(name))
print("Phone Number: +64 {}".format(phonenum))
print()
print(bcolors.BOLD + "Pizzas:" + bcolors.ENDC)
# Iterate through the selected pizza types and print them with their corresponding index
for index, pizza_type in enumerate(pizza_types_name, start=1):
    print("{}. {}".format(index, pizza_type))
print()
if delivery_method == "delivery":
    print("Deliver to {} {}".format(addressnum, addressstreet))
else:
    print("Pickup In store")
print()
print(cashorcred)
if cashorcred == "credit":
    print("Card Number {}".format(censoredcard))
print("${}".format(cost))
print()
confirm = string_checker("Confirm? ", 1, yes_no_list)
if confirm == "no":
    confirmation = string_checker("Are you Sure you wish to Delete Your order? ", 1, yes_no_list)
    if confirmation == "yes":
        print(bcolors.FAIL + "Order Was Deleted")
        exit()

print('''
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] 
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5


# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing....
ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit : ${:.2f}".format(profit)

# edit text below!! It needs to work if we have unsold tickets
sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${}. ie: Their Ticket is " \
              "free!".format(winner_name, total_won)

# list holding content to print / write to file

to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()


print(heading)
print()

# output table with ticket data
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total ticket profit ${:.2f}".format(profit))
''')