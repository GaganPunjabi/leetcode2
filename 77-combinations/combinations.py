class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(cur, k, index):
            if k == 0:
                res.append(cur.copy())
            elif index > n:
                return
            else:
                cur.append(index)
                dfs(cur, k-1, index+1)
                cur.pop()
                dfs(cur, k, index+1)
        dfs([], k, 1)
        return res