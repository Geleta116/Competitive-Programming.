# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if (not root1 and root2) or (not root2 and root1) or (root1 and root2 and root1.val != root2.val):  
            return False
        
        if not root1 and not root2:
            return True
        
        
        right = False
        right1 = False
        left = False
        right2 =  False
        
        
        left = self.flipEquiv(root1.left, root2.right)
        left1 = self.flipEquiv(root1.left, root2.left)
        
        right = self.flipEquiv(root1.right, root2.left)
        right1 = self.flipEquiv(root1.right, root2.right)
        
        
        return (right and left) or (right1 and left1)
    
    
    
    
    
    
    
    
    
    
    
    
    