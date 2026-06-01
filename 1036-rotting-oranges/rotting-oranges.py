"""

2 1 1
1 1 0
0 1 1
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        time = 0
        ROW, COL = len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                match grid[i][j]:
                    case 1:
                        fresh += 1
                    case 2:
                        queue.append((i,j))

        # fresh = 6 queue = [(0,0)]
        # t=0: [(0,0)]
        # t=1: [(0,1), (1,0)]
        # t=2: [(0,2), (1,1)]
        # t=3: [(2,1)]
        # t=4: [(2,2)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:  
            length = len(queue)
            for _ in range(length):
                rotten = queue.popleft()
                for d in directions:
                    i, j = rotten[0] + d[0], rotten[1] + d[1]
                    if i >= 0 and i < ROW and j >= 0 and j < COL and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        queue.append((i,j))
            if queue:
                time += 1
        return time if fresh == 0 else -1