class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        need = len(s1Count)

        for i in range(len(s2)):
            s2Count = {}
            crnt = 0
            for j in range(i, len(s2)):
                s2Count[s2[j]] = s2Count.get(s2[j],0) + 1

                if s1Count.get(s2[j], 0) < s2Count[s2[j]]:
                    break
                if s1Count.get(s2[j], 0) == s2Count[s2[j]]:
                    crnt += 1
                if crnt == need:
                    return True
        return False