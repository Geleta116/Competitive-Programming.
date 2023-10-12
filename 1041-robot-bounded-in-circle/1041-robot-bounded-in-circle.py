class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        curr = [0,0]
        direction = 0
        for string in instructions:
            if string == "G":
                if direction == 0:
                    curr[1] += 1
                elif direction == 1:
                    curr[0] -= 1
                elif direction == 2:
                    curr[1] -= 1
                elif direction == 3:
                    curr[0] += 1
            elif string == "L":
                if direction != 3:
                    direction += 1
                else:
                    direction  = 0
            elif string == "R":
                if direction != 0 :
                    direction -= 1
                else:
                    direction = 3
        if curr[0] == 0 and curr[1] == 0:
            return True
        if direction != 0:
            return True
        return False