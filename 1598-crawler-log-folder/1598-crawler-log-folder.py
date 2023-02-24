class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0
        for ops in logs:
            if ops == "../":
                if operations > 0:
                    operations -= 1
            elif ops == "./":
                continue
            else:
                operations += 1
        return operations
                
        
        