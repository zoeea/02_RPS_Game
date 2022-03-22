# checks user enters yes / no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


# outputs instructions, returns ""
def instructions():
    print("**** How to Play *****")
    print()
    print("The rules of the game go here")
    print()
    print("Choose either a number of rounds or press <enter> for infinite mode")
    print()
    print( "Then for each round, choose from "
          " rock / paper / scissors (or xxx to quit)"
          "You can type r / p / s / x if you don't want to type the whole word" )
    return ""


# checks user enters a number between low and high

# ****** Main routine goes here... *****
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("program continues")

print()

