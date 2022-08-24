
show_instructions = ""
while show_instructions.lower() != "xxx":

   show_instructions = input("have you played this game before:").lower()
   if show_instructions == "yes":
       print("program continue")

   elif show_instructions == "y":
       print("program continue")

   elif show_instructions == "no":
       print("displaying instructions:")

   elif show_instructions == "n":
       print("displaying instructions:")

   else:
       print("please answer yes/no")

print("you choose {}".format(show_instructions))

