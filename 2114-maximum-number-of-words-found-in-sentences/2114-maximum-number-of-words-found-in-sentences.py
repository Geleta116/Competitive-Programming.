class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        case = []
        for i in sentences:
            case.append(i.split())
        return len(max(case,key=len))