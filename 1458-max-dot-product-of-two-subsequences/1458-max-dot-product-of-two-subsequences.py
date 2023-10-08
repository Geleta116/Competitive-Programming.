class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.sol = float("inf")
        @cache
        def dp(i,j):
            if i >= len(nums1) or j  >= len(nums2):
                return 0
            
            passBoth = dp(i + 1, j + 1)
            passLeft = dp(i + 1, j)
            passRight = dp(i, j + 1)
            accept = nums1[i] * nums2[j] + passBoth
            newAccept = nums1[i] * nums2[j]
            store = list()
            store.append(passBoth)
            store.append(passLeft)
            store.append(passRight)
            store.append(accept)
            store.append(newAccept)
            store.sort()
            # print(store,i,j)
            if newAccept == 0 :
                self.sol = 0
                return max(store)
            for idx in range(len(store) - 1, -1, -1):
                if store[idx] != 0:
                    return store[idx]
            return 0
        
        solution = dp(0,0)
        if solution < 0 and self.sol == 0:
            return 0
        return solution
        