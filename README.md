# Women in TECH

## INST326 Final Project Documentation: Connect Four Game

Our final project this semester is to create a Connect Four game. The game involves one human player and one computer player competing against each other – but the twist is that each player is able to access a random power up during the game that changes the state of the board as they take their turns. 

<br>
<b>Our Repository Files</b>

In our GitHub repository for the Women in TECH group, we have one primary file for our program to run. That file is “connectfour.py.” We also have one file named “test.txt,” which we created when we had an assignment to make sure that we could all commit and pull to make changes to the repository. Our repository also has a README.md that also contains the documentation that we have in this document. 

<br>
<b>Running the Program From the Command Line</b>

Our program takes one command line argument to run: a string that is the human player’s name. If a user is using a Mac, their command line prompt to run the program should be “python3 connectfour.py personName” as long as the Python file is in their working directory. If a user is using a windows computer, the prompt to run the program should be “python connectfour.py personName”. For example, if Hannah was trying to initiate the program, “python3 connectfour.py hannah”. 

<br>
<b>Using the Program and Interpreting Output</b>

Our program is moderated through the play() method within the overarching Board class. This method involves a while loop that calls all of the necessary classes and methods that are needed to allow a player to take their turn, add that turn to the board and continuously check if a player has won, a column on the board has filled up or if the game has ended in a tie. 
<br>
<br>
When the program begins running, the human player will get prompted to determine a location to set their ‘x’ piece on the Connect Four board. The user input must be a valid column in the range of 1-7. When the user picks a valid column, the Board.turn() class will check to make sure there is room in that given column and then allow the program to continue if the input is valid.
<br>
<br>
If the player does not play a valid column, or their chosen column is full, they will be looped back into the HumanPlayer.turn() method over and over until they give a valid input that allows the program to continue. 
<br>
<br>
Each player in the game is allowed to use up to two power ups to help them throughout the competition. In addition to column values, a player can also type the words ‘power-up’ during their turn to initiate a randomly chosen power-up from the two that we have: invert and randomize. This power-up usage counts as the player’s turn. When a power-up is used, one of the power-up functions gets called, changes the board and returns the new board. 
<br>
<br>
After each turn or each use of a power-up, the player in the game should be able to see the current state of the board. If one player wins as a result of the Board.check_four() method confirming that they have four pieces in a row either vertically, horizontally or diagonally, a statement declaring the winner will print and the game will be over. 

<br>
<b>Project Attribution</b>
<br>
<br>
<em>Classes/Methods/Function each group member is responsible for:</em>
<br>
<br>
Christina Yang:
<li>BoardState __init__() method</li>
<li>Board check_four() method</li>

<br>
Emily Isaacson
<li>Invert function</li>
<li>Board play() method</li>
<li>ComputerPlayer child class</li>
<li>Board game_details() method</li>

<br>
Hannah Ziegler
<li>Randomize function</li>
<li>Player parent class</li>
<li>HumanPlayer child class</li>
<li>main() function</li>
<li>BoardState __str__() method</li>
<li>Parse_ags function</li>

<br>
Tasfia Haque
<li>Eliminate function</li>
<li>Board turn() method</li>

<br>
Parker Leipzig
<li></li>
<li>xxx</li>
<li>xxx</li>

<br>
<br>
<em>Guideline 6.D Requirements: </em>
<br>
<br>
Christina Yang:
<li>conditional expressions</li>
<li>sequence unpacking</li>

<br>
Emily Isaacson
<li>inheritance</li>
<li>with statements</li>

<br>
Hannah Ziegler
<li>the ArgumentParser class</li>
<li>magic methods other than __init__()</li>

<br>
Tasfia Haque
<li>regex</li>
<li>dictionary comprehensions</li>
<li>f-strings</li>

<br>
Parker Leipzig
<li>xxx</li>
<li>xxx</li>

<br>

<b>Annotated Bibliography</b>

<em>Word game instructions by Aric Bills: https://umd.instructure.com/courses/1330825/assignments/6131269?module_item_id=11569089</em>
<li>Our group used our class Word Game assignment to understand more about how to craft a game in Python with two players when we still planned to have two real life participants</li>
<li>This program informed the way we thought about Connect Four’s functionality, main() function and how to keep track of winners and losers in our game based on counters</li>
<br>
<br>
<em>Hangman instructions by Aric Bills: https://umd.instructure.com/courses/1330825/pages/hangman</em>
<li>Our program is modeled closely off of the Hangman program we worked through during class to learn more about inheritance in terms of creating a functional game. </li>
<li>We modeled our Player parent class, HumanPlayer and ComputerPlayer off of the inheritance functionality in the Hangman program. </li>
<br>
<li>Both our program and Hangman inherit “name” from the main Player parent class and overwrite turn() methods based on the rule of the game.</li>
<li>In Hangman and our ConnectFour game, both HumanPlayer.turn() methods ask for user input to decide their move.
<ul>In Hangman, this input is a letter that is returned</ul>
<ul>In Connect Four, this input is a column number that is returned</ul>
</li>
<br>
<li>Both programs make use of a ComputerPlayer class to automate the computer’s move and give it some degree of intelligence.</li>
<li>In Hangman, the computer makes a move based on certain conditions, and the same holds true n 
Our program modeled the computer off of Hangman’s functionality by only giving it access to its power ups if there are enough pieces on the board to warrant using one. </li>
<li>This is similar to how Hangman does not let the computer guess until more than half of the letters in a word have been guessed. </li>
<li>Also similar to Hangman, our Connect Four program implements two classes for the state of the game/board and for the game’s functionality itself.</li>
<li>We modeled the organization of our game’s BoardState and Board classes off of Hangman’s Gamestate and Game classes.</li> 
<li>The organization of the two programs are similar, but we have different methods included in our BoardState class to generate a string representation of our board and initialize the dictionary that holds the game.</li>
