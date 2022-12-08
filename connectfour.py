"""A Connect Four game that can be played by two players and involves 
power-ups."""
# REMINDER GUYS: WRITE A LOT OF COMMENTS
# Each team member must contribute at least 2 functions or methods

# List of things everyone is doing:
# CHRISTINA:
# HANNAH: lambda expression, optional parameter
# EMILY: with statements (file),
# TASFIA:
# PARKER: magic method besides init, argparse

# Potential things for more complexity later:
# Pandas? Stats for one/multiple games
# Regex that shit somehow

import argparse
import sys
import random


class Player:
    """Represents a turn taken by a Player in the Connect Four game.

    Attributes: 
        piece (str) = a piece on the board
    """

    def __init__(self, name):
        self.name = name
        """Creates a piece attribute.

        Args:
            name (str) = the player's name
        """

    def turn(self, state, powerup=None):
        """Prompts a player to take their turn and place their piece in a 
        column. Takes a turn.

        Args:
            state (BoardState) = the current state of the game

        Returns:
            (int) the column in which the Player will place a piece
            #CHECK TO SEE IF THIS IS CLEAR WITH ARIC
        """
        state = self.state
        print(self.state)
        player_piece = int(input(
            f"Hello {self.name}! Please enter a valid column to place your piece (valid columns: 1-7) or use a power-up by typing 'power-up':"))
        if player_piece in range(1-7):
            return player_piece
        if player_piece == 'power-up':
            powerup = random.choice(PowerUp.invert, PowerUp.randomize)
            return powerup

        # HANNAH


class BoardState:
    """Provides information on the current state of the game. Used in the
    Player.turn() method.

    Attributes:
        board (dict of (int, int):str): a representation of the board, with
            columns represented as pipes (|s) and empty spots represented with
            spaces. Positions on the board are represented via coordinates of
            (int, int), with the bottom left spot as (1,1)

    """

    def __init__(self):
        """Sets attributes."""
        # CHRISTINA
        # This is a dictionary that sets the coordinates for each board position
        # (x,y): x=column(1-7), y=row(1-6)
        self.board = {
            (1, 1): "",
            (1, 2): "",
            (1, 3): "",
            (1, 4): "",
            (1, 5): "",
            (1, 6): "",
            (2, 1): "",
            (2, 2): "",
            (2, 3): "",
            (2, 4): "",
            (2, 5): "",
            (2, 6): "",
            (3, 1): "",
            (3, 2): "",
            (3, 3): "",
            (3, 4): "",
            (3, 5): "",
            (3, 6): "",
            (4, 1): "",
            (4, 2): "",
            (4, 3): "",
            (4, 4): "",
            (4, 5): "",
            (4, 6): "",
            (5, 1): "",
            (5, 2): "",
            (5, 3): "",
            (5, 4): "",
            (5, 5): "",
            (5, 6): "",
            (6, 1): "",
            (6, 2): "",
            (6, 3): "",
            (6, 4): "",
            (6, 5): "",
            (6, 6): "",
            (7, 1): "",
            (7, 2): "",
            (7, 3): "",
            (7, 4): "",
            (7, 5): "",
            (7, 6): ""
        }
        # I think i might need another function in here that decides the value
        # of each key. unsure if that goes under another method

    def __str__(self):
        """Returns a string representation of the board."""
        return f"The board is currently at {self.board}"
        # PARKER


