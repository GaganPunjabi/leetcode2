class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in num_index_map:
                return [num_index_map[target - nums[i]], i]
            num_index_map[nums[i]] = i