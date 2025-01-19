class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        # Stack contains starting index from where we can take 
        # considering val to be minimum and val is the value
        stack = []
        prefix_sum = [0] # Contains sum till all prev elements
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        for i, n in enumerate(nums):
            new_index = i
            while stack and stack[-1][1] > n:
                # Pop the element for monotonous increasing stack
                start, num = stack.pop()
                new_index = start
                total = prefix_sum[i] - prefix_sum[start]
                res = max(total * num, res)
            stack.append((new_index, n))
        
        while stack:
            index, num = stack.pop()
            total = prefix_sum[-1] - prefix_sum[index]
            res = max(total * num, res)
        return res % (10**9 + 7)