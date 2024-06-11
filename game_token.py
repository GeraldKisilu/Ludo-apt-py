class Token:
    def __init__(self, player, position=0):
        self.player = player
        self.position = position

    def move(self, steps):
        self.position += steps

    def reset(self):
        self.position = 0

    def is_at_home(self):
        return self.position == 0

    def is_finished(self):
        # Assuming the finish position is 56 for simplicity
        return self.position >= 56
