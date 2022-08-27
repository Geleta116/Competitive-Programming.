class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        com = []
        l = []
        if len(intervals)!= 0:
            for j in range(len(intervals)):
                l.append(intervals[j][0])
            xy = [xy for l,xy in sorted(zip(l,intervals))]
            com.append(xy[0])

            for i in xy[1:]:
                if i[0]>com[-1][1]:
                        com.append(i)
                else:
                     com[-1][1] = max(com[-1][1],i[1])

            return(com)
        else:
            return([])




'''
The below code wroks as well. It only failed 2 test cases due to exceeding time limit but it works and the error was Time limit exceeded
but it works for any input of numbers
l = []
intervals.sort()
xy = intervals

for i in range(len(xy)):
    for j in range(i,len(xy)):
        if xy[i][1]<xy[j][0]:
            continue
        elif xy[i][1]==xy[j][0]:
            xy[i]= [xy[i][0],xy[j][1]]
            xy[j]=xy[i]
        elif xy[i][1]==xy[j][1]:
            xy[j] = xy[i]
        elif xy[i][1]>xy[j][0]:
            if xy[i][1]>xy[j][1]:
                xy[j] = xy[i]
            elif xy[i][1]<xy[j][1]:
                xy[i] = [xy[i][0],xy[j][1]]
                xy[j] = xy[i]
   
        
    

y = []
for b in xy:
    while b not in y:
        y.append(b)
print(y)
    
'''
