class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We have a list of integer (+/-) values, we must return a length 2 array, 
            # ex. [0,1] (first and second respective position)
            # that sum to a target value (any). 

            # The array will always contain ONE pair of values which succceeds

        # This problem appears to require two pointers, the array may or may not be sorted.
        
        hashmap = {} # key(array val) value (array index)

        # enumerate creates index, val pairs and they extract to the variables i,n 
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashmap: 
                return [hashmap[difference], i]
            hashmap[n] = i            



    
