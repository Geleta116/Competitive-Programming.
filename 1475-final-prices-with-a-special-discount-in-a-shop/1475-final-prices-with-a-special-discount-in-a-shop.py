class Solution:
    def finalPrices(self, A):
        stack  = []
        for i,n in enumerate(A):
            while stack and A[stack[-1]]>=n:
                A[stack.pop()]-=n
            stack.append(i)
        return A
    
        