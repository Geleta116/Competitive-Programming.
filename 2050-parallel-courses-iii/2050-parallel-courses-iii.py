class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        indegree = [ 0 for _ in range(1,n + 1)]
        graph = defaultdict(list)
        
        for source, dest in relations:
            graph[source].append(dest)
            indegree[dest - 1] += 1
        
   
        queue = deque()
        maxSoFar = 0
        
        for node in range(1, n + 1):
            if indegree[node - 1] == 0:
                
                queue.append(node)
        dp = [i for i in time]    
        
        output = 0
        while queue:
                curr = queue.popleft()
                
                for child in graph[curr]:
                    indegree[child -1] -= 1
                    dp[child - 1] = max(dp[child - 1], dp[curr - 1] +  time[child - 1]) 
                    if indegree[child - 1] == 0:
                        dp[child - 1] = max(dp[child - 1], dp[curr - 1] + time[child - 1]) 
                        queue.append(child)
        # print(dp)         
        return max(dp)
    
    
    
    
    