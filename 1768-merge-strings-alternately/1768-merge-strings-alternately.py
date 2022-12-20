class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merg = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        if len_word1 > len_word2:
            # i = 0
            word_1_iterator = 0
            word_2_iterator = 0
            while word_2_iterator<len_word2:
                merg += word1[word_1_iterator]
                word_1_iterator+=1
                merg += word2[word_2_iterator]
                word_2_iterator+=1
            merg += word1[word_1_iterator:]
            return merg
        else:
            word_1_iterator = 0
            word_2_iterator = 0
            while word_1_iterator<len_word1:
                merg += word1[word_1_iterator]
                word_1_iterator+=1
                merg += word2[word_2_iterator]
                word_2_iterator+=1
                
            merg += word2[word_2_iterator:]
            return merg

