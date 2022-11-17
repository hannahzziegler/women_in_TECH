class PlayerX:
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
    
    def turn(self):
        """Takes a turn.
        """


class PlayerO(PlayerX):
    """_summary_

    Args:
        PlayerX (_type_): _description_
    """


class BoardState:
    """Provide information on the current state of the game. Used in the
    PlayerX.turn() method.
    """
    def __init__(self):
        """_summary_
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
        """_summary_
        """
        
    def check_four(self):
        """Determines if the game is over, i.e. if a player has four connected
        four pieces in a row vertically, horizontally, or diagonally.
        """
        

class PowerUp:
    """A power-up used during a Connect Four game.
    """
    def __init__(self):
        """_summary_
        """
    
    def invert(self):
        """Transforms all X's on the game board to O's, and vice versa.
        """
    
    def randomize(self):
        """Randomizes the positions of all pieces on the game board.
        """


 
def main():
    """Sets up and plays a game of Connect Four.
    """