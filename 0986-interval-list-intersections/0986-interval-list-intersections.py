class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fp = 0
        sp = 0
        answer = []
        while fp <len(firstList) and sp<len(secondList):
            first_start, first_end = firstList[fp]
            second_start, second_end = secondList[sp]
            
            if first_start > second_end or first_end < second_start:
                if first_start >second_end:
                    sp +=1
                else:
                    fp +=1
                
            else:
                temp_sp = sp
                
                while not(first_start > second_end or first_end < second_start) and temp_sp<len(secondList):
                    answer.append([max(first_start, second_start), min(first_end, second_end)])
                    temp_sp += 1
                    if temp_sp<len(secondList):
                        second_start, second_end = secondList[temp_sp]
                fp += 1
                # sp = temp_sp
        return answer
                
        