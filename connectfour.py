"""A Connect Four game (with power-ups!) that can be played against a
computer."""
# REMINDER GUYS: WRITE A LOT OF COMMENTS
# Each team member must contribute at least 2 functions or methods

# List of things everyone is doing:
# CHRISTINA: conditional expressions, sequence unpacking (tentative)
# HANNAH: magic method besides init, argparse
# EMILY: with statements ( writing to a text file), inheritance
# TASFIA: comprehension, regex
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
        name (str): the name of the player
        powerup (str): a powerup that can be played during the game

    Citation:
        https://umd.instructure.com/courses/1330825/pages/hangman hangman.py by
        Aric Bills
            Player class is modeled off of the parent player class from hangman.
    """

    def __init__(self, name):
        """Creates a player name attribute.

        Args:
            name (str): the player's name

        Side effects:
            Initializes the name and powerup attributes
        """
        self.name = name
        self.powerup = None

    def __str__(self):
        """Returns a string representation of the player's name."""
        return f"{self.name}"

    def turn(self, state):
        """Takes a turn.

        Args:
            state (BoardState): a snapshot of the current game

        Raises:
            NotImplementedError: raised if the method is not present in child
                class(es).
        """
        raise NotImplementedError


class HumanPlayer(Player):
    def turn(self, state, turn_counter):
        """Prompts a player to take their turn and place their piece in a 
        column. Takes a turn.

        Args:
            state (BoardState): the current state of the game
            turn_counter (int): a counter that counts the number of turns taken

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
        # Prints the current state of the board
        print(state)
        # Sets a counter of available powerups
        powerup_count = 2
        # Prompts the player to choose a column in which to place a piece
        human_choice = input(
            f"{self.name}, please enter a valid column to place your "
            "piece (valid columns: 1-7) or use a power-up by typing "
            "'power-up':")
        # Decrements the powerup counter if a powerup is played
        if human_choice == 'power-up':
            powerup_count -= 1
        return human_choice


class ComputerPlayer(Player):
    """Represents a computer playing connect four. 

    Attributes: 

        name (str): the name of the player
        powerup (str): a powerup that can be played during the game

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
            turn_counter (int): a counter that counts the number of turns taken

        Side effects:
        
            prints the state of the game to stdout

        Returns:
        
            computer_choice (str): the computer player's choice of what to do 
            with their turn (a number (1-7) or 'power-up')
        """
        # This is an example of inheritence, as the ComputerPlayer inherits the 
        # init method from Player
        #Prints the state of the board
        print(state)
        # Sets a powerup counter
        powerup_count = 2
        # Defines the list of choices that the computer can make
        column_list = ["1", "2", "3", "4", "5", "6", "7"]
        #If there are less than 10 pieces on the board, only place a piece
        if turn_counter <= 10:
            computer_choice = random.choice(column_list)
        # If there are more than 10 pieces on the board, you can also play
        # a powerup
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
        """Sets attributes.
        
        Side effects:
        
            Initializes the connect four board. 
            
        """

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
        # HANNAH


class Board:
    """A Connect Four game.

    Attributes:
    
        players (list): the names of the human and computer player
        turn_counter (int): a counter that counts how many turns have been taken
        state (BoardState): the current state of the board
        
    """

    def __init__(self, players):
        """Initializes the Board class.

        Args:
        
            players (list of HumanPlayer, ComputerPlayer): the players
            
        Side effects:
        
            initializes the players, turn_counter, and state attributes
        """
        self.players = players
        self.turn_counter = 0
        self.state = BoardState()

        # PARKER

    def turn(self, player):
        """Ensures that the player's turn is valid, implements any powerups. 

        Args:
            player (Player): the player whose turn it is

        Side effects:
        
            prints to stdout
            changes the state of the board
        """
        # TASFIA
        if isinstance(player, HumanPlayer):
            column = player.turn(self.state, self.turn_counter)
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
                          " power-up. Enter /quit/ to quit the program")
                    player.turn(self.state, self.turn_counter)
                # if the column selected is already full
                elif self.state.board[(column, 6)] != "":
                    print(
                        f"Column {column} is currently full. Please choose another column.")
                    player.turn(self.state, self.turn_counter)
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
                    elif player.powerup == "elimination":
                        self.state.board = elimination(self.state)
                        print(str(self.state.board))

                elif column == 'power-up' and player.powerup is not None:
                    print(
                        "You do not have any powerups. Enter a new column between 1 and 7.")
                    player.turn(self.state, self.turn_counter)

                else:
                    print(
                        "We recognized you want to use a powerup. Please use the following syntax: power-up")
                    player.turn(self.state, self.turn_counter)

        # If the user wants to quit the game 
        elif column == "quit":
            print("Thank you for playing our game!"
                  " "
                  "(Game Credits)"
                  " "
                  "Producer : Christina,"
                  " "
                  "Director : Hannah,"
                  " "
                  "Graphic Designer : Emily,"
                  " "
                  "Visual/Audio : Tasfia,"
                  " "
                  f"Special Thanks To: Players Like You!")
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
        """Plays Connect Four until winning conditions have been met. Tells 
        the user how the game ended. 

        Side effects:
        
            Writes to stdout.
            Calls game_details 
            See also turn().
        """
        # EMILY
        # This is an example of using with statements to write to a file 
        player = None
        # Checks to make sure the game hasn't been won yet
        while self.check_four() is None:
            # Increments the turn counter by one
            self.turn_counter += 1
            # Assuming that the human player always goes first:
            # If the turn counter is even, the player species is the human player
            # If the turn counter is odd, the player species is the computer
            if self.turn_counter % 2 == 0:
                player = self.players[1]
            else:
                player = self.players[0]
            self.turn(player)
            print(f"the player that just went is {player.name}")
        # Checks the outcome of the game, prints the outcome, and calls 
        # game_details to save the details of the game in a text file 
        outcome = self.check_four()
        if outcome == "tie":
            print("The game ended in a tie!")
            self.game_details(self.state.board, self.turn_counter, player)
        elif outcome == "win":
            print(f"{str(player)} won! The game lasted {self.turn_counter} turns.")
            self.game_details(self.state.board, self.turn_counter, player)

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
        
        # Initializing a counter for calculating if there's a tie
        played_positions = 0

        # Iterate through every position in the board
        for position in self.state.board:
            # Initializing some counters for number of pieces in a line
            vert_count = 1
            horiz_count = 1
            pdiag_count = 1
            ndiag_count = 1

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

    def game_details(self, state, turn_counter, player):
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
        if player == True:
            winner = player.name
            loser = "Computer"
        # And vice versa for the else statement
        else:
            winner = "Computer"
            loser = player.name
        # Here is a demonstration of a with statement
        # Open a file for writing to
        game_file = input("What do you want to call your save file?")
        with open(game_file, "w") as f:
            # Write the string representation of the board state to the file
            f.write(str(self.state.board))
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
    """Looks at all x's and o's on the board, randomly changes them to an x or 
    an o. 
    
    Args:
    
        state (BoardState): the state of the board
        
    Side effects:
    
        Passes new information to BoardState
    """
    # For each piece on the board that is x or o, randomly choose whether to 
    # make it x or o 
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
    """Deletes the x's and o's from a random column on the board. 
    
    Args:
    
        state (BoardState): the state of the board
        
    Side effects:
    
        Passes new information to BoardState
    """
    dictionarycomprehension = {
        position1 for position1, position2 in state.board}
    # Chooses a random column
    randomposition = random.choice(tuple(dictionarycomprehension))
    # Checks for x's and o's and removes them
    for piece in state.board:
        piece = state.board[randomposition]
        if piece == "x":
            state.board[randomposition] = ""
        elif piece == "o":
            state.board[randomposition] = ""
    return state.board


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

    Expects one mandatory arguments: 
    
        name (str): name of human player

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
