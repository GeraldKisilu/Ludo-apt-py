class Board:
    def __init__(self):
        self.layout = self.create_board_layout()

    def create_board_layout(self):
        # Create and return the board layout
        # This is a simplified representation
        return [[' ' for _ in range(15)] for _ in range(15)]

    def display(self, players):
        for row in self.layout:
            print(' '.join(row))
        # Display player tokens
        for player in players:
            for token in player.tokens:
                print(f"{player.name} Token at position {token.position}")
