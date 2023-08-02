# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
            self.hasTargetSum = False
            
            self.output = []
        
            def dfs(node, runningSum, arr):

             
                if not node:
                    return

                if node.left == None and node.right == None:

                    if runningSum + node.val == targetSum:
                        arr.append(node.val)
                        self.output.append(arr[:])
                        arr.pop()
                        
                        return
                    else:
                        return
                arr.append(node.val)

                dfs(node.left, runningSum + node.val,arr)
                dfs(node.right, runningSum + node.val,arr)
                arr.pop()
                return

            dfs(root, 0 , [])

            return self.output
        