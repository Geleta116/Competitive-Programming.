class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def backtrack(left , right, turn):
            if left > right:
                return 0
            
            if turn == 1:
                return max(nums[left] + backtrack(left + 1 , right , 0),nums[right] + backtrack(left , right - 1 , 0 ))
            else:
                return min(-nums[left] + backtrack(left + 1 , right , 1 ), -nums[right] + backtrack(left , right - 1 , 1 ))
        case = backtrack(0, len(nums)-1 , 1)
        if case >=0:
            return True
        return False
            
            
    
            
        