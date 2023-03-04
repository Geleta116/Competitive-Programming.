class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def kth(row, curr):
            if row == 1:
                return 0 
            parent = kth(row - 1, (curr // 2) + curr % 2)
            if parent == 1:
                if curr % 2 == 1:
                    return 1
                return 0
            else:
                if curr % 2 == 1:
                    return 0
                return 1
        return kth(n,k)
            
            
                
        