class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sink = set()
        source = set()
        
        for edge in edges:
            if edge[0] not in sink:
                source.add(edge[0])
            if edge[1] in source:
                source.remove(edge[1])
            sink.add(edge[1])
        
        source_list = []  
        for item in source:
            source_list.append(item)
        
        return source_list
            
        
        
            
            
        
        