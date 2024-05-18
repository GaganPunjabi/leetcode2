class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        prev_lst = [[]]
        for num in nums:
            cur_lst = []
            for lst in prev_lst:
                cur_lst.append(lst)
                cur_lst.append(lst + [num])
            prev_lst = cur_lst
        return prev_lst
        