# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.out = 0
        stack = []
        
        stack.append(root)
        while stack:
            current = stack.pop()
            if current.val % 2 == 0:
                if current.left:
                    
                    if current.left.left:
                        self.out += current.left.left.val
                    if current.left.right:
                        self.out += current.left.right.val
                if current.right:
                    
                    if current.right.left:
                        self.out += current.right.left.val
                    if current.right.right:
                        self.out += current.right.right.val
            if current.left:
                stack.append(current.left)
            if current.right:
                    stack.append(current.right)
        return self.out
            
            
                
        