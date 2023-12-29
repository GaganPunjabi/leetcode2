# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        ptr = root
        while ptr:
            if ptr.val > val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = TreeNode(val)
                    break
            else:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = TreeNode(val)
                    break
        return root
                