class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        result = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, len(charSet))
        return result