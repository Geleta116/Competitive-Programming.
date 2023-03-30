class Solution:
    def findComplement(self, num: int) -> int:
        # length = int(math.sqrt(num)) + 1
        # print(length)
        # compliment = 0
        # current = 0
        # while current < length:
        #     compliment += 2 ** current
        #     current += 1
        num2 = num
        length = 0
        while num2:
            length += 1
            num2 = num2 // 2
        compliment = 2 ** (length ) - 1
        
        
        return num ^ compliment
            
        
        
        
        
        
        
        
        
        
        
        
        
#         output = 0
#         while num :
#             temp = num & 1
#             if temp == 1:
#                 output = output * 2
#                 num = num >> 1
#             else:
#                 output = output * 2 + 1
#                 num = num >> 1
#         result = 0
        
#         while output:
#             temp = output & 1
#             if temp ==0:
#                 result *= 2
#                 output = output >> 1
#             else:
#                 result = result * 2 + 1
#                 output = output >> 1
#         return result
            
       
        