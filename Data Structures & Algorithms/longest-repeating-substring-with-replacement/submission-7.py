class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0 
        mostFreqInWindow = 0

        for right in range(len(s)):
            # k is our budget on how many of our most seen char in the window we can increase by
            count[s[right]] = count.get(s[right], 0) + 1
            mostFreqInWindow = max(mostFreqInWindow, count[s[right]])

            while ((right - left + 1) - mostFreqInWindow) > k:
                count[s[left]] -= 1
                left += 1 # if we have no budget left move the left pointer by one  

            result = max(result, right - left + 1) # result should be updated with some currMax
        return result