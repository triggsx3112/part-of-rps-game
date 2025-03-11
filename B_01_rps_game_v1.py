import random


def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


def instructions():
    print('''
 ***instructions***

To begin, choose the number of rounds (or pick infinite mode)

Then play against the computer. You need to pick R (rock), P (paper), S (scissors).

The rules are as follows:
    Paper beats rock
    Rock beats scissors
    scissors beats paper.

Press <xxx> to end the game at anytime

Good luck
    ''')


def int_check(question):

    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def rps_compare(user, comp):

    if user == comp:
        result = "tie"

    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"


    else:
        result = "lose"

    return result



mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("Rock / Paper / Scissors Game")
print()


want_instructions = string_checker("Do you wish to see the instructions for this game? ")


# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()



num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "

    else:
        rounds_heading = f"\n round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    comp_choice = random.choice(rps_list[:-1])

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    if mode == "infinite":
        num_rounds += 1



