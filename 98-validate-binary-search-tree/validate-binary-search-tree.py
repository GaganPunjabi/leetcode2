# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            flag1, flag2 = True, True
            if root.val >= high or root.val <= low:
                return False
            if root.left:
                flag1 = helper(root.left, low, root.val)
            if root.right:
                flag2 = helper(root.right, root.val, high)
            return flag1 and flag2
        return helper(root, float('-inf'), float('inf'))