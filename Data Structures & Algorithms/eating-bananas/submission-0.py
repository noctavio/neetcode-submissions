class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) # maximum element in this array takes O(n) to find
        result = right

        while left <= right:
            k = (left + right) // 2
            totalHours = 0

            for p in piles:
                totalHours += math.ceil(p / k)

            if totalHours <= h:
                right = k - 1
                result = min(result,k)
            else:
                left = k + 1

        return result