balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play again or xxx to quit:")
while play_again == "":

    rounds_played += 1

    print(rounds_played)
    balance -= 1
    print("Balance:", balance)
    print()

    play_again = input("")
