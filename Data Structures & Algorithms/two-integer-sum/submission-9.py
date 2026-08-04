class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We an array of ints, at least two in the array will sum up to a `target` int
        # then return a list of the two INDICES which contain the two elements which sum to target
            # i != j in our search, these integers are unique 0,0 is not a valid answer
        # we know n + m = target
        # we can rearrange the equation such that target - n = m 
        # So we iterate through the array until eventually that condition is true, when it is
        # we have found the two integer values which sum to target
        hashmap = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in hashmap:
                return [hashmap[m], i]
            hashmap[n] = i       
            
                