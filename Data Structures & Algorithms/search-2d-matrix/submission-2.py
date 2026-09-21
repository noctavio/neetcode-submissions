class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        left = 0
        right = ROWS * COLS - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // COLS
            col = mid % COLS
            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        
        return False
        