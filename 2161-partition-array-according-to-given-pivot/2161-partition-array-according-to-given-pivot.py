class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        rearranged_Array = []
        for each_num in nums:
            if each_num< pivot:
                rearranged_Array.append(each_num)
        for each_num in nums:
            if each_num == pivot:
                rearranged_Array.append(each_num)
        for each_num in nums:
            if each_num > pivot:
                rearranged_Array.append(each_num)
        return rearranged_Array
        