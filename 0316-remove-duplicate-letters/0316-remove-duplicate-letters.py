class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s1 = []
        sett =set()
        last = {}
        for d in range(len(s)):
            last[s[d]]=d
        print(last)
        for i in range(len(s)):
            if s[i] not in sett:
                while (s1 and s1[-1]>s[i] and last[s1[-1]]>i):
                    sett.remove(s1.pop())
                s1.append(s[i])
                sett.add(s[i])
        return "".join(s1)

        