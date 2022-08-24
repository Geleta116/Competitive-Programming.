class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp =[]
        red = []
        white = []
        blue = []
        for i in range(len(nums)):
            if nums[i] == 2:
                blue.append(2)
            elif nums[i] == 1:
                white.append(1)
            elif nums[i] == 0:
                red.append(0)
        count0 = len(red)
        count1 = len(white)+count0
        count2 = len(blue)+count0+count1

        for m in range(len(nums)):
            if m<count0:
                nums[m] = 0
            elif m<count1 and m>=count0:
                nums[m] = 1
            elif m<count2 and m>= count1:
                nums[m] = 2
        



"""
THis is another way of doing it 
temp =[]
red = []
white = []
blue = []
for i in range(len(nums)):
            if nums[i] == 2:
                blue.append(2)
            elif nums[i] == 1:
                white.append(1)
            elif nums[i] == 0:
                red.append(0)
for z in range(len(red)):
            temp.append(red[z])
for l in range(len(white)):
            temp.append(white[l])
for k in range(len(blue)):
            temp.append(blue[k])
nums = temp
print(nums)
'''
