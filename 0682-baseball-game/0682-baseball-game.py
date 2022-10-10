class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for i in operations:
            if i=='C':
                st.pop()
                
            elif i=="D" :
                p1 = st.pop()
                st.append(p1)
                st.append(2*p1)
                  
            elif i=='+':
                p2 = st.pop()
                p3 = st.pop()
                st.append(p3)
                st.append(p2)
                st.append(p2+p3)        
            else:
                st.append(int(i))
        
        return sum(st)
            
       