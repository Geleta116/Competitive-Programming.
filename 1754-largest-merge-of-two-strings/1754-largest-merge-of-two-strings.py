class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        pointer_1 = 0
        pointer_2 = 0
        merge = ""
        while pointer_1<len(word1) and pointer_2<len(word2):
            
            if pointer_1 <len(word1) and pointer_2<len(word2) and word1[pointer_1:]>word2[pointer_2:]:
                merge += word1[pointer_1]
                pointer_1 +=1
            else:
                merge += word2[pointer_2]
                pointer_2 +=1
           

        if pointer_1 < len(word1):
            merge += word1[pointer_1:]
        elif pointer_2 < len(word2):
            merge += word2[pointer_2:]
                    
        return merge
            
        