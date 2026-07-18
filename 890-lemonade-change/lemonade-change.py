"""
5  -> 0
10 -> 0
20 -> 
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10 and five >= 1:
                five -= 1
                ten += 1
            elif b == 20 and ten >= 1 and five >= 1:
                ten -= 1
                five -= 1
            elif b == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True
