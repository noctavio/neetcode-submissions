class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks: 
            count[t] = count.get(t, 0) + 1

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()
        while queue or maxHeap:
            time += 1
            if maxHeap:
                taskCount = heapq.heappop(maxHeap) + 1
                if taskCount:
                    queue.append([taskCount, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
