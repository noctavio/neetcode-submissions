class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # my approach, create a max heap of the stones
        stones = [-s for s in stones]
        heapq.heapify(stones)  

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        if len(stones) == 0: 
            return 0
        return abs(stones[0])



        # if only one element remains 

        # get the root and root.right (largest and 2nd largest value)
            # if they are equal pop both
            # if one stone is greater calculate 
                # greater - lesser 
                # pop both stones, insert a new stone with that value, and heapify again?