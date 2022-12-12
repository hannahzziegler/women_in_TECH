"""A Connect Four game (with power-ups!) that can be played against a
computer."""
# REMINDER GUYS: WRITE A LOT OF COMMENTS
# Each team member must contribute at least 2 functions or methods

# List of things everyone is doing:
# CHRISTINA: conditional expressions, sequence unpacking (tentative)
# HANNAH: magic method besides init, argparse
# EMILY: with statements (file), inheritance
# TASFIA: f-string, regex
# PARKER:

# LAST DEBUGGING
# Emily -- update documentation/docstrings based on new board
# Other stuff:
#   Better distinguish between turns (ask Christina for more detail)
#   Emily - Check to see if the write file function works

# DONE DEBUGGING
#   fix str method
#   Hannah - Power ups

import argparse
import sys
import random
import re


class Player:
    """Represents a player in a Connect Four game.

    Attributes: 
        piece (str): a piece on the board

    Citation:
        https://umd.instructure.com/courses/1330825/pages/hangman hangman.py by
        Aric Bills
            Player class is modeled off of the parent player class from hangman.
    """

    def __init__(self, name):
        """Creates a player name attribute.

        Args:
            name (str): the player's name
        """
        self.name = name
        self.powerup = None

    def __str__(self):
        return f"{self.name}"

    def turn(self, state):
        """Take a turn.

        Args:
            state (BoardState): a snapshot of the current game

        Raises:
            NotImplementedError: raised if the method is not present in child
                class(es).
        """
        raise NotImplementedError


class HumanPlayer(Player):
    def turn(self, state):
        """Prompts a player to take their turn and place their piece in a 
        column. Takes a turn.

        Args:
            state (BoardState): the current state of the game

        Side effects:
            prints the state of the game to stdout

        Returns:
            human_choice (str): the human player's choice of what to do with
                their turn (a number (1-7) or 'power-up')

            human_piece (str): the piece (x or o) that the player will 
            participate as. Human players are always 'x'.

        Citation:
        https://umd.instructure.com/courses/1330825/pages/hangman hangman.py by
        Aric Bills
            Human player class is modeled off of the parent player class from 
            hangman. 
            Deviations: initializing turn and powerup variables. Code is 
            mirrored off of returning human piece choice, similar to hangman's
            human letter choice.
        """
        print(state)

        powerup_count = 2
        human_choice = input(
            f"{self.name}, please enter a valid column to place your "
            "piece (valid columns: 1-7) or use a power-up by typing "
            "'power-up':")
        if human_choice == 'power-up':
            powerup_count -= 1
        return human_choice


class ComputerPlayer(Player):
    """Represents a computer playing connect four. 

    Attributes:
        piece (str): a piece on the board

    Citation:
        https://umd.instructure.com/courses/1330825/pages/hangman hangman.py by
        Aric Bills
            Human player class is modeled off of the parent player class from 
            hangman. 
            Deviations: Changing stipulations for when a computer can make
            choices within the game (when to use a powerup vs. when not to). 
            Code is mirrored off of returning computer piece choice, similar to 
            hangman's computer letter choice.
    """

    def turn(self, state, turn_counter):
        """Allows the computer player to take a turn 

        Args:
            state (BoardState): the current state of the game

        Side effects:
            prints the state of the game to stdout

        Returns:
            Returns:
                computer_choice (str): the computer player's choice of what to do 
                with their turn (a number (1-7) or 'power-up')

                computer_piece (str): the piece (x or o) that the player will 
                participate as. Computer players are always 'o'.
        """
        print(state)

        powerup_count = 2
        column_list = ["1", "2", "3", "4", "5", "6", "7"]
        if turn_counter <= 10:
            computer_choice = random.choice(column_list)
        elif turn_counter > 10 and powerup_count > 0:
            column_list.append("power-up")
            computer_choice = random.choice(column_list)
        if computer_choice == "power-up":
            powerup_count -= 1

        return computer_choice


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

    def __str__(self):
        """Returns a string representation of the board."""
        return f"The current board:\n\
        (| {self.board[(1, 6)]}| {self.board[(2, 6)]} | {self.board[(3, 6)]} | {self.board[(4, 6)]} | {self.board[(5, 6)]} | {self.board[(6, 6)]} | {self.board[7, 6]} |)\n\
        (| {self.board[(1, 5)]}| {self.board[(2, 5)]} | {self.board[(3, 5)]} | {self.board[(4, 5)]} | {self.board[(5, 5)]} | {self.board[(6, 5)]} | {self.board[7, 5]} |)\n\
        (| {self.board[(1, 4)]}| {self.board[(2, 4)]} | {self.board[(3, 4)]} | {self.board[(4, 4)]} | {self.board[(5, 4)]} | {self.board[(6, 4)]} | {self.board[7, 4]} |)\n\
        (| {self.board[(1, 3)]}| {self.board[(2, 3)]} | {self.board[(3, 3)]} | {self.board[(4, 3)]} | {self.board[(5, 3)]} | {self.board[(6, 3)]} | {self.board[7, 3]} |)\n\
        (| {self.board[(1, 2)]}| {self.board[(2, 2)]} | {self.board[(3, 2)]} | {self.board[(4, 2)]} | {self.board[(5, 2)]} | {self.board[(6, 2)]} | {self.board[7, 2]} |)\n\
        (| {self.board[(1, 1)]}| {self.board[(2, 1)]} | {self.board[(3, 1)]} | {self.board[(4, 1)]} | {self.board[(5, 1)]} | {self.board[(6, 1)]} | {self.board[7, 1]} |)\n"
        # PARKER


