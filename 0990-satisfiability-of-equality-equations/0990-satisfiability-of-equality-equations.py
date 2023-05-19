class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        self.rep = defaultdict(str)
        
        for order in range(97,123):
            self.rep[chr(order)] = chr(order)
        
        def find( node):
            
            if self.rep[node] == node:
                return node
            
            parent = find(self.rep[node])
            self.rep[node] = parent
            return parent
    
    
        def union( node1, node2):
            
            rep1, rep2 = find(node1), find(node2)
            
            if rep1 <= rep2:
                self.rep[rep2] = rep1
            else:
                self.rep[rep1] = rep2
           
            
                
        
        for equation in equations:
            
            if equation[1] == "=":
                union(equation[0], equation[-1])
                
        
        for equation in equations:
            if equation[1] == "!":
                if self.rep[find(equation[0])]  == self.rep[find(equation[-1])]:
                    
                    return False
        
        return True
                
        
        