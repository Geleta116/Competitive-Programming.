class Solution:
    def maxDepth(self, s):
        st = []
        out = 0
        for i in s:
            if i == "(":
                st.append(i)
                out = max(out,len(st))
            elif i == ")":
                st.pop()
        return out