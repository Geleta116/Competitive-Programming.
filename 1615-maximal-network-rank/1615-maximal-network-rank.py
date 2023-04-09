class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roads.sort()
        adjecency_list = defaultdict(set)
        
        for road in roads:
            adjecency_list[road[0]].add(road[1])
            adjecency_list[road[1]].add(road[0])
        
        maximum_rank = 0
        
        for start in range(n):
            for end in range(start + 1, n):
                current = len(adjecency_list[start]) + len(adjecency_list[end])
                if end in adjecency_list[start]:
                    current -= 1
                
           
                maximum_rank = max(maximum_rank, current)
       
        return maximum_rank
                
        
        
        