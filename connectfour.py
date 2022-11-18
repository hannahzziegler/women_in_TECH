from argparse import ArgumentParser

"""A Connect Four game that can be played by two players and involves 
power-ups"""


class PlayerX:
    """Represents a turn taken by player X in the connect four game.

    Attribute: 
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
            the choice of piece placement that player X decided on
        """


class PlayerO(PlayerX):
    """Represents a turn taken 

    Args:
        PlayerX (class): the parent class 

    Returns:
        the choice of piece placement that player O decided on
    """


class BoardState:
    """Provide information on the current state of the game. Used in the
    PlayerX.turn() method.
    """

    def __init__(self):
        """Initializes the board state
        """

    def __str__(self):
        """Returns a string representation of the board.
        """


class Board:
    """A Connect Four game.
    """

    def __init__(self):
        """_summary_
        """

    def generate_board(self):
        """Returns the current state of the Connect Four board as a BoardState
        object
        """

    def turn(self, player):
        """Manages the player's turn

        Args:
            player (PlayerX, PlayerO): the player whose turn it is

        Side effects:
            Alerts the user when they attempt to place a piece in an invalid 
            column
        """

    def play(self):
        """Play Connect Four (group note: while self.check_four is None, 
        play continues)

        Side effects: writes to stdout.
        """

    def check_four(self, state):
        """Determines if the game is over, i.e. if a player has four connected
        four pieces in a row vertically, horizontally, or diagonally.

        Args:
            state (BoardState): the current state of the board 

        Returns:
            "win" if a player has won, "tie" if there are no winners/no possible
            moves, None if the game is not over
        """


class PowerUp:
    """A power-up used during a Connect Four game.
    """

    def __init__(self):
        """initializes a power up object
        """

    def invert(self, state):
        """Transforms all X's on the game board to O's, and vice versa.

        Args:
            state (BoardState): the state of the board

        Side effects: passes new information to BoardState
        """

    def randomize(self, state):
        """Randomizes the positions of all pieces on the game board.

        Args:
            state (BoardState): the state of the board

        Side effects: passes new information to BoardState
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
