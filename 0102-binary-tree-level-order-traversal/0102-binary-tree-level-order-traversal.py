# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        queue = deque()
        queue.append([root,1])
        if not root:
            return []
        while queue:
            node,curr = queue.popleft()
            levels[curr].append(node.val)
            if node.left:
                queue.append([node.left,curr + 1])
            if node.right:
                queue.append([node.right,curr + 1])
                
        output = []
        for keys in levels:
            output.append(levels[keys])
        return output
                
        