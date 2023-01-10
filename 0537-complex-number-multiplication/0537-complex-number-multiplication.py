class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        print(num1)
        print(num2)
        combined = []
        combined.append([num1[0], num2[0]])
        combined.append([num1[0], num2[1][:-1]])
        combined.append([num1[1][:-1], num2[0]])
        combined.append([num1[1][:-1], num2[1][:-1]])
        real = 0
        imaginary = 0
        print(combined)
        real += eval(str(combined[0][0]+"*"+combined[0][1]))
        print(real)
        real -= eval(str(combined[3][0]+"*"+combined[3][1]))
        
        print(real)
        real = str(real)
        imaginary +=eval(str(combined[1][0]+"*"+combined[1][1]))
        imaginary +=eval(str(combined[2][0]+"*"+combined[2][1]))
        imaginary = str(imaginary)
        return str(real+"+"+imaginary+"i")
        
        
                
        