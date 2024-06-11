from game_token import Token

class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = [Token(self) for _ in range(4)]

    def move_token(self, token_index, steps):
        self.tokens[token_index].move(steps)

    def reset_token(self, token_index):
        self.tokens[token_index].reset()

    def has_won(self):
        return all(token.is_finished() for token in self.tokens)
