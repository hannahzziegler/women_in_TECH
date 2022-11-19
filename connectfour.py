"""A Connect Four game that can be played by two players and involves 
power-ups."""

import argparse
import sys

class PlayerX:
    """Represents a turn taken by Player X in the Connect Four game.

    Attributes: 
        piece (str) = a piece on the board
    """

    def __init__(self, name):
        """Creates a piece attribute.

        Args:
            name (str) = the player's name
        """

    def turn(self, state):
        """Prompts a player to take their turn and place their piece in a 
        column. Takes a turn.

        Args:
            state (BoardState) = the current state of the game

        Returns:
            (int) the column in which Player X will place a piece
        """



class PlayerO(PlayerX):
    """Represents a turn taken by Player O in the Connect Four game.

    Args:
        PlayerX (class): the parent class 

    Returns:
        (int) the column in which Player O will place a piece
    """



class BoardState:
    """Provides information on the current state of the game. Used in the
    PlayerX.turn() method."""

    def __init__(self):
        """Initializes the board state."""

    def __str__(self):
        """Returns a string representation of the board."""



class Board:
    """A Connect Four game."""
    def __init__(self):
        """Initializes the Board class."""

    def generate_board(self):
        """Returns the current state of the Connect Four board as a BoardState
        object."""

    def turn(self, player):
        """Manages the player's turn.

        Args:
            player (PlayerX, PlayerO): the player whose turn it is

        Side effects:
            prints to stdout
        """
        state = self.state()
        while True:
            column = int(player.turn(state))
            if column.isdigit() == False or (column < 1 or 7 < column):
                # user did not give an integer OR user gave invalid integer
                input("You must choose a number between 1 and 7 OR use your "
                      "power-up. Enter a new column number or type "
                      "\"power-up\": ") 
            else:
                #user gave a valid column
                continue
                
                
            
        
        # Alerts the user when they attempt to make an invalid move
            # Column number does not exist
            # Column selected is already full
            # Other nonsense responses

    def play(self, state):
        """Play Connect Four (group note: while self.check_four is None, 
        play continues)

        Args:
            state (BoardState) = the current state of the game
        
        Side effects:
            writes to stdout.
        """
        while self.check_four(self.state) == None & "" in self.state.values():
            
            
            

    def check_four(self, state):
        """Determines if the game is over, i.e. if a player has four connected
        four pieces in a row vertically, horizontally, or diagonally.

        Args:
            state (BoardState): the current state of the board 

        Returns:
            "win" if a player has won, "tie" if there are no winners/no possible
            moves, None if the game is not over
        """
        diag_count = 0
        
        


class PowerUp:
    """A power-up used by a player during a Connect Four game."""

    def __init__(self):
        """initializes a power-up object."""

    def invert(self, state):
        """Transforms all X's on the game board to O's, and vice versa.

        Args:
            state (BoardState): the state of the board

        Side effects:
            passes new information to BoardState
        """

    def randomize(self, state):
        """Randomizes the positions of all pieces on the game board.

        Args:
            state (BoardState): the state of the board

        Side effects: 
            passes new information to BoardState
        """


def main(name1, name2):
    """Sets up and plays a game of Connect Four.

    Args:
        name1 (str) = playerX's name
        name2 (str) = playerO's name

    Side effects:
        writes to stdout
    """


def parse_args(arglist):
    """Parse command-line arguments.

    Expects two mandatory arguments: 
        name1 (str) = name of player X
        name2 (str) = name of player O

    Args:
        arglist (list of str): arguments from the command line.

    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("name1", help="the name of the first person")
    parser.add_argument("name2", help="the name of the second person")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name1, args.name2)