class Board:
    """A Connect Four game.

    Attributes:

    """
    # This needs an Attributes section later?

    def __init__(self, players):
        """Initializes the Board class.

        Args:
            board (str): represents the board the game is played on
            players (list of HumanPlayer, ComputerPlayer): the players
        """
        self.players = players
        self.turn_counter = 0
        self.state = BoardState()

        # PARKER

    # def generate_board(self):
    #     """Returns the current state of the Connect Four board as a BoardState
    #     object."""
    #     return BoardState
        # TASFIA
        # Aric said it won't count towards points in the project
        # If more complexity is needed, we'll add another power up
        # CHRISTINA: i have a feeling this might need to be more complicated. revisit later

    # optional parameter, when powerup is available.
    def turn(self, player):
        """Manages the player's turn.

        Args:
            player (Player): the player whose turn it is

        Side effects:
            prints to stdout
            calls player.turn
            uses self.state attribute 
        """
        # TASFIA
        if isinstance(player, HumanPlayer):
            column = player.turn(self.state)
        else:
            column = player.turn(self.state, self.turn_counter)

        correctcolumn = re.search(
            r"\d|\b((p|P)(ower?)).?((u|U)(p?))\b", column)

        if correctcolumn is not None:  # if the correct column is actually a match

            if column.isdigit():
                column = int(column)
                if column < 1 or 7 < column:
                    # user did not give a invalid integer
                    print("You must choose a number between 1 and 7 OR use your"
                          " power-up.")
                    player.turn(self.state)
                # if the column selected is already full
                elif self.state.board[(column, 6)] != "":
                    print(
                        f"Column {column} is currently full. Please choose another column.")
                    player.turn(self.state)
                else:
                    self.drop_piece(column, player)
            else:
                # this is to check if the player actually has powerups
                if column == 'power-up' and player.powerup is None:
                    # these are the powerups that could be chosen
                    player.powerup = random.choice(["invert", "randomize"])
                    # going to account for if we get other powerups
                    print(f"You have used {player.powerup}")
                    if player.powerup == "invert":
                        self.state.board = invert(self.state)
                        print(str(self.state.board))
                    elif player.powerup == "randomize":
                        self.state.board = randomize(self.state)
                        print(str(self.state.board))

                elif column == 'power-up' and player.powerup is not None:
                    print(
                        "You do not have any powerups. Enter a new column between 1 and 7.")
                    player.turn(self.state)

                else:
                    print(
                        "We recognized you want to use a powerup. Please use the following syntax: power-up")
                    player.turn(self.state)

        elif column == "quit":
            print("Thank you for playing our game!")
            sys.exit()

        else:
            print("This is an invalid input. Try again.")
            player.turn(self.state)

    def drop_piece(self, choice, player):
        """Assigns 'x' or 'o' to a key (determined by choice) in self.board.

        Args:
            choice (str): the column of choice, validated by Board.turn()
            player (HumanPlayer, ComputerPlayer): an object of a Player
                child class
        Returns:
            'x' if the turn was played by a HumanPlayer, 'o' if played by a
                ComputerPlayer, '' if no turn was played
        """
        counter = 1

        while self.state.board[(choice, counter)] != "":
            counter += 1

        self.state.board[(choice, counter)] = ("x" if isinstance(player,
                                                                 HumanPlayer)
                                               else "o")

    def play(self):
        """Play Connect Four (group note: while self.check_four is None, 
        play continues)

        Side effects:
            Writes to stdout.
            See also turn().
        """
        # EMILY

        player = None
        # Checks to make sure the game hasn't been won yet
        while self.check_four() is None:
            # Increments the turn counter by one
            self.turn_counter += 1
            # CHRISTINA: what in the while loop is actually causing the back and forth of turns?
            # Assuming that the human player always goes first:
            # If the turn counter is even, the player species is the human player
            # If the turn counter is odd, the player species is the computer
            if self.turn_counter % 2 == 0:
                player = self.players[1]
            else:
                player = self.players[0]
            self.turn(player)
            print(f"the player that just went is {player.name}")

        # we need to call the game details method somewhere in this play method to get it going
        outcome = self.check_four()
        if outcome == "tie":
            print("The game ended in a tie!")
            self.game_details()
        elif outcome == "win":
            print(f"{str(player)} won! The game lasted {self.turn_counter} turns.")
            self.game_details()

            # note: i took out player_human = False because i initialized it as None

            # now that you know which player's turn it is, you should trigger
            # self.turn(player)! there might also be other conditions that must
            # be satisfied before .turn() can be activated, idk
            # play() is also responsible for printing the board at every turn
            # also, once you exit the while loop, play() should call check_four()
            # using the return from check four, print to stdout and declare the winner and loser
            # no need to return anything!! because once play ends, the game is over

    def check_four(self):
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
        for position in self.state.board:
            # piece is equivalent to 'x' or 'o'
            piece = self.state.board[position]
            # Isolate out the coordinates of position
            x, y = position

            # Skipping over empty spots on the board
            if piece != "":
                # Counting to see if there's a tie
                played_positions += 1

                # Check for a vertical win
                while ((self.state.board.get((x, y+vert_count)) == piece) or
                        (self.state.board.get((x, y-vert_count)) == piece)):
                    vert_count += 1

                # Check for a horizontal win
                while ((self.state.board.get((x+horiz_count, y)) == piece) or
                        (self.state.board.get((x-horiz_count, y)) == piece)):
                    horiz_count += 1

                # Check for a diagonal win in the positive direction
                while ((self.state.board.get((x+pdiag_count, y+pdiag_count))
                        == piece)
                        or
                        (self.state.board.get((x-pdiag_count, y-pdiag_count))
                         == piece)):
                    pdiag_count += 1

                # Check for a diagonal win in the negative direction
                while ((self.state.board.get((x+ndiag_count, y-ndiag_count))
                        == piece)
                        or
                        (self.state.board.get((x-ndiag_count, y+ndiag_count))
                         == piece)):
                    ndiag_count += 1

                print("================================================")
                print(
                    f"vert_count is {vert_count}. horiz_count is {horiz_count}.")
                print(
                    f"pdiag_count is {pdiag_count}. ndiag_count is {ndiag_count}.")
                print("================================================")
                # Figuring out what to return based on the iterations through the board
                if ((vert_count >= 4) or (horiz_count >= 4) or
                        (pdiag_count >= 4) or (ndiag_count >= 4)):
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
        game_file = input("What do you want to call your save file?")
        with open(game_file, "w") as f:
            # Write the string representation of the board state to the file
            f.write(str(state.board))
            # Write an f string of the game's outcome to the file
            f.write(f"""{loser} suffered a humiliating 
                    defeat at the hands of {winner}. 
                    The game lasted {turn_counter} turns.""")


