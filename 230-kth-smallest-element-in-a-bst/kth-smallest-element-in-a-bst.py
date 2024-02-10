# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = collections.deque()
        stack.append((root, False))
        kth_num = 0
        while stack and k > 0:
            node, flag = stack.pop()
            if node:
                if not flag:
                    stack.append((node, True))
                    stack.append((node.left, False))
                else:
                    k -= 1
                    kth_num = node.val
                    stack.append((node.right, False))
        if k == 0:
            return kth_num