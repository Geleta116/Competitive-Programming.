class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        store = []
        for i in range(left,right+1):
            case = 0
            temp = i
            while i:
                case = i%10
                if case == 0:
                    break
                else:
                    if temp %case != 0 :
                        break
                    elif temp%case ==0:
                        i = i//10
            if not i:
                store.append(temp)
            else:
                continue
       
        return store
                        
                        
                    
                
            
        