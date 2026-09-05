class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # where k is 4, The problem simply ask to return the top 4 most frequent elements in the array
        #
        count = {}
        frequency = [[] for i in range(len(nums) + 1)] 
        # this array stores elements at some index, for how frequently they occur

        for n in nums: 
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            frequency[c].append(n)

        result = []        
        for i in range(len(frequency) - 1, 0 ,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result