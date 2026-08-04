class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We an array of ints, at least two in the array will sum up to a `target` int
        # then return a list of the two INDICES which contain the two elements which sum to target
            # i != j in our search, these integers are unique 0,0 is not a valid answer
        # we know n + m = target
        # we can rearrange the equation such that m = target - n
        # So we iterate through the array until we find m. Then we return an array
            # [hashmap[m], i] the 
        visitedMap = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in visitedMap:
                return [visitedMap[m], i] # we use m as the key to retrieve the index, and return 'n' index
            visitedMap[n] = i       
            
                