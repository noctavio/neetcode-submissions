class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        # my pseudo code approach
        # create hash map which stores a consecutive array as the value
            # the key should be array(len(array) - 1), this key should be updated everytime we append a new value 

        # explore the rest of the array, we just need to see if the consecutive values (not contingent to the array)\
        # exist at all within it and keep updating the array and creating a new map? then use a length function on that value?
            # so if our hashmap only stores hypothetically one keyvalue pair... it's still useful for look up but seems wasteful
            # and may invalidate my approach 

        numSet = set(nums)
        longest = 0 

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest


