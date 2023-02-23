class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        zero = [0]*len(matrix[0])
        matrix.insert(0,zero)
        for row in matrix:
            row.insert(0,0)
        for row in range(1,len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1] + matrix[row][col] - matrix[row - 1][col - 1]
                
        
        matrix.pop(0)
        for mat in matrix:
            mat.pop(0)
        print(matrix)
        c = len(matrix[0])-1
        r = len(matrix)-1
        arr = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                pre_ind_y = min(c,col+k) 
                pre_ind_x = min(r,row+k)
                pre = matrix[pre_ind_x][pre_ind_y]
                # print(pre)  #I used this to find the last index of presum
                
                left_bottom = 0
                middle = 0
                right_top = 0
                lb = False
                rt = False
                if col - k -1>= 0:
                    left_bottom = matrix[pre_ind_x][col-k-1]
                    lb = True
                if row - k -1 >= 0:
                    right_top = matrix[row - k -1][pre_ind_y]
                    rt = True
                if rt and lb:
                    middle = matrix[row - k -1][col - k -1]
                
                item = pre - right_top - left_bottom + middle
                arr.append(item)
        count = 0
        out = []
        for row in range(len(matrix)):
            temp = []
            for col in range(len(matrix[0])):
                temp.append(arr[count])
                count +=  1
            out.append(temp)
        return out
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    