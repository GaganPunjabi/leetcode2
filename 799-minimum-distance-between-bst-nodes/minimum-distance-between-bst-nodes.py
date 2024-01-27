# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def predecessor(self, root):
        root = root.left
        while root and root.right:
            root = root.right
        return root

    def successor(self, root):
        root = root.right
        while root and root.left:
            root = root.left
        return root

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_value = float('inf')
        def helper(root):
            nonlocal min_value
            if not root:
                return min_value
            pred = self.predecessor(root)
            successor = self.successor(root)
            if pred and root.val - pred.val < min_value:
                min_value = root.val - pred.val
            if successor and successor.val - root.val < min_value:
                min_value = successor.val - root.val
            return min(helper(root.left), helper(root.right))
        helper(root)
        return min_value