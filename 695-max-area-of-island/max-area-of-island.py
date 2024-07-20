from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        rows_len = len(grid)
        cols_len = len(grid[0])
        max_area = 0
        for i in range(rows_len):
            for j in range(cols_len):
                if grid[i][j] == 1:
                    cur_area = 0
                    queue = deque()
                    queue.append((i,j))
                    while queue:
                        r,c = queue.popleft()
                        if r+1 < rows_len and grid[r+1][c] == 1 and (r+1,c) not in queue:
                            queue.append((r+1,c))
                        if c+1 < cols_len and grid[r][c+1] == 1 and (r,c+1) not in queue:
                            queue.append((r,c+1))
                        if r-1 >= 0 and grid[r-1][c] == 1 and (r-1,c) not in queue:
                            queue.append((r-1,c))
                        if c-1 >= 0 and grid[r][c-1] == 1 and (r,c-1) not in queue:
                            queue.append((r,c-1))
                        cur_area += 1
                        grid[r][c] = 0
                    max_area = max(max_area, cur_area)
        return max_area