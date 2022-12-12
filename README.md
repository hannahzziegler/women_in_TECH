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

Our program is moderated through the play() method within the overarching Board class. This method involves a while loop that 

<br>
<b>Project Attribution</b>

<b>Classes/Methods/Function each group member is responsible for:</b>

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

<br>
Tasfia Haque
<li>Board generate_board() method</li>
<li>Board turn() method</li>

<br>
Parker Leipzig
<li>BoardState __str__() method</li>
<li>Parse_ags function</li>

<br>
<br>
<b>Guideline 6.D Requirements </b>

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
<li>set operations on sets or frozensets</li>
<li>comprehensions or generator expressions</li>

<br>
Tasfia Haque
<li>optional parameters</li>
<li>f-strings</li>

<br>
Parker Leipzig
<li>the ArgumentParser class</li>
<li>magic methods other than __init__()</li>

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
