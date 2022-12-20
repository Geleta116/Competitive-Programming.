class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merg = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        if len_word1 > len_word2:
            # i = 0
            j = 0
            k = 0
            while k<len_word2:
                merg += word1[j]
                j+=1
                merg += word2[k]
                k+=1
            merg += word1[j:]
            return merg
        else:
            j = 0
            k = 0
            while j<len_word1:
                merg += word1[j]
                j+=1
                merg += word2[k]
                k+=1
                
            merg += word2[k:]
            return merg

