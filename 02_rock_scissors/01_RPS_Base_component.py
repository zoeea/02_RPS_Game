import random

# Functions go here


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n "

        # if infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # if response is too low, go bak to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # if response is not an integer go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue

        return response


# def choice_checker(question):
#
#     valid = False
#     while not valid:
#
#         # Ask user for choice
#         response = input(question)
#
#         if response == "r" or response == "rock":
#             return response
#         elif response == "p" or response == "paper":
#             return response
#         elif response == "s" or response  == "scissors":
#             return response
#
#         # check for exit code...
#         elif response == "xxx":
#             return response
#         else:
#             print("error")

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

rounds_played = 0
choose_instructions = "Please choose rock (r), paper " \
                      "(p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    # Start of game play loop

    rounds_played +=1

    # Rounds Heading
    print()
    if rounds == "":
            heading = "Continuous Mode:"
            "Round {}".format(rounds_played)

    else:
            heading = "Rounds {} of {}".format(rounds_played, rounds)

    print(heading)
    choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"
    choose_error = "Please choose from rock /" \
                   "paper / scissors (or xxx to quit)"

    # Ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list,
                            choose_error)

    # end game if exit code is typed
    if choose == "xxx":
        break
    elif rounds_played == rounds:
        break



# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...


# Ask user if they want to see their game history.
# If 'yes' show game history

# Show game statistics