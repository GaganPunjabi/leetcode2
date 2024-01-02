# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def predecessor(self, root):
        cur = root
        cur = cur.left
        while cur.right and cur.right != root:
            cur = cur.right
        return cur

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)  
                root = root.right
            else:
                pred = self.predecessor(root)
                if pred.right != root:
                    res.append(root.val) 
                    pred.right = root
                    root = root.left
                else:
                    pred.right = None
                    root = root.right
        return res
                