class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we have two STRING inputs s and t, we must return a boolean value
        # Are the string lengths the same? Is either empty?
            # What is an anagram? An anagram is a word that can have its letters rearranged to  
            # spell a DIFFERENT word

        # for this approach we just need to add each individual letter in string S to a hashmap, 
            # this is a linear O(n) traversal.

        # Then we traverse string `T` and if a character in T is not in S(keys), then we return false
        # If no new keys are added to the hashmap, then both strings are the same length and have the same 
        # letters therefore it is an anagram

        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)): 
            # for some letter in the string's, increment by 1, 
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1

        return sCount == tCount