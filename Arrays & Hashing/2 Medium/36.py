"""
Leetcode 36. Determine if a 9x9 Sudoku is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.   
"""

# Resolution: Using Sets to Track Seen Numbers
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]   
    for i in range(9):
        for j in range(9):
            num = board[i][j]   
            if num != '.':
                box_index = (i // 3) * 3 + (j // 3)
                if (num in rows[i] or
                    num in cols[j] or
                    num in boxes[box_index]):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
    return True
# Time complexity: O(1), since the board size is fixed at 9x9
# Space complexity: O(1), since we are using a fixed number of sets