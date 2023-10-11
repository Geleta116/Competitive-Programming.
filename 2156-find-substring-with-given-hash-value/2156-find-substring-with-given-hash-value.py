class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        powers = [1] 
        for powIdx in range(1, k + 1):
            powers.append(powers[-1] * power)
            
        char_values = {}  
        for char in 'abcdefghijklmnopqrstuvwxyz':
            char_values[char] = ord(char) - 96

        currWindowHash = 0

        currWindowHash = 0
       
        for i in range(k):
            currWindowHash +=  (char_values[s[i]]) * (powers[i])
            
        if currWindowHash % modulo ==  hashValue:
            return s[: k]
        
        for idx in range(k, len(s)):
           
            currWindowHash +=  (char_values[s[idx]]) * (powers[k])
            currWindowHash -= char_values[s[idx - k]]
            currWindowHash  = currWindowHash // power
            
            if (currWindowHash) % modulo == hashValue:
                return s[idx - k + 1 : idx + 1]
            