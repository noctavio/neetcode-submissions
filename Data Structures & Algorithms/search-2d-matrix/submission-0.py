class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top = 0
        bot = ROWS * COLS - 1
        while top <= bot:
            mid = (top + bot) // 2
            row = mid // COLS
            col = mid % COLS
            if target > matrix[row][col]:
                top = mid + 1
            elif target < matrix[row][col]:
                bot = mid - 1
            else:
                return True
        
        return False
        