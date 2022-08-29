import random

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
    print("Choose a starting amount (minimum $1, maximum $10)")
    print()
    print("Then press <enter> to play. you will either get a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1)")
    print()
    print("Can you avoid the donkeys, get the unicorns and walk home with the money??")
    print()
    print("Hint: to quit while your ahead, type 'xxx' instead of pressing <enter>")
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

def statement_generator (statement, decoration):

    sides = decoration * 3


    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

statement_generator("Welcome to Lucky Unicorn Game:", "*")
print()
show_instructions = yes_no ("have you played this game before:")

if show_instructions == "no":
    instrucyions()

how_much = num_check("how much would you like to play with:",0 , 10)


print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <Enter>...").lower()
while play_again == "":

    rounds_played += 1
    print()
    print("*** Rounds #{} ***".format(rounds_played))

    chosen_num = random.randint(1,100)

    if 1 <= chosen_num <= 5:
            chosen = "unicorn"
            prize_decoration = "!"
            balance += 4
    elif 6 <= chosen_num <= 36:
        prize_decoration = "D"
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance <1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit:")

print()
print("Final balance", balance)
