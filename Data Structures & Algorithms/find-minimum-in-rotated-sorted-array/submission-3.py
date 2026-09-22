class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        result = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                result = min(nums[left], result)
                break

            mid = (left + right) // 2
            result = min(nums[mid], result)
            # if the next value in an array decreases that means we fount the cut
            # the right value MUST be the minimum 

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return result