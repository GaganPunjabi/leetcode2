class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n)]
        
        dp.append(0) # We need to split last num.
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
        return dp[n]