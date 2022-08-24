def yes_no(question):
    valid = False
    while not valid:
        responce = input(question).lower()

        if responce == "yes" or responce == "y":
            responce = "yes"
            return responce
        elif responce == "no" or responce == "n":
            responce = "no"
            return responce

        else:
            print("please answer yes / no")

def instrucyions():
    print("***** How To Play *****\n")
    print()
    print("""Welcome to Lucky Unicorn, the cost is $1 per round to play.
if you get a unicorn you get 5$.
if you receive a horse or zebra you win 50c.
A donkey gets you nothing""")
    print()
    return ""

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
10
show_instructions = yes_no ("have you played this game before:")

if show_instructions == "no":
    instrucyions()

how_much = num_check("how much would you like to play with:",0 , 10)


print("program continue")
