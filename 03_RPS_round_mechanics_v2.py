# Function used to check input is valid


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0 "
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except