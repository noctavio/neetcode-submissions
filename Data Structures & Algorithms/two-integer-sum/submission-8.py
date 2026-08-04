class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We an array of ints, at least two in the array will sum up to a `target` int
        for i, n in enumerate(nums): 
            for j, m in enumerate(nums): 
                if n + m == target and i != j: 
                    retList = [i,j]
                    return retList