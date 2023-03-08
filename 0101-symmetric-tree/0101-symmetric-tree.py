# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arrleft = []
        arrright = []
        if root.left and root.right:
            if root.left.val != root.right.val:
                return False
        def inorderleft(root):
            if not root:
                return
            if root.left:
                inorderleft(root.left)
            elif root.right:
                arrleft.append(None)
            arrleft.append(root.val)
            if root.right:
                inorderleft(root.right)
            elif root.left:
                arrleft.append(None)
                
            return arrleft
        def inorderright(root):
            if not root:
                return
            if root.left:
                inorderright(root.left)
            elif root.right:
                arrright.append(None)
            arrright.append(root.val)
            if root.right:
                inorderright(root.right)
            elif root.left:
                arrright.append(None)
                
            return arrright
        
        inorderleft(root.left)
        inorderright(root.right)
        arrright.reverse()
        print(arrleft,arrright)
        if arrleft == arrright:
            return True
        return False
    
      