# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root
    
    def predecessor(self, root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        # Search node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)            
        else:
            if not root.left and not root.right:
                return None
            elif root.left:
                node = self.predecessor(root)
                root.val, node.val = node.val, root.val
                root.left = self.deleteNode(root.left, key)
            else:
                node = self.successor(root)
                root.val, node.val = node.val, root.val
                root.right = self.deleteNode(root.right, key)
        return root

                