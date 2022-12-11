"""A Connect Four game (with power-ups!) that can be played against a
computer."""
# REMINDER GUYS: WRITE A LOT OF COMMENTS
# Each team member must contribute at least 2 functions or methods

# List of things everyone is doing:
# CHRISTINA: conditional expressions, sequence unpacking (tentative)
# HANNAH: set stuff, list/dict comprehensions
# EMILY: with statements (file), inheritance
# TASFIA: optional parameter, f-string
# PARKER: magic method besides init, argparse

import argparse
import sys
import random


class Player:
    """Represents a turn taken by a Player in the Connect Four game.

    Attributes: 
        piece (str): a piece on the board
    """

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        """Creates a player name attribute.

        Args:
            name (str): the player's name
        """

        def turn(self, state):
            raise NotImplementedError
        # CHRISTINA: i'm confused about what this method does and why it's
        # nested under the init??
        


class HumanPlayer(Player):
    def turn(self, state):
        """Prompts a player to take their turn and place their piece in a 
        column. Takes a turn.

        Args:
            state (BoardState): the current state of the game

        Returns:
            human_choice (str): the human player's choice of what to do with
                their turn (a number (1-7) or 'power-up')
        """
        print(state)
        #self.piece = input(f"Hello {self.name}. Would you like to use 'x' as your token or 'o'? ")
        # if self.piece == 'x':
        # Hannah: struggling with assigning diff pieces to players
        # CHRISTINA: honestly, i think we can just make the human x every time
        # coding in a choice is nice but superfluous in terms of functionality

        powerup_count = 2
        human_choice = input(
            f"{self.name}, please enter a valid column to place your "
            "piece (valid columns: 1-7) or use a power-up by typing "
            "'power-up':")
        if human_choice == 'power-up':
            powerup_count = powerup_count - 1
        return human_choice, human_piece #we can erase human_piece if human will be x every time


class ComputerPlayer(Player):
    """Represents a computer playing connect four. 

    Attributes:
        piece (str): a piece on the board
    """

    def turn(self, state):
        # CHRISTINA: write a docstring for this 
        print(state)
        computer_piece = 'o'
        powerup_count = 2
        column_list = [1, 2, 3, 4, 5, 6, 7]
        if self.turn_counter <= 10:
            computer_player_choice = random.choice(column_list)
        elif self.turn_counter > 10 and powerup_count > 1:
            computer_player_choice = random.choice(column_list, "power-up")
        if computer_player_choice == "power-up":
            powerup_count = powerup_count - 1
            # CHRISTINA: where is the code that says, "don't let the computer
            # play a power-up if it has already used them all up" ?
        return computer_player_choice, computer_piece
    # don't worry about making it too smart


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
        def piece_or_blank(player):
            """Return an 'x', 'o', or an empty string, depending on if a piece
            has been played and by whom.

            Args:
                'x' if the turn was played by a HumanPlayer, 'o' if played by a
                    ComputerPlayer, '' if no turn was played
            """
            if isinstance(player, HumanPlayer):
                return "x"
            elif isinstance(player, ComputerPlayer):
                return "o"
            else:
                return ""
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
        
        # CHRISTINA: honestly have no idea what i'm doing rn but hopefully this
        # gives me a launch point for tomorrow
        self.board = {position: piece_or_blank(player) for position in self.board}

    def __str__(self):
        """Returns a string representation of the board."""
        return f"The current board:\n\
        (| {self.board[36]}| {self.board[37]} | {self.board[38]} |\
        {self.board[39]} | {self.board[40]} | {self.board[41]} |)\n \
        (| {self.board[30]}| {self.board[31]} | {self.board[32]} |\
        {self.board[33]} | {self.board[34]} | {self.board[35]} |)\n\
        (| {self.board[24]}| {self.board[25]} | {self.board[26]} \
        | {self.board[27]} | {self.board[28]} | {self.board[29]} |)\n\
        (| {self.board[18]}| {self.board[19]} | {self.board[20]} |\
        {self.board[21]} | {self.board[22]} | {self.board[23]} |)\n\
        (| {self.board[12]}| {self.board[13]} | {self.board[14]} |\
        {self.board[15]} | {self.board[16]} | {self.board[17]} |)\n\
        (| {self.board[6]} | {self.board[7]} | {self.board[8]} |\
        {self.board[9]} | {self.board[10]} | {self.board[11]} |)\n\
        (| {self.board[0]} | {self.board[1]} | {self.board[2]} |\
        {self.board[3]} | {self.board[4]} | {self.board[5]} |)\n"
        # PARKER


