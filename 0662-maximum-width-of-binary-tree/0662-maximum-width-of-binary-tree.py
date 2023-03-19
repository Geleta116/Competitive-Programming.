# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_level_column = [[root,0]]
        max_width = 0
        while current_level_column:
            max_width = max(max_width, current_level_column[-1][1] - current_level_column[0][1] + 1)
            next_level_column = []
            
            for each_node in current_level_column:
                
                if each_node[0].left:
                    next_level_column.append([each_node[0].left , each_node[1] * 2])
                if each_node[0].right:
                    next_level_column.append([each_node[0].right , each_node[1] * 2 + 1])
            current_level_column = list(next_level_column)
        return max_width
            
            
        
        