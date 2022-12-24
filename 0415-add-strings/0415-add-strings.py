class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        intis = {'0':0, '1':1, '2':2, '3':3 , '4':4,"5":5, '6':6, '7':7, '8':8, '9':9}
        num11 = 0 
        for i in num1:
            num11 = num11 *10 + intis[i]
            
        num22 = 0 
        for i in num2:
            num22 = num22 *10 + intis[i]
        
        return str(num11 + num22)
        