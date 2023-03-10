# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.out = []
        
        def backtrack(root,arr):
            arr.append(root.val)
            if not root.left and not root.right:
                new = [str(i) for i in arr]
                self.out.append("->".join(new))
                return
           
            
            if root.left:
                backtrack(root.left,arr)
                arr.pop()
                if root.right:
                    backtrack(root.right,arr)
                    arr.pop()

            elif root.right:
                backtrack(root.right,arr)
                arr.pop()
        backtrack(root,[])
        return self.out
