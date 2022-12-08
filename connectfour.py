"""A Connect Four game that can be played by two players and involves 
power-ups."""
# REMINDER GUYS: WRITE A LOT OF COMMENTS
# Each team member must contribute at least 2 functions or methods

# List of things everyone is doing:
# CHRISTINA: conditional expressions, sequence unpacking (tentative)
# HANNAH: lambda expression, optional parameter
# EMILY: with statements (file), super
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
        #TASFIA
        self.piece = None
        #This is just a placeholder for the piece. I want to see how the piece attribute works in the other methods better before initializing.

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
        # CHRISTINA: idk if it's good practice to call a class by name like this
        # i think it's considered hard coding but we will talk later


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
        #TASFIA
        #Aric said it won't count towards points in the project
        #If more complexity is needed, we'll add another power up

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
            if not column.isdigit() or (column < 1 or 7 < column):
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

        Returns:
        
            Passes new information to board state.
        """
        # EMILY
        #Initializes turn counter
        turn_counter = 0
        # Initializes a blank string for player species
        player_species = ""
        # Checks to make sure the game hasn't been won yet
        while ((self.check_four(self.state) == None) &
               ("" in self.state.values())):
            # Increments the turn counter by one
            turn_counter = turn_counter + 1
        # Assuming that the human player always goes first:
        # If the turn counter is even, the player species is the human player
        if turn_counter % 2 == 0:
            player_human = True
        #If the turn counter is odd, the player species is the computer
        else:
            player_human = False
            return state.board, turn_counter, player_human


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
        
    def game_details(self, state, turn_counter, player_human):
        """Writes the details of a finished game to a text file. 
        
        Args:
        
            state (BoardState): the current state of the board
            turn_counter (int): the value of the turn counter
            player_human (boolean): whether the winner is a human or a computer
            
        Side effects: 
        
            Writes a string representation of the board and a string detailing 
            the game's outcome to a text file. 
            
        """
        # If player_human is true, the winner is the player's name and the 
        # loser is the computer
        if player_human == True:
            winner = Player.name
            loser = "Computer"
        # And vice versa for the else statement
        else:
            winner = "Computer"
            loser = Player.name
        # Here is a demonstration of a with statement   
        # Open a file for writing to 
        with open("finishedgame.txt", "w") as f:
            # Write the string representation of the board state to the file
            f.write(str(state.board))
            # Write an f string of the game's outcome to the file 
            f.write(f"""{loser} suffered a humiliating 
                    defeat at the hands of {winner}. 
                    It took them {turn_counter} turns.""")


class PowerUp:
    """A power-up used by a player during a Connect Four game."""

    def __init__(self):
        """initializes a power-up object."""
        # Write more for docstring later!
        # Ask Aric in office hours

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
            if piece == "x":
                state.board[position] = "o"
            elif piece == "o":
                state.board[position] = "x"
            else:
                state.board[position] = ""
        return state.board
        # return the state of the board
        # CHRISTINA: wouldn't the thing within the clause be state.board[position]?
        # because piece as a variable does not communicate back to GameState in any way
        # also it wouldn't be double ==

    def randomize(self, state):
        """Randomizes the positions of all pieces on the game board.

        Args:
            state (BoardState): the state of the board

        Returns:
            passes new information to BoardState
        """
        # HANNAH
        value_list = ([(v) for v in state.board.values() if v != ""])
        # getting a list of all pieces on the board that have an "X" or "O" in them
        random.shuffle(value_list)
        # shuffling the order of the "X" and "O" values
        key_list = ([(k) for k, v in state.board.items() if v != ""])
        # gettng a list of all spots on the board where pieces have been placed
        dict_with_pieces = {key_list[i]: value_list[i]
                            for i in range(len(key_list))}
        # concatenating the lists into a new dictionary
        board_filtered_dict = {}
        # creating an empty dictionary that will have a list of all the spaces
        # on the board without pieces
        for (key, value) in state.board.items():
            if value == "":
                board_filtered_dict[key] = value
                # loop is basically saying 'if there is not a piece in this spot
                # on the board, make it a key value pair in the empty dict
        union_dicts = dict(dict_with_pieces.items() |
                           board_filtered_dict.items())
        # creating a union where all of the shuffled keys/values that have
        # pieces on them are joined to the ones that remain empty
        sorted_unions = sorted(union_dicts.items(), key=lambda item: item[0])
        # sorting the union of spots with pieces and spots without them to get
        # the matrix looking the same as it did before (i.e. (1,1), (1,2), etc.)
        state.board = sorted_unions
        # reassigning state.board to the new union of pieces/empty spaces
        # ^^ I don't know if this works but we need to somehow make sorted_unions
        # the new board object
        return state.board


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
