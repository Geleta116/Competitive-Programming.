import numpy
class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitted = s.split()
        max_string = max(splitted, key = lambda leng: len(leng))
        max_string_leng = len(max_string)
        store = []
        for word in splitted:
            case = []
            for char in word:
                case.append(char)
            while len(case)<max_string_leng:
                case.append(" ")
            store.append(case)
        transposed = numpy.transpose(store)
        print(transposed)
        answer = []
        for result in transposed:
            answer.append("".join(result).rstrip())
        
        return answer
        