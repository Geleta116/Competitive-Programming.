class Solution:
    def minWindow(self, s: str, t: str) -> str:
      
        #It is impossible for len(s) to be greater that T and still return a Truthy Value
        if len(s)<len(t):
            return ""
        
        #if the length are equal and their sorted value is different return False
        elif len(s)==len(t):
            temp = s
            s = [i for i in s]
            s.sort()
            t = [j for j in t]
            t.sort()
            s= "".join(s)
            t = "".join(t)
            
            if s == t:
                
                return temp
            else:
                return ""
        else:
            left = 0
            #build sliding window to check the minimum
            shortest_substring = ""
            mini = float("inf")
            counter_t = Counter(t)
            hold = defaultdict(int)
            for right in range(len(s)):
                
                hold[s[right]] += 1
                flag = True
                for c in counter_t:
                    if counter_t[c] > hold[c]:
                        flag = False
                        break 
                # print(flag)
                if flag:
                    if mini > right - left:
                        mini = right - left
                        shortest_substring = s[left:right + 1]
                    while left <= right and flag:
                        hold[s[left]] -= 1
                        left += 1
                        for c in counter_t:
                            if counter_t[c] > hold[c]:
                                flag = False
                                break
                        
                        if flag:
                            if mini > right - left:
                                mini = right - left
                                shortest_substring = s[left:right + 1]
                            
                            
                        
            if mini == float(inf):  
                   return ""
            else:
                return shortest_substring 
                    
                
                
        
        
        
