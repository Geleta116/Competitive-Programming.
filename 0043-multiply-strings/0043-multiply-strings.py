class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numss1 = 0
        numss2 = 0
        numbers = {"0":0, "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in num1:
            numss1 = numss1*10 + numbers[i]
        for i in num2:
            numss2 = numss2*10 + numbers[i]
        
        return str(numss1*numss2)
            
            
        