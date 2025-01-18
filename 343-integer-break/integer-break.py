class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            else:
                dp[num] = num if num != n else 0
                for i in range(1, num):
                    res = dfs(i) * dfs(num - i)
                    dp[num] = max(res, dp[num])
            return dp[num]
        return dfs(n)