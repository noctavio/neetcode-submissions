class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)] #what is this looping pair, zip function?

        stack = []
        for p,s in sorted(pair)[::-1]: #sort and reverse
            stack.append((target-p)/s) # what is this calculating
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #why 
                stack.pop() 
        return len(stack)