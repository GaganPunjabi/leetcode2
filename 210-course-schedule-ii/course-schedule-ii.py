class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_lst = {i: [] for i in range(numCourses)}
        visited = set()
        output = []
        for pre in prerequisites:
            adj_lst[pre[0]].append(pre[1])

        def dfs(cur):
            if cur in visited:
                return False
            if cur in visited:
                return True
            for pre in adj_lst[cur]:
                visited.add(cur)
                if not dfs(pre):
                    return False
                adj_lst[cur] = []
                visited.remove(cur)
            if cur not in output:
                output.append(cur)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output