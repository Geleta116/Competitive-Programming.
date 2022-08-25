nums = [1,2,3]
num_good_pair = 0
for i in range(len(nums)):
    j = 0
    while j<len(nums):
        if i<j:
            if nums[i] == nums[j]:
                num_good_par+=1
        j+=1
print(good_pair)
            
