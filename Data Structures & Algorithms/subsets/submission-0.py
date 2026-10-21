class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all ints are uniqie
        # return all subsets in the array (ignore unique orders)

        # no duplicates allowed 

        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result