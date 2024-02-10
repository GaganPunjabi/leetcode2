# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque()
        stack.append((root, False))
        total = 0
        while stack:
            node, flag = stack.pop()
            if node:
                if not flag:
                    stack.append((node, True))
                    stack.append((node.right, False))
                else:
                    node.val += total
                    total = node.val
                    stack.append((node.left, False))
        return root