class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        #create the suffix sum of shifts
        for shift in range(len(shifts)-2,-1,-1):
            shifts[shift] += shifts[shift + 1]
        
        #convert the string to list
        s = [char for char in s]
        
        #shift the strings 
        for index in range(len(s)):
            shifts[index] %= 26
            oldord = ord(s[index]) + shifts[index]
            if oldord > 122:
                oldord = oldord%122 + 96
            newchar = chr(oldord)
            s[index] = newchar
        
        return "".join(s)
            
        