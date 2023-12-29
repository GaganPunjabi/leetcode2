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
        def search_in_bst(root: TreeNode, val: int) -> TreeNode:
            while root:
                if root.val > val and root.left:
                    root = root.left
                elif root.val < val and root.right:
                    root = root.right
                else:
                    return root
        node = search_in_bst(root, val)

        if val > node.val:
            node.right = TreeNode(val)
        else:
            node.left = TreeNode(val)
        return root
                