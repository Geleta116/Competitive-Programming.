class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small_len = min(strs,key = len)
        if len(strs) == 1:
            return strs[0]
        if len(small_len) == 0:
            return ""
        
        
        for index, spelling in enumerate(small_len):
            for words in strs :
                if words[index] != spelling:
                    return small_len[:index]
        return  small_len
                    
        