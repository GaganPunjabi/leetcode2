# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        self.dfs(root)
        return self.max_path_sum

    def dfs(self, root: Optional[TreeNode]):
        left_max, right_max, root_val = float('-inf'), float('-inf'), float('-inf')
        if root:
            root_val = root.val
            if root.left:
                left_max = self.dfs(root.left)
            if root.right:
                right_max = self.dfs(root.right)
        self.max_path_sum = max(root_val, root_val + left_max, root_val + right_max, left_max + right_max + root_val, self.max_path_sum)
        node_sum = max(root_val, root_val + left_max, root_val + right_max)
        return node_sum