class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        hashmap = {}

        for i, n in enumerate(nums): 
            if n in hashmap:
                return True
            hashmap[n] = i
        
        return False 

        
