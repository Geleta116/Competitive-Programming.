class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.out = dict()
        candidates.sort()
        def backtrack(arr,start,summ):
            
            if summ == target:
                
                self.out[tuple(arr[:])] = 1
                return

            
            
            for end in range(start, len(candidates)):
                
                if summ + candidates[end] > target:
                    return
                
                arr.append(candidates[end])
                backtrack(arr,end,summ + candidates[end])
                arr.pop()

        
        backtrack([],0,0)
        return self.out.keys()
            
            
        