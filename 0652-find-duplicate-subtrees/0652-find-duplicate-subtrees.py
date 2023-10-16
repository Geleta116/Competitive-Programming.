# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.checker = defaultdict(int)
        self.output = []
        
        def dfs(node):
            if not node:
                return "None"
            
            curr = f"{node.val}, {dfs(node.left)} ,{dfs(node.right)}".strip()
            if curr in self.checker:
                self.checker[curr] += 1
                if self.checker[curr] == 2:
                    # print(curr)
                    self.output.append(node)
            else:
                 self.checker[curr] = 1
            return curr
                          
        dfs(root)
        return self.output
        