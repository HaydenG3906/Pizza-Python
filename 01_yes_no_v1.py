# functions go here


# main routine goes here
want_instructions = input("Do you want to read the instructions? ").lower()

if want_instructions == "yes":
    print("Instructions go here")
elif want_instructions == "no":
    pass
else:
    print("please answer yes / no")