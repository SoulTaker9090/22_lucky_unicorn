def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            responce = int(input(question))
            if low < responce <= high:
                return responce
            else:
                print("error")

        except ValueError:
            print(error)
how_much = num_check("how much would you like to play with:",0 , 10)
