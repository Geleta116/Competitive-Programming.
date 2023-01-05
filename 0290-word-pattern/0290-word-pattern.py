class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split()) != len(pattern):
            return False
        else:
            listed_words = s.split()
            defa_word = {}
            defa_patt = {}
            for patterns in range(len(pattern)):
                if listed_words[patterns] in defa_word and defa_word[listed_words[patterns]]!= pattern[ patterns]:
                    return False
                elif pattern[patterns] in defa_patt and defa_patt[pattern[patterns]]!=listed_words[patterns]:
                    return False
                defa_word [ listed_words[patterns]] = pattern[patterns]
                defa_patt[pattern[patterns]] = listed_words[patterns]
            return True
                
                
                
               
                # if defa[pattern[patterns]]=="":
                #     defa[pattern[patterns]] = listed_words[patterns]
                # else:
                #     if defa[pattern[patterns]]!= listed_words[patterns]:
                #         return False
           
            
        
        