class Board:
    """A Connect Four game.

    Attributes:

    """
    # This needs an Attributes section later?

    def __init__(self, board, turn_counter):
        """Initializes the Board class.

        Args:
            board (str) = represents the board the game is played on
            turn_counter (str) = represents the number of turns played in the game
        """
        self.board = board
        self.turn_counter = turn_counter

        # PARKER

    def generate_board(self):
        """Returns the current state of the Connect Four board as a BoardState
        object."""
        return BoardState(self.board)
        # TASFIA
        # Aric said it won't count towards points in the project
        # If more complexity is needed, we'll add another power up
        # CHRISTINA: i have a feeling this might need to be more complicated. revisit later

    # optional parameter, when powerup is available.
    def turn(self, player, powerup=None):
        """Manages the player's turn.

        Args:
            player (Player): the player whose turn it is
            powerup (string, optional): the potential powerup used

        Side effects:
            prints to stdout
        """
        # TASFIA
        state = self.state()
        while True:
            column = int(player.turn(state))
            if not column.isdigit() or (column < 1 or 7 < column):
                # user did not give an integer OR user gave invalid integer
                print("You must choose a number between 1 and 7 OR use your "
                      "power-up.")
                player.turn()

            elif column == None:  # if the column selected is already full
                print(f"{column} is currently full. Please choose another column.")
                player.turn()

            elif column == 'power-up' and powerup != None:  # this is to check if the player actually has powerups
                # these are the powerups that could be chosen
                powerup = random.choice(invert, randomize)
                # going to account for if we get other powerups
                print(f"You have used {powerup}")
                return powerup

            elif column == 'power-up' and powerup == None:
                print(
                    "You do not have any powerups. Enter a new column between 1 and 7.")
                player.turn()
                # CHRISTINA: changed every Player to player. you don't need to call
                # the class because player is your Player object
            else:
                # user gave a valid column
                self.turn_counter += 1
                continue

        # Christina says to fix the way we choose a random power-up – from my previous code on it when it was in my method
        # Alerts the user when they attempt to make an invalid move
            # Column number does not exist
            # Column selected is already full
            # Other nonsense responses

        # Also account for the player wanting to save progress at any time
        # Power up is an optional parameter so remember that

    def play(self):
        """Play Connect Four (group note: while self.check_four is None, 
        play continues)

        Args:
            state (BoardState) = the current state of the game

        Side effects:
            Writes to stdout.
            See also turn().
        """
        # EMILY
        # Initializes turn counter, player
        self.turn_counter = 0
        player_human = None
        # Checks to make sure the game hasn't been won yet
        while ((self.check_four(self.state) == None) &
               ("" in self.state.values())):
            # Increments the turn counter by one
            self.turn_counter += 1
            # CHRISTINA: what in the while loop is actually causing the back and forth of turns?
            # Assuming that the human player always goes first:
            # If the turn counter is even, the player species is the human player
            # If the turn counter is odd, the player species is the computer
            if self.turn_counter % 2 == 0:
                player_human = True
            
            # now that you know which player's turn it is, you should trigger
            # self.turn(player)! there might also be other conditions that must
            # be satisfied before .turn() can be activated, idk
            # play() is also responsible for printing the board at every turn
            # also, once you exit the while loop, play() should call check_four()
            # using the return from check four, print to stdout and declare the winner and loser
            # no need to return anything!! because once play ends, the game is over
            


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
    state.board.update(union_dicts)
    return state.board
    # updates state.board with each key's corresponding values
    # returns state.board


def main(human_name, computer_player=False):
    """Sets up and plays a game of Connect Four.

    Args:
        human_name (str) = human player's name
        name2 (str) = human player's name

    Side effects:
        writes to stdout
    """
    players = HumanPlayer(human_name)
    if computer_player:
        players.append(ComputerPlayer("Computer"))
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
    parser.add_argument("-c", "--computer_player", action="store_true",
                        help="add a computer player")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.computer_player)
