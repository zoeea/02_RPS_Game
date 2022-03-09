# Functions go here
def choice_checker(question):

    error = " Please choose from rock / paper / " \
            "scissors (or xxx or quit)"

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response  == "scissors":
            return response

    # check for exit code...
        elif response == "xxx":
            return response

    # main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("choose rock / paper / "
                                 "scissors (r/p/s)")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))