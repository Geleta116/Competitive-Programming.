class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zero_list = []
        more_list = []

        def manhattan(zeros, mores):
            x1, y1 = zeros
            x2, y2 =  mores

            return abs(x1 - x2) + abs(y1 - y2)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    zero_list.append((row, col))
                elif grid[row][col] > 1:
                    for _ in range(grid[row][col] - 1):
                        more_list.append((row, col))

        min_sofar = float("inf")
        for perm in permutations(more_list, len(zero_list)):
            distance = 0
            for i in range(len(zero_list)):
                distance += manhattan(zero_list[i], perm[i])
            min_sofar = min(min_sofar, distance)
        return min_sofar


            

        

