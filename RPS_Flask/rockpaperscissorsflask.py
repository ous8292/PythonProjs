from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/play/<move>')
def play_move(move):
    computer_move = [Rock, Paper, Scissor]
    random_move = (random.choice(computer_move))

    if move == "rock":
        player_move = Rock()
    elif move == "paper":
        player_move = Paper()
    elif move == "scissor":
        player_move = Scissor()
    else:
        return "Choose rock, paper, or scissor"
    #result = player_move.compare(random_move)

    if random_move in player_move.wins_against:
        result = 'won'
    elif random_move in player_move.loses_against:
        result = 'loss'
    elif random_move in player_move.ties_against:
        result = 'tie'
    return f"You {result}, you chose {move} and the computer chose {random_move}"

class Rock:
    def __init__(self):
        self.loses_against = [Paper]
        self.wins_against = [Scissor]
        self.ties_against = [Rock]

    # def compare(self, move):
    #     if move == "rock":
    #         return "Tie"
    #     elif move == "paper":
    #         return "lost"
    #     elif move == "scissor":
    #         return "won"

class Paper:
    def __init__(self):
        self.loses_against = [Scissor]
        self.wins_against = [Rock]
        self.ties_against = [Paper]
    # def compare(self, move):
    #     if move == "paper":
    #         return "tie"
    #     elif move == "scissor":
    #         return "lost"
    #     elif move == "rock":
    #         return "won"


class Scissor:
    def __init__(self):
        self.loses_against = [Rock]
        self.wins_against = [Paper]
        self.ties_against = [Scissor]
    # def compare(self, move):
    #     if move == "scissor":
    #         return "tie"
    #     elif move == "rock":
    #         return "lost"
    #     elif move == "paper":
    #         return "won"



# x = Scissor()
# print(x.compare("paper"))
#
# #unit test: tests if something works, a particular unit.. one function, one class, one ect...
# def test_scissors():
#     scissors = Scissor()
#     result = scissors.compare('paper')
#     assert result == 'won'
#
# test_scissors()