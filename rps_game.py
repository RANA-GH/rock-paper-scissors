import random
class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_last_move = None
        self.opponent_last_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.opponent_last_move = their_move

class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)

class ReflectPlayer(Player):
    def move(self):
        return self.opponent_last_move

class CyclePlayer(Player):
    def move(self):
        if self.my_last_move is None:
            return random.choice(self.moves)
        index = (self.moves.index(self.my_last_move) + 1) % len(self.moves)
        return self.moves[index]

class HumanPlayer(Player):
    def move(self):
        while True:
            human_choice = input("Rock, paper, scissors? > ").lower()
            if human_choice in self.moves:
                return human_choice
            elif human_choice == 'exit':
                exit()

class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.scores = {"Player 1": 0, "Player 2": 0}

    def beats(self, one, two):
        return (one, two) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

    def get_rounds(self):
        while True:
            rounds = input("How many rounds would you like to play? > ")
            if rounds.isdigit():
                return int(rounds)
            elif rounds.lower() == 'exit':
                exit()

    def play_round(self):
        move1, move2 = self.p1.move(), self.p2.move()
        if self.beats(move1, move2):
            self.scores["Player 1"] += 1
            result = "**** PLAYER ONE WINS ****"
        elif move1 == move2:
            result = "**** IT'S A TIE ****"
        else:
            self.scores["Player 2"] += 1
            result = "**** PLAYER TWO WINS ****"

        print(f"\n> You played: {move1}\n> Opponent played: {move2}\n{result}")
        print(f"Score: Player 1 ({self.scores['Player 1']}), Player 2 ({self.scores['Player 2']})")
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\n>>>> Game Start! <<<<")
        print("(Type 'exit' anytime to quit the game)")
        rounds = self.get_rounds()
        for round in range(1, rounds + 1):
            print(f"\nRound {round} --")
            self.play_round()
        
        if self.scores["Player 1"] > self.scores["Player 2"]:
            winner_message = "---- PLAYER ONE WINS THE GAME! ----"
        elif self.scores["Player 1"] < self.scores["Player 2"]:
            winner_message = "---- PLAYER TWO WINS THE GAME! ----"
        else:
            winner_message = "---- IT'S A TIE! ----"
        
        print(f"\n{winner_message}\nFinal Score: Player 1 ({self.scores['Player 1']}), Player 2 ({self.scores['Player 2']})")

if __name__ == '__main__':
    opponent = random.choice([RandomPlayer(), ReflectPlayer(), CyclePlayer()])
    game = Game(HumanPlayer(), opponent)
    game.play_game()
