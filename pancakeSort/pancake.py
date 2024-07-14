class Solution:
    def pancakeSort(self, l: List[int]) -> List[int]:
                f = 0
                h = len(l)
                sol = []
                check = True
                s = 0
                while s<len(l)-1:
                    if l[s]>=l[s+1]:
                        check = False
                        break
                    s+=1
                    
                if check==True:
                    return []
                else:
                    while f<=h-1:
                        maxi = max(l[0:h-f])
                        if l.index(maxi)== 0:
                                    sol.append(1)
                                    sol.append(maxi)
                                    new = []
                                    for i in range(maxi-1,-1,-1):
                                        new.append(l[i])
                                    for j in range(maxi-1+1,len(l)):
                                            new.append(l[j])
                                    l = new

                        else:
                                    sol.append(l.index(maxi)+1)
                                    new = []
                                    for i in range(l.index(maxi),-1,-1):
                                        new.append(l[i])
                                    for j in range(l.index(maxi)+1,len(l)):
                                            new.append(l[j])
                                    l = new
                                    new = []
                                    sol.append(maxi)
                                    for i in range(maxi-1,-1,-1):
                                        new.append(l[i])
                                    for j in range(maxi-1+1,len(l)):
                                            new.append(l[j])
                                    l = new


                        f+=1
                    
                    return sol