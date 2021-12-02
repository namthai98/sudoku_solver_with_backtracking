# sudoku_solver_with_backtracking
Project: Sudoku solver with backtracking
Programming language: Python
Additional module: pygame

##### How to install module pygame #####
#	pip install pygame             #
########################################

- What is sudoku ?
Sudoku is a logic-based, combinatorial number-placement puzzle. 
In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, 
and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. 
The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

- Introduction
This project build a sudoku basic game with 9x9 grid. The grid will create random.
Then user will try to guess the value of each cell.
Using backtracking algorithm to check the result.
Build GUI with pygame module in python.

- Flows:
Step 1: create 4 sudoku grid
This game will choose grid ramdomly.
In the future, we can improve this step by create a grid randomly.

Step 2: find the empty cell
Search each cell which have value = 0 (empty cell).
Search row by row and column by column.

Step 3: find the right value for empty cell
For each empty cell, we will try each number and check the rules of sudoku game.

Step 4: back tracking
When we try a new value in empty cell, there are 3 things to check the valid:
1. Check if there are duplicate number in a row
2. Check if there are duplicate number in a column
3. Check if there are duplicate number in 3x3 sub-grid

- Process:
Create a grid --> find the  --> Try each number --> Check the valid --> Output solved
                  empty cell     for empty cell                          grid