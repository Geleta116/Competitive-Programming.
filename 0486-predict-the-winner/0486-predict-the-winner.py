class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def backtrack(left , right, turn):
            if left > right:
                return 0
            
            if turn :
                return max(nums[left] + backtrack(left + 1 , right , not turn),nums[right] + backtrack(left , right - 1 , not turn ))
            else:
                return min(-nums[left] + backtrack(left + 1 , right , not turn ), -nums[right] + backtrack(left , right - 1 , not turn))
        case = backtrack(0, len(nums)-1 , True)
        if case >=0:
            return True
        return False
            
            
    
            
        