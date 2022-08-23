class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        l =["1","2","3","4","5","6","7","8","9"]
        z = [None]*len(x)
        for i in x:
            y =[]
            for j in i:
                y.append(j)
            z[int(y[-1])-1] = y

        emp =""

        for m in z:
            for n in m:
                if n not in l:
                    emp +=str(n)
            emp+=" "
        return(emp[0:-1])
        
