class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1 is the array empty? Is it sorted? Integers can be positive/negative.
        # Since any value can appear more than once my approach is 
            # sort the list, store the current value in a variable and compare it to the next
            # if cur == next then the list contains a duplicate 

        #2 O(1),O(logn),O(n), O(nlogn), O(n^2), O(2^n)
        # We now know that creating a hashmap is faster than sorting the list avg case?
        
        if not nums:
            return False 

        hashmap = {}
        for i in nums: 
            #if key(number) value(count) is 1 return True
            if i in hashmap:
                return True;
            hashmap[i] = 1

        return False

        
