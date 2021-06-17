# Sudoku Solver

Welcome to Sudoku Solver! This repository is home to a Python3 program that solves sudoku puzzles.

## 💻 How It Works

This program uses a backtracking algorithm to solve a given sudoku board.

1. It searches the board until it finds an empty space. The program then tries to insert a number 1-9 until it finds a number that fits in the current sudoku board
2. If the number fits, it places the number on the board and moves onto the next space
3. If there are no numbers that fit in a given space, it returns to the last-filled space and tries a different number
4. If there are no previous spaces to which it can return, then there is no valid board solution

## 🔧 Requirements

This program requires Python3 to run

## 💾 How to Run

You can run this program by cloning this repository to your local machine. Either clone it using the command line or download the folder as a zip and place it in the directory of your choice.

Navigate to the directory by opening a terminal and typing

```bash
cd /path/to/sudoku_solver
```

Run the program by running the following command

```bash
python3 solver_txt.py
```

## ✏️ Changing the Sudoku Board

With the current iteration of the project, if you would like to change the sudoku board, open solver.txt in the editor of your choice and modify the variable sudoku_test2. Note that a 0 represents an empty space.

## 📈 Progress

TODO:

- [x] Design a backtracking algorithm that cycles through a sudoku board and solves it
- [x] Make a text based version of the program that solves sudoku puzzles encoded as a 2d array of integers
- [ ] Write unit tests to check different edge cases and test multiple boards
- [ ] Create a GUI frontend version of the program that visually demonstrates how the algorithm works
- [ ] Add functionality to allow users to input a starter board using a GUI frontend
