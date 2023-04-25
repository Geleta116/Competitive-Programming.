class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.mark = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        
        
        
    def death(self, name: str) -> None:
        
        self.mark.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        
        out = []
        def dfs(current):
            if current not in self.mark:
                out.append(current)
            for child in self.graph[current]:
                dfs(child)
        
        dfs(self.kingName)
        
        
        
        
        return out
            
        
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()