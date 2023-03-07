# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or (not p and q):
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        
        else:
            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)
            return left and right
            
        