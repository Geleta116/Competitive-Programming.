class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard1 = "qwertyuiopQWERTYUIOP"
        keyboard2 = "asdfghjklASDFGHJKL"
        keyboard3 = "zxcvbnmZXCVBNM"
        flag = 3
        out = []
        for word in words:
            if word[0] in keyboard1:
                flag = 0
            elif word[0] in keyboard2:
                flag = 1
            elif word[0] in keyboard3:
                flag = 2
            
            if flag == 0:
                    f1 = 1
                    fl = True
                    for i in word:
                        if i not in keyboard1:
                            f1 = False
                            break
                    if f1:
                        out.append(word)
                        
            elif flag == 1:
                    f2 = 1
                    f2 = True
                    for i in word:
                        if i not in keyboard2:
                            f2 = False
                            break
                    if f2:
                        out.append(word)
                        
            elif flag == 2:
                    f2 = 1
                    f3 = True
                    for i in word:
                        if i not in keyboard3:
                            f3 = False
                            break
                    if f3:
                        out.append(word)
            
        return out
                        
        