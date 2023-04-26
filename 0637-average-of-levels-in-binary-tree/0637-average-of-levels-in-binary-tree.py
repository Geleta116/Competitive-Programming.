# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        new = defaultdict(list)
        queue = deque()
        visited = set()
        visited.add(root)
        queue.append((root,0))
        while queue:
            current,level = queue.popleft()
            if current:
                new[level].append(current.val)
            
            if current.left and current.left not in visited:
                queue.append((current.left, level + 1))
            if current.right and current.right not in visited:
                queue.append((current.right, level + 1))
                
        out = []
        
        for key in new:
            out.append(sum(new[key])/len(new[key]))
            
        return out
            
        
            
            
        