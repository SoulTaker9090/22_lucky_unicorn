error = "please enter a whole number between 1 and 10\n"



valid = False
while not valid:
    try:
        # ask the question
        responce = int(input("How much would you like to play with:"))
        if 0 < responce <= 10:
            print("You have asked to play with ${}".format(responce))

        else:
            print("error")

    except ValueError:
        print(error)