class Board:
    """A Connect Four game.

    Attributes:

    """
    # This needs an Attributes section later?

    def __init__(self):
        """Initializes the Board class."""
        # PARKER
        # Write more for docstring later!

    def generate_board(self):
        """Returns the current state of the Connect Four board as a BoardState
        object."""
        # TASFIA
        # Aric said it won't count towards points in the project
        # If more complexity is needed, we'll add another power up

    def turn(self, player):
        """Manages the player's turn.

        Args:
            player (Player): the player whose turn it is

        Side effects:
            prints to stdout
        """
        # TASFIA
        state = self.state()
        while True:
            column = int(player.turn(state))
            if column.isdigit() == False or (column < 1 or 7 < column):
                # user did not give an integer OR user gave invalid integer
                input("You must choose a number between 1 and 7 OR use your "
                      "power-up. Enter a new column number or type "
                      "\"power-up\": ")
            else:
                # user gave a valid column
                continue

        # Alerts the user when they attempt to make an invalid move
            # Column number does not exist
            # Column selected is already full
            # Other nonsense responses

        # Also account for the player wanting to save progress at any time
        # Power up is an optional parameter so remember that

    def play(self, state):
        """Play Connect Four (group note: while self.check_four is None, 
        play continues)

        Args:
            state (BoardState) = the current state of the game

        Side effects:
            writes to stdout.
        """
        # EMILY
        while ((self.check_four(self.state) == None) &
               ("" in self.state.values())):
            return state.board
        
    def save_progress(self, state):
        """Writes the game progress to a text file. Reopens a text file and
        resumes a game.

        Args:
            state (BoardState) = the current state of the game

        Side effects:
            creates and writes the game progress to a text file
            reads in a text file and resumes a game
        """
        with open("filename", "w") as f:
            f.write(state.board)
            f.close()
        # EMILY

    def check_four(self, state):
        """Determines if the game is over, i.e. if a player has four connected
        four pieces in a row vertically, horizontally, or diagonally.

        Args:
            state (BoardState): the current state of the board 

        Returns:
            "win" if a player has won, "tie" if there are no winners/no possible
            moves, None if the game is not over
        """
        # CHRISTINA
        # Initializing some counters for number of pieces in a line
        vert_count = 1
        horiz_count = 1
        pdiag_count = 1
        ndiag_count = 1

        # Initializing a counter for calculating if there's a tie
        played_positions = 0

        # Iterate through every position in the board
        for position in state.board:
            # piece is equivalent to 'x' or 'o'
            piece = state.board[position]
            # Isolate out the coordinates of position
            x, y = position

            # Skipping over empty spots on the board
            if piece:
                # Counting to see if there's a tie
                played_positions += 1

                # While loop that will end when we have 4 in a row
                while (vert_count or horiz_count or
                       pdiag_count or ndiag_count) < 4:
                    # Check for a vertical win
                    while (state.board.get((x, y+vert_count)) or
                           state.board.get((x, y-vert_count))) == piece:
                        vert_count += 1

                    # Check for a horizontal win
                    while (state.board.get((x+horiz_count, y)) or
                           state.board.get((x-horiz_count, y))) == piece:
                        horiz_count += 1

                    # Check for a diagonal win in the positive direction
                    while ((state.board.get((x+pdiag_count, y+pdiag_count)) or
                           state.board.get((x-pdiag_count, y-pdiag_count)))
                           == piece):
                        pdiag_count += 1

                    # Check for a diagonal win in the negative direction
                    while ((state.board.get((x+ndiag_count, y-ndiag_count)) or
                           state.board.get((x-ndiag_count, y+ndiag_count)))
                           == piece):
                        ndiag_count += 1

        # Figuring out what to return based on the iterations through the board
        if (vert_count or horiz_count or pdiag_count or ndiag_count) == 4:
            return "win"
        elif played_positions == 42:
            return "tie"
        else:
            return None


class PowerUp:
    """A power-up used by a player during a Connect Four game."""

    def __init__(self):
        """initializes a power-up object."""
        # Write more for docstring later!

    def invert(self, state):
        """Transforms all X's on the game board to O's, and vice versa.

        Args:
            state (BoardState): the state of the board

        Side effects:
            passes new information to BoardState
        """
        for position in state.board:
            # iterating through each position in the board
            piece = state.board[position]
            # each piece is X or O
            if piece == "X":
                piece == "O"
            elif piece == "O":
                piece == "X"
            else:
                piece == ""
        return state.board
        # return the state of the board

    def randomize(self, state):
        """Randomizes the positions of all pieces on the game board.

        Args:
            state (BoardState): the state of the board

        Returns:
            passes new information to BoardState
        """
        # HANNAH
        # potentially lambda expression????


def main(name1, name2):
    """Sets up and plays a game of Connect Four.

    Args:
        name1 (str) = playerX's name
        name2 (str) = playerO's name

    Side effects:
        writes to stdout
    """
    # PARKER


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
    # PARKER
    parser = argparse.ArgumentParser()
    parser.add_argument("name1", help="the name of the first person")
    parser.add_argument("name2", help="the name of the second person")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name1, args.name2)
