lens = input().split()
len1 = int(lens[0])
len2 = int(lens[1])
arr1 = input().split()
arr1 = [int(i) for i in arr1]
arr2 = input().split()
arr2 = [int(i) for i in arr2]
fir_pr = 0
sec_pr = 0
expected = [0]*len2
while  sec_pr<len2:
      if fir_pr<len1 and arr1[fir_pr] < arr2[sec_pr]:
            fir_pr +=1
      
      else:
            expected[sec_pr] = fir_pr
            sec_pr += 1
 
print(*expected)
