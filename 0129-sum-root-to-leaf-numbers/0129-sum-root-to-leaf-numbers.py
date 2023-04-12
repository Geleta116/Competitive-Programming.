# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.out = 0
        def dfs(root, arr):
            
            if not root:
                return True
            
            arr.append(str(root.val))
            
            left = False
            right =  False 
            
            
            
            left = dfs(root.left, arr)
            right = dfs(root.right, arr)
            
            if left and right:
                print(arr)
                self.out += int("".join(arr))
            arr.pop()
            
        dfs(root, [])
        return self.out