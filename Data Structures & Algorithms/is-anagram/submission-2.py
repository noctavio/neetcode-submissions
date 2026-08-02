class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two string inputs, both are at least one char and MIGHT be the same length
            # return a boolean, stating whether they are anagrams (can be transformed to the other string)
        # same char's can appear more than once

        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        for idx in range(len(s)):
            sMap[s[idx]] = sMap.get(s[idx], 0) + 1
            tMap[t[idx]] = tMap.get(t[idx], 0) + 1
        
        for c in sMap:
            # since we filled the maps, now we just retrive with the key, 
            # if the values do not match then we return False
            if sMap[c] != tMap.get(c, 0): 
                return False

        return True