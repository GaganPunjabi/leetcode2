# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        else:
            return []
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_val = float('inf')
        lst = self.inorder(root)
        for i in range(len(lst) - 1):
            min_val = min(min_val, lst[i+1] - lst[i])
        return min_val
        