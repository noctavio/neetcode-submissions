class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointer approach, the array is sorted we conituniously split the array in half
        # to search for our target value repeatedly until we've exhaused the array or our middle pointer
            # until we've exhaused the array or our middle pointer lands on our target
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target: 
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else: 
                return middle
        
        return -1



