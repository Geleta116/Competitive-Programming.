class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        
        directions = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
        
        def inbound(r, c):
            return 0 <= r < len(img) and 0 <= c < len(img[0])
        
        output = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        
        for row in range(len(img)):
            for col in range(len(img[0])):
                
                curr_count = 1
                curr_sum = img[row][col]
                
                for added_row, added_col in directions:
                    new_row = row + added_row
                    new_col = col + added_col
                    
                    if inbound(new_row, new_col):
                        curr_sum += img[new_row][new_col]
                        curr_count += 1
                
                curr_avg = curr_sum // curr_count
                output[row][col] = curr_avg
        
        return output