class Solution:
    def isPallindrome(self, s):
        i,j= 0, len(s) - 1
        while j > i:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def dfs(substr):
            if not substr:
                res.append(cur.copy())
            for i in range(len(substr)):
                if self.isPallindrome(substr[:i+1]):
                    cur.append(substr[:i+1])
                    dfs(substr[i+1:])
                    cur.pop()
        dfs(s)
        return res