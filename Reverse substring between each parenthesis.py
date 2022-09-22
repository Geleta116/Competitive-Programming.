class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for j in s:
            st.append(j)
        st1 = []
        st2 = []
        i = 0
        while i<len(st):
            if st[i]!=")" :
                st1.append(st[i])
                
            elif st[i]==")":
                j = len(st1)-1
                while  st1[j]!="(":
                    x = st1.pop()
                    st2.append(x)
                    j-=1
                if len(st1)!=0:
                    st1.pop()
                for m in st2:
                    st1.append(m)
                st2 = []
            i+=1
        out = ""
        for v in st1:
            out+=v
            
        return out
                
