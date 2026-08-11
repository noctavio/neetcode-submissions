class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a string is an anagram if it can be rearranged into a word using the same characters
            # str.length 1-10000, the list can be empty!, lowercase ENGLISH only!
        res = defaultdict(list) ##??

        for string in strs:
            count = [0] * 26 

            for c in string:
                count[ord(c) - ord("a")] += 1 

            res[tuple(count)].append(string) 
        
        return list(res.values()) ##??