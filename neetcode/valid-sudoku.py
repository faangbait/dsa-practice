# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:



# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2:

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        inners = []

        for i in range(0,9):
            col = []
            for j in range(0,9):
                col += [board[j][i]]
            cols += [col]

        for i in range(0,3):
            for j in range(0,3):
                inner = []
                for k in range(0,3):
                    for l in range(0,3):
                        inner += [board[i*3+l][j*3+k]]
                inners += [inner]

        for row in board:
            if not self.validBox(row):
                return False
        for col in cols:
            if not self.validBox(col):
                return False
        for inner in inners:
            if not self.validBox(inner):
                return False
        return True
    
    def validBox(self, box: List[str]) -> bool:
        for i in range(1,10):
            if box.count(str(i)) > 1:
                return False
        return True
