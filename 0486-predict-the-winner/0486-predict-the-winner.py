class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.score = 0
        def winner(nums,s,e,turn):
            if s == e:
                return turn * nums[s]
            left = turn * nums[s] + winner(nums,s+1,e,-1 * turn)
            right = turn * nums[e] + winner(nums,s,e - 1, -1 * turn)
            return turn * max(left * turn,right * turn)
           
        store =  winner(nums,0,len(nums)-1, 1)
        if store >= 0 :
            return True
        return False
            
        