from board import Board
from dice import Dice
from player import Player
from game import Game

def main():
    # Initialize game components
    board = Board()
    dice = Dice()
    players = [Player(name) for name in ["Player 1", "Player 2", "Player 3", "Player 4"]]
    game = Game(board, dice, players)

    # Start the game loop
    game.start()

if __name__ == "__main__":
    main()
