class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        y =[]
        r = []
        w = []
        b= []
        for i in range(len(nums)):
            if nums[i] == 2:
                b.append(2)
            elif nums[i] == 1:
                w.append(1)
            elif nums[i] == 0:
                r.append(0)
        count0 = len(r)
        count1 = len(w)+count0
        count2 = len(b)+count1

        for m in range(len(nums)):
            if m<count0:
                nums[m] = 0
            elif m<count1 and m>=count0:
                nums[m] = 1
            elif m<count2 and m>= count1:
                nums[m] = 2
        