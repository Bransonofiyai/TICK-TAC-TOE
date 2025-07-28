# TICK-TAC-TOE
#Tic Tac Toe – Object-Oriented Python Implementation
Description
This is a command-line Tic Tac Toe game implemented in Python using Object-Oriented Programming (OOP) principles. It models the game using three main classes:

#Option: Represents a player’s symbol (X or O)
Table: Manages the game board
Match: Controls the game flow, turn-taking, and win/draw logic

#Features
Fully interactive terminal-based gameplay
Input validation with clear error messages
Winner and draw detection

#Clean code following OOP principles:
Encapsulation: Each class handles its own logic and data
Abstraction: Game board and logic separated from UI
Error handling: Prevents illegal moves and invalid inputs

#Game Rules
The board is a 3x3 grid.
Two players take turns placing their symbols (X or O) on the board.
The first to get 3 of their symbols in a row (horizontal, vertical, or diagonal) wins.
If the board fills up without a winner, the game ends in a draw.

#Code Overview
class Option
Represents a player's symbol, either 'X' or 'O'.

#class Table
Initializes and manages a 3x3 game board.
Validates and places moves.
Displays the current board.
Checks for a winner or full board.

#class Match
Coordinates the entire game.
Alternates turns between players.
Handles user input and game results.
