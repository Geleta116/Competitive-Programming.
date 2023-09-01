class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = [i for i in range(n)]  # Initially each element is its own parent
        rank = [0] * n                  # Rank array for optimization
        sum_values = [nums[i] for i in range(n)]  # Initialize sum values with the element values
        visited = set()
        # Find operation
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
                sum_values[root_x] += sum_values[root_y]
            else:
                parent[root_x] = root_y
                sum_values[root_y] += sum_values[root_x]
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1
        output = [0]
        for index in range(len(nums) - 1, -1, -1):
           
            visited.add(removeQueries[index])
            if removeQueries[index] > 0 and  removeQueries[index] - 1 in visited:
                union(removeQueries[index], removeQueries[index] - 1 )
            if removeQueries[index] < (len(nums) - 1) and  removeQueries[index] + 1 in visited:
                union(removeQueries[index], removeQueries[index] + 1 ) 
            curr = sum_values[find(removeQueries[index])]
            maxi = max(output[-1], curr)
            output.append(maxi)
        if output:
            output.pop()
        return output[::-1]
            
