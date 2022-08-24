show_instructions = ""
while show_instructions != "xxx":
    show_instructions = input("have you played this game before:")

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continue:")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("displaying instructions:")

    else:
        print("please enter yes or no:")
