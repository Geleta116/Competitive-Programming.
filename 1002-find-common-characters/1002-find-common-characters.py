class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
       
        check = list(A[0])
        for word in A:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check
#         arr = [0] * 26
#         offset = ord('a')
#         words.sort( key = lambda x: len(x))
#         word = words[0]
#         check = []
#         for char in word:
            
#             for item in words:
#                 if char in item:
#                     asciii = ord(char)
#                     arr[asciii - offset] += 1
#         print(arr)