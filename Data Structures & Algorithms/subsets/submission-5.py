class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all ints are uniqie
        # return all subsets in the array (ignore unique orders)

        # no duplicates allowed 

        result = []

        subset = []
        def dfs(idx): # index tells us what element we're currently visitng
            if idx >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[idx]) # include the int
            dfs(idx + 1)
            
            subset.pop() # skip the int
            dfs(idx + 1)

        dfs(0)
        return result