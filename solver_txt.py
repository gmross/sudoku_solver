"""
    Python sudoku solver
    Takes a 2d array of integers representing a sudoku board where 0 represents
     a blank space. This text based version solves it using a depth-first-search
     and interacts only with text-streams in the terminal.
"""
class SudokuSolver: 
    def __init__(self):
        pass
    
    def print_board(self, board):
        print("Welcome to Sudoku\n")

        for row in range(len(board)):
            print(board[row])
    
    # Helper function to check each sudoku validity rule
    def is_valid(self, row, col, number, board):
        # Check Row and col
        for index in range(0, 9):
            if board[index][col] == number or board[row][index] == number:
                return False
        
        # Check Box
        ## Floor the starting positions to the nearest multiple of 3
        row = row//3 * 3
        col = col//3 * 3

        for i in range(0, 3):
            for j in range(0, 3):
                if board[row + i][col + j] == number:
                    return False
        
        return True
    
    """
        Perform a depth-first search
        Look for an empty space and iterate through all possible numbers until we
         find a valid space. Backtrack if we reach a permutation that is not valid.
         Run-time Complexity: 9^m, where m is the number of empty spaces on the board
    """
    def dfs_solve(self, row, col, board):
        # iterate through the board and make solution changes in-place
        for i in range(row, len(board)):            
            for j in range(col, len(board[row])):
                # move until we find an empty cell
                if board[i][j] == 0:
                    # Check all possible permutations of that board space
                    #  until we find a valid state
                    for num in range(1, 10):
                        if self.is_valid(i, j, num, board):
                            board[i][j] = num
                            # We found the solution board
                            if self.dfs_solve(i, j+1, board):
                                #self.print_board(board)
                                return True
                            # Backtrack as a solution is impossible
                            board[i][j] = 0
                    # Backtracking failed--no valid solution
                    return False
            # reset columns if we reach the end of a row
            col = 0
        # No board solution exists
        return True
    
    def solve_board(self, board):
        return self.dfs_solve(0, 0, board)


sudoku_test1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

sudoku_test2 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_solution2 = [
    [5 , 3, 4, 6, 7, 8, 9, 1, 2],
    [6 , 7, 2, 1, 9, 5, 3, 4, 8],
    [1 , 9, 8, 3, 4, 2, 5, 6, 7],
    [8 , 5, 9, 7, 6, 1, 4, 2, 3],
    [4 , 2, 6, 8, 5, 3, 7, 9, 1],
    [7 , 1, 3, 9, 2, 4, 8, 5, 6],
    [9 , 6, 1, 5, 3, 7, 2, 8, 4],
    [2 , 8, 7, 4, 1, 9, 6, 3, 5],
    [3 , 4, 5, 2, 8, 6, 1, 7, 9]
]



def main():
    tester = SudokuSolver()

    if tester.solve_board(sudoku_test2):
        tester.print_board(sudoku_test2)
        print("We did it")
    else:
        print("No valid solution to this sudoku")

if __name__ == "__main__":
    main()
