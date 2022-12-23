class Solution:
    def freqAlphabets(self, s: str) -> str:
            alpha = {"1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "7":"g", "8":"h", "9":"i", "10#":"j", "11#":"k", "12#":"l", "13#":"m", "14#":"n", "15#":"o", "16#":"p", "17#":"q", "18#":"r", "19#":"s", "20#":"t", "21#":"u", "22#":"v", "23#":"w", "24#":"x", "25#":"y", "26#":"z" } 
       
            out = ""
            first = 0
            end = 2
            while first<len(s):
                if end<len(s) and s[end] == "#":
                    case = s[first:end+1]
                    l = str(alpha[case])
                    out+=l
                    first = end+1
                    end = first + 2
                else:
                    case = s[first]
                    l = str(alpha[case])
                    out+=l
                    # out += str(alpha[case])
                    first += 1
                    end +=1
        
            return out
        # res=""
        # i=0
        # while i<len(s):
        #             if i+2<len(s) and s[i+2]=='#':
        #                 stri=s[i:i+3]
        #                 res=res+alpha[stri]
        #                 i=i+3
        #             else:
        #                 res=res+alpha[s[i]]
        #                 i+=1
        # return res
          

               


