"""
    Python sudoku solver
    Takes a 2d array of integers representing a sudoku board where 0 represents
     a blank space. This text based version solves it using a depth-first-search
     and interacts only with text-streams in the terminal.
"""
class SudokuSolver: 
    def __init__(self):
        pass
    
    # Helper functions to reduce complexity of validity check
    def row_valid(self, row, col, number, board):
        # set to keep track of values
        nums = set()

        for index in range(0, 9):
            if board[index][col] in nums:
                return False
            nums.add(board[index][col])
            
        return True
    
    def col_valid(self, row, col, number, board):
        # set to keep track of values
        nums = set()

        for index in range(0, 9):
            if board[row][index] in nums:
                return False
            nums.add(board[row][index])

        return True
    
    def square_valid(self, row, col, number, board):
        # Floor the starting positions to the nearest multiple of 3
        row = row//3 * 3
        col = col//3 * 3

        nums = set()

        for i in range(0, 3):
            for j in range(0, 3):
                if board[row + i][col + j] in nums:
                    return False
                nums.add(board[row+i][col+j])
        return True
    
    # Helper function to check each sudoku validity rule
    def is_valid(self, row, col, number, board):
        if self.row_valid(row, col, number, board) and \
            self.col_valid(row, col, number, board) and \
                self.square_valid(row, col, number, board):
            return True
        
        return False
    
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
                if board[row][col] != 0:
                    break
                
                # Check all possible permutations of that board space
                #  until we find a valid state
                for num in range(1, 10):
                    if self.is_valid(row, col, num, board):
                        board[row][col] = num
                        # We found the solution board
                        if self.dfs_solve(row, col+1, board):
                            print(board)
                            return True
                        # Backtrack as a solution is impossible
                        board[row][col] = 0
                
                return False        
            # reset columns if we reach the end of a row
            col = 0
        # No board solution exists
        return True
    
    def solve_board(self, board):
        return self.dfs_solve(0, 0, board)

    def print_board(self, board):
        print("Welcome to Sudoku\n")

        for row in range(len(board)):
            print(board[row])


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


def main():
    tester = SudokuSolver()

    if tester.solve_board(sudoku_test2):
        tester.print_board(sudoku_test2)
        print("We did it")
    else:
        print("No valid solution to this sudoku")

if __name__ == "__main__":
    main()