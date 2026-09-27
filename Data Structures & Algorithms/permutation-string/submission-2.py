class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        need = len(s1Count)

        for left in range(len(s2)):
            s2Count = {}
            crnt = 0
            for right in range(left, len(s2)):
                s2Count[s2[right]] = s2Count.get(s2[right],0) + 1
                
                if s1Count.get(s2[right], 0) < s2Count[s2[right]]:
                    break
                if s1Count.get(s2[right], 0) == s2Count[s2[right]]:
                    crnt += 1
                if crnt == need:
                    return True
        return False