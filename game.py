class Game:
    def __init__(self, board, dice, players):
        self.board = board
        self.dice = dice
        self.players = players
        self.current_player_index = 0

    def start(self):
        while not self.is_game_over():
            self.play_turn()

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"{current_player.name}'s turn")
        roll = self.dice.roll()
        self.dice.display_roll(roll)

        # Allow the player to move a token based on the roll
        self.move_token(current_player, roll)

        # Check if the player gets another turn
        if roll != 6:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        self.board.display(self.players)

    def move_token(self, player, roll):
        # Prompt the player to choose a token
        token_index = self.choose_token(player)
        if token_index is not None:
            player.move_token(token_index, roll)
        else:
            print(f"{player.name} has no tokens to move.")

    def choose_token(self, player):
        while True:
            try:
                token_index = int(input(f"{player.name}, choose a token to move (0-3): "))
                if 0 <= token_index < len(player.tokens):
                    if not player.tokens[token_index].is_finished():
                        return token_index
                    else:
                        print("This token has already finished. Choose another token.")
                else:
                    print("Invalid token index. Please choose a valid token.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 3.")

    def is_game_over(self):
        # Check if any player has won
        for player in self.players:
            if player.has_won():
                print(f"{player.name} has won the game!")
                return True
        return False
