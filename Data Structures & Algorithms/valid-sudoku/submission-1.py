class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # We use integer division (round down) to find a bigSquare    
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3, c//3]): 
                    return False # If we already visited this row, column, or square
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True