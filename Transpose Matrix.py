class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        temp = []
        len_m_item = len(matrix[0])
        cur_index = 0
        while cur_index < len_m_item:
            item = 0
            while item<len(matrix):
                temp.append(matrix[item][cur_index])
                item+=1
            out.append(temp)
            temp = []
            cur_index+=1
        return out

    
