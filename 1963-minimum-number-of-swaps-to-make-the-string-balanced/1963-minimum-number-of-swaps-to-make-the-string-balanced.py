class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for i in s:
            if st and i!="[":
                st.pop()
            else:
                st.append(i)
        if len(st)==len(s):
            return len(st)//2-1
        return len(st)//2
            
            
        