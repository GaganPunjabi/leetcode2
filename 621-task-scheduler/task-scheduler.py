class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = collections.deque()
        counter = collections.Counter(tasks)
        heap = [-freq for freq in counter.values()]
        # Create maxheap for storing frequency.
        heapq.heapify(heap)
        cur_counter = 0
        while heap or queue:
            if queue and queue[0][1] == cur_counter:
                heapq.heappush(heap, queue.popleft()[0])
            if heap:
                freq = heapq.heappop(heap) + 1
                if freq != 0:
                    queue.append((freq, cur_counter + n + 1 ))
            cur_counter += 1
        return cur_counter