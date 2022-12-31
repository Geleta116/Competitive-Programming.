class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = 0
        for num in nums:
            if num%2==0:
                even_sum+=num
        
        for item in queries:
            prev = nums[item[1]]
            after = nums[item[1]] + item[0]
            nums[item[1]] = after
            if prev %2!=0 and after %2==0:
                even_sum+=after
                answer.append(even_sum)
            elif prev %2 == 0 and after %2 !=0:
                even_sum -= prev
                answer.append(even_sum)
            elif prev %2 != 0  and after != 0:
                answer.append(even_sum)
                
            elif prev%2 == 0 and after %2 == 0:
                even_sum += (after - prev)
                answer.append(even_sum)
        return answer
        
                
#         for i in queries:
#             even = 0
#             nums[i[1]]+= i[0]
#             for num in nums:
#                 if num%2 == 0:
#                     even += num
#             answer.append(even)
#         return answer
            
        