class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = []
        for ops in logs:
            if ops == "../":
                if len(operations):
                    operations.pop()
            elif ops == "./":
                continue
            else:
                operations.append("file")
        return len(operations)
                
        
        