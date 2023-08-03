def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer")


number = num_check("enter: ")
strnumber = int(str(number)[0])
strnumber2 = int(str(number)[1])
truenumber = "{}{}".format(strnumber, strnumber2)
print("{}**".format(truenumber))
