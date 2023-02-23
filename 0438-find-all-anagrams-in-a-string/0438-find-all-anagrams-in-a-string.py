class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        angrm_start = []
        check_dict = defaultdict(int)
        count_p = Counter(p)
        length_p = len(p)
        for right in range(len(s)):
            if right - left < length_p:
                check_dict[s[right]]+=1
            else:
                if check_dict == count_p:
                    angrm_start.append(left)
                check_dict[s[right]] += 1
                
                
                if check_dict[s[left]] == 1:
                    check_dict.pop(s[left])
                else:
                    check_dict[s[left]] -= 1
                left += 1
        if check_dict == count_p:
                    angrm_start.append(left)
        return angrm_start
                
        
        