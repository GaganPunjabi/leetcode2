class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[-1]= 1

        for ci in range(len(coins)-1, -1, -1):
            coin = coins[ci]
            for a in range(amount, -1, -1):
                if a + coin <= amount:
                    dp[a] += dp[a+coin]
        return dp[0]