class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, currCombination, total):
            if total == target:
                result.append(currCombination.copy())
                return
            if idx >= len(nums) or total > target:
                return
        
            currCombination.append(nums[idx])

            includeTotal = total + nums[idx]
            dfs(idx, currCombination, includeTotal)

            currCombination.pop()
            dfs(idx + 1, currCombination, total)


        dfs(0, [], 0)
        return result