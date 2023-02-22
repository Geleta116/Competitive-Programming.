class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        len_p = len(p)
        anagram_check = Counter(s[:len_p])
        start = 0
        end = len_p
        valid = []
        if anagram_check == count_p:
                valid.append(start)
        while end < len(s):
            if anagram_check == count_p:
                valid.append(start)
            if anagram_check[start] == 1:
                anagram_check.pop(s[start])
            else:
                anagram_check[s[start]]-=1
            if anagram_check[s[end]]:
                anagram_check[s[end]] += 1
            else:
                anagram_check[s[end]] = 1
            
                
            end += 1
            start += 1
            if end == len(s):
                if anagram_check == count_p:
                    valid.append(start)
                    break
        return list(set(valid))
                
        
        
    
            
            
        