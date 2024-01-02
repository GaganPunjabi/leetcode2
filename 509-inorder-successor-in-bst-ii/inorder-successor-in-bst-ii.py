"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def parent_successor(self, root: 'Node') -> 'Optional[Node]':
        while root:
            if not root.parent:
                return None
            elif root.parent.right == root:
                root = root.parent
            else:
                return root.parent
    
    def child_successor(self, root: 'Node') -> 'Node':
        root = root.right
        while root and root.left:
            root = root.left
        return root

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            return self.child_successor(node)
        elif node.parent and node.parent.right == node:
            return self.parent_successor(node)
        else:
            return node.parent
