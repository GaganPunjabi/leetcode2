from typing import List


class Solution:
    def isLeaf(self, vertex: int) -> bool:
        return len(self.tm[vertex]) == 1

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Create adjency matrix
        self.adj = [[] for i in range(n)]
        for parent, child in edges:
            self.adj[parent].append(child)
            self.adj[child].append(parent)
        print(self.adj)
        def dfs(cur: int, parent: int) -> int:
            time = 0
            for child in self.adj[cur]:
                if child == parent:
                    continue
                child_time = dfs(child, cur)
                if child_time or hasApple[child]:
                    time += child_time + 2
            return time
        return dfs(0, -1)