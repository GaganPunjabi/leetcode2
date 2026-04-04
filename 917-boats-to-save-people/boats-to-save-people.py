class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        people.sort()
        boat = 0
        while l < r:
            total_wt = people[l] + people[r]
            if total_wt > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boat += 1
        return boat + 1 if l==r else boat