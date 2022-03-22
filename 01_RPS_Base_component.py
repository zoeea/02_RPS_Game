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
played_before = choice_checker("Have you played the game before? ", ["yes", "no"], "Please enter yes or no")

if played_before == "no":
    instructions()

print("program continues")

print()
# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

rounds_played = 0
choose_instructions = "Please choose rock (r), paper " \
                      "(p) or scissors (s)"
# ask user for # of rounds then loop...
rounds_played = 0 

rounds_lost = 0
rounds_drawn = 0


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

    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # end game if exit code is typed
    if user_choice == "xxx":
            break
    elif rounds_played == rounds:
            break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    

    # end game if exit code is typed
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1


    feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)

    print(feedback)
    



# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...


# Ask user if they want to see their game history.
# If 'yes' show game history

# Show game statistics
# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game statements 
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")