from typing import List
from collections import *

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	   indegree = [0 for _ in range(len(adj))]
	   order = []
	   
	   for item in range(len(adj)):
	        for each in adj[item]:
	            indegree[each] += 1
	   
	   queue =  deque()
	   
	   for item in range(len(indegree)):
	        if indegree[item] < 2:
	            queue.append(item)
	           

	   
	   while queue:
	       curr = queue.popleft()
	       
	       order.append(curr)
	       
	       for item in adj[curr]:
    	           indegree[item] -= 1
    	          
    	           if indegree[item] ==1 :
    	               queue.append(item)
    	              
	   
	   if len(order) == len(adj):
	       return False
	   return True
	   
	   
	        
	        
	        
	        
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends