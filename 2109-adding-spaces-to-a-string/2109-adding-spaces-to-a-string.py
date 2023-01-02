class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_as_a_list = []
        start = 0
        for end in spaces:
            s_as_a_list.append(s[start:end])
            start = end
        s_as_a_list.append(s[end:])
        return " ".join(s_as_a_list)        
        
        
        # # spaces.sort()
        # s_as_a_list = [char for char in s]
        # ct = 0
        # for index in spaces:
        #     s_as_a_list.insert(index+ct," ")
        #     ct+=1
        # # [s_as_a_list.insert(index," ") for index in spaces]
        # # print(s_as_a_list)
        # return "".join(s_as_a_list)