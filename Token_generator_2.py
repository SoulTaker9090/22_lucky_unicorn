import random

tokens = ("unicorn", "horse","horse","horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey",)
Starting_Balance = 100
balance = Starting_Balance

for item in range(0,20):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("Starting balance: ${}".format(Starting_Balance))
print("Final Balance: ${}".format(balance))
