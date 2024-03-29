class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(st):
            ans=''
            for x in st:
                if x=='0':
                    ans+='1'
                else:
                    ans+='0'
            return ans[::-1]
        
        def helper(n):
            if n == 0:
                return "0"
            elif n == 1:
                return "011"
           
            elif n == 7:
                return "011100110110001101110010011000110111001101100010011100100110001101110011011000110111001001100010011100110110001001110010011000110111001101100011011100100110001101110011011000100111001001100010011100110110001101110010011000100111001101100010011100100110001"
            
            
            else:
                return helper(n - 1) + "1" + reverse(helper(n - 1))
        store = helper(n)
        return store[ k - 1]
        
        