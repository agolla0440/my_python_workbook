import random


def play():
    user = input(" What is your choice,"
                 "'r',(r is for rock) 'p',(p is for paper) 's'(s s for scissors): ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "Congrats you won"

    return "Sorry you lost"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
