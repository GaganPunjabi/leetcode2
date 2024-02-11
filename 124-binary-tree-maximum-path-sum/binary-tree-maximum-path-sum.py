# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        self.pathSum(root)
        return self.max_path_sum

    def pathSum(self, root: Optional[TreeNode]):
        left_sum, right_sum, root_val = float('-inf'), float('-inf'), float('-inf')
        if root:
            root_val = root.val
            if root.left:
                left_sum = self.pathSum(root.left)
            if root.right:
                right_sum = self.pathSum(root.right)
        self.max_path_sum = max(root_val, root_val + left_sum, root_val + right_sum, left_sum + right_sum + root_val, self.max_path_sum)
        node_sum = max(root_val, root_val + left_sum, root_val + right_sum)
        return node_sum