# Minesweeper Game

## Overview

This project is a Python-based implementation of the classic **Minesweeper** game. The game allows a single player to uncover a field filled with hidden mines, based on numerical clues indicating how many mines surround each square. The goal is to clear the board without detonating any mines. 

This implementation uses abstract data types and various functions to simulate the Minesweeper experience, including the placement of mines, updating the game state, and checking for game termination conditions.

## Description of the Game

Minesweeper is a logic-based puzzle game where the objective is to clear a rectangular field of cells, some of which contain hidden mines. The player must reveal the cells without triggering the mines. Each revealed cell shows a number that indicates how many of its eight neighboring cells contain mines. 

The game is played on a grid with the following:
- **Columns** identified by uppercase letters (A to Z).
- **Rows** identified by numbers (1 to 99).
  
Each cell on the grid can be in one of three states:
1. **Covered** – The cell is not revealed.
2. **Uncovered** – The cell is revealed and shows a number indicating how many neighboring mines are present.
3. **Flagged** – The player has marked the cell as potentially containing a mine.

## Game Mechanics

- **Initial Setup**: The game starts with all cells covered, and no mines are placed until the player makes their first move. The first cell revealed by the player will never contain a mine, nor will its adjacent cells.
- **Mines Placement**: Mines are placed randomly after the first move, ensuring no mines are placed in the first revealed cell or its neighboring cells.
- **Actions**: The player can either:
  - **Clear** a cell to reveal its contents.
  - **Flag** a cell as potentially containing a mine.

### Automatic Clearing:
If a revealed cell contains no neighboring mines, its neighboring cells are automatically cleared. This continues recursively, revealing large portions of the board.

### Winning and Losing:
- The player wins by revealing all cells that do not contain mines.
- The player loses if they reveal a cell containing a mine.