# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        RECURSIVE METHOD
        """
        insertnode = TreeNode(val)
        if not root:
            return insertnode
        elif root.val < val:
            root.right = self.insertIntoBST(root.right,val)
            return root
        elif root.val >= val:
            root.left = self.insertIntoBST(root.left,val)
            return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        ITERATIVE METHOD
        """
#         insertnode = TreeNode(val)
#         temp = root
#         if not root:
#             temp = insertnode
#         else:
#             while root:
#                 if  root.val < val:
#                     if root.right:
#                         root = root.right
#                     else:
#                         root.right = insertnode
#                         break
#                 elif root.val >= val:
#                     if root.left:
#                         root = root.left
#                     else:
#                         root.left = insertnode
#                         break
        
#         return temp
        
            
        