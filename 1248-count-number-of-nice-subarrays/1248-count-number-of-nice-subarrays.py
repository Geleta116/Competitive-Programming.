class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        def atmost(k):
            out = 0
            start = 0
            odd = 0
            for end in range(len(A)):
                if A[end] % 2 != 0:
                    odd += 1
                while odd > k :
                    if A[start] % 2 != 0:
                        odd -= 1
                    start += 1
                out += end - start + 1
            return out
        return atmost(k) - atmost(k-1)
                
            
