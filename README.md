# Tic-Tac-Toe

## Overview
Tic-Tac-Toe is a simple implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns and place their marks ('X' or 'O') on a 3x3 grid. The first player to align three of their marks horizontally, vertically, or diagonally wins the game.

## Features
- Two-player game
- Simple text-based interface
- Checks for win conditions

## How to Play
1. The game starts with an empty 3x3 board.
2. Players take turns to place their marks ('X' or 'O') on the board.
3. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
4. If all nine squares are filled and no player has three marks in a row, the game is a draw.

## Code Structure
- `sum(a, b, c)`: Helper function to sum three values.
- `printBoard(xstate, ystate)`: Function to print the current state of the board.
- `checkWin(xstate, ystate)`: Function to check if there is a winner.

## Running the Game
1. Ensure you have Python installed on your machine.
2. Save the code in a file named `tictactoe.py`.
3. Open a terminal and navigate to the directory containing `tictactoe.py`.
4. Run the game using the command:
   ```bash
   python tictactoe.py
