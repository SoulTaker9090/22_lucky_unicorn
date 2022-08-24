import random



Starting_Balance = 100

balance = Starting_Balance

for item in range(0,100):
    chosen_num = random.randint(1,100)

    if 1 <= chosen_num <= 5:
            chosen = "unicorn"
            balance += 4
    elif 6 <= chosen_num <= 36:
            chosen = "donkey"
            balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. your balance is ${:.2f}".format(chosen, balance))

print()
print("Starting balance: ${}".format(Starting_Balance))
print("Final Balance: ${}".format(balance))
