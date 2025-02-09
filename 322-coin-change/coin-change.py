from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mincoins = [inf] * (amount+1)
        mincoins[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if (i - c) >= 0:
                    mincoins[i] = min(mincoins[i-c] + 1, mincoins[i])
        return mincoins[-1] if mincoins[-1] < inf else -1