def invert(state):
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


def randomize(state):
    for position in state.board:
        piece = state.board[position]
        if piece == "x":
            state.board[position] = random.choice(['x', 'o'])
        elif piece == "o":
            state.board[position] = random.choice(['x', 'o'])
        else:
            state.board[position] = ""
    return state.board


def elimination(state):
    dictionarycomprehension = {position1 for position1, position2 in state.board}
    randomposition = random.choice(tuple(dictionarycomprehension))
    for piece in state.board:
        piece = state.board[randomposition]
        if piece == "x":
            state.board[randomposition] = ""
        elif piece == "o":
            state.board[randomposition] = ""
    return state.board

# another powerup idea = blocking
# it replaces EVERY x and o into a B
# this "blocks" the board, meaning that you cant use those pieces to win
# you have to work over the pieces instead


# BROKEN RANDOMIZE -- IGNORE
# {state.board[position]: random.choice('x', 'o') for position in state.board if position = 'x'}
    # {state.board[position] == random.choice('x', 'o'): state.board[position] for position in state.board if position = 'x'}

# def randomize(state):
    # """Randomizes the positions of all pieces on the game board.

    # Args:
    # state (BoardState): the state of the board

    # Returns:
    # passes new information to BoardState

    # HANNAH
    # for position in state.board:
    # piece = state.board[position]
    #  value_list = ([(v) for v in piece if v != ""])
    # getting a list of all pieces on the board that have an "X" or "O" in them
    # random.shuffle(value_list)
    # shuffling the order of the "X" and "O" values
    # key_list = ([(k) for k, v in state.board.items() if v != ""])
    # gettng a list of all spots on the board where pieces have been placed
    # dict_with_pieces = {key_list[i]: value_list[i]
    #   for i in range(len(key_list))}
    # concatenating the lists into a new dictionary
    # board_filtered_dict = {}
    # creating an empty dictionary that will have a list of all the spaces
    # on the board without pieces
    # for (key, value) in state.board.items():
    # if value == "":
    # board_filtered_dict[key] = value
    # loop is basically saying 'if there is not a piece in this spot
    # on the board, make it a key value pair in the empty dict
    # union_dicts = dict(dict_with_pieces.items() |
    # board_filtered_dict.items())
    # creating a union where all of the shuffled keys/values that have
    # pieces on them are joined to the ones that remain empty
    # state.board.update(union_dicts)
    # return state.board
    # updates state.board with each key's corresponding values
    # returns state.board


def main(human_name):
    """Sets up and plays a game of Connect Four.

    Args:
        human_name (str) = human player's name

    Side effects:
        writes to stdout
    """
    players = [HumanPlayer(human_name), ComputerPlayer("Computer")]
    game = Board(players)
    game.play()
    # PARKER


def parse_args(arglist):
    """Parse command-line arguments.

    Expects two mandatory arguments: 
        name (str) = name of human player

    Args:
        arglist (list of str): arguments from the command line.

    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    # PARKER
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="the name of the person")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name)
