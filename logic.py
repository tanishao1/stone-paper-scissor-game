from utils.constants import WIN_MSG, LOSE_MSG, DRAW_MSG

def decide_winner(user, computer):
    if user == computer:
        return DRAW_MSG

    if (
        (user == "Stone" and computer == "Scissor") or
        (user == "Paper" and computer == "Stone") or
        (user == "Scissor" and computer == "Paper")
    ):
        return WIN_MSG
    else:
        return LOSE_MSG