class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = {}
        for l in arr:
            if l in count:
                count[l]+=1
            else:
                count[l]=1
        #I could have used the Counter function 
        temp_dic = sorted(count.keys())
        out = 0
        
        for i,n in enumerate(temp_dic):
            j = i 
            k = len(temp_dic)-1
            while j<=k:
                
                if temp_dic[j]+temp_dic[k]<target - temp_dic[i]:
                    j+=1
                elif temp_dic[j]+temp_dic[k]>target - temp_dic[i]:
                    k-=1
                else:
                    if i<j<k:
                        out += count[temp_dic[i]]*count[temp_dic[j]]*count[temp_dic[k]]
                    elif i==j<k:
                        out += (count[temp_dic[i]]*(count[temp_dic[i]]-1))//2 * count[temp_dic[k]]
                    elif i<j==k:
                        out += count[temp_dic[i]]*(count[temp_dic[j]]*(count[temp_dic[j]]-1))//2
                    else:
                        out += (count[temp_dic[i]]*(count[temp_dic[j]]-1)*(count[temp_dic[k]]-2))//6
                    j+=1
                    k-=1
        return out%(10**9 + 7)
                    
        