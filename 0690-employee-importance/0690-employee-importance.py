"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adjecency_list = defaultdict( List['Employee'])
        
        for employee in employees:
            adjecency_list[employee.id] = employee
    
        
        self.total_importance = 0
        
        def dfs(employee):
            
            self.total_importance += employee.importance
            
            if employee.subordinates == []:
                return 
            
            for subordinate in employee.subordinates:
                dfs(adjecency_list[subordinate])
            
            return
        
        dfs(adjecency_list[id])
        
        return self.total_importance
            
            
            
            
            
            
            
            
            
            
            
            
            
        