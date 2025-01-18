class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis_lst = [1 for i in range(len(nums))]
        cnt_lst = [1 for i in range(len(nums))]
        
        max_lis, max_cnt = 1, 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    if lis_lst[i] < lis_lst[j] + 1:
                        lis_lst[i] = lis_lst[j] + 1
                        cnt_lst[i] = cnt_lst[j]
                    elif lis_lst[i] == lis_lst[j] + 1:
                        cnt_lst[i] += cnt_lst[j]
            
            if max_lis < lis_lst[i]:
                max_lis = lis_lst[i]
                max_cnt = cnt_lst[i]
            elif max_lis == lis_lst[i]:
                max_cnt += cnt_lst[i]
        return max_cnt