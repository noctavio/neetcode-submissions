class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1

        currMax = 0

        while left < right:
            water = (right - left) * min(heights[left], heights[right])

            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            
            currMax = max(water, currMax)
        
        return currMax