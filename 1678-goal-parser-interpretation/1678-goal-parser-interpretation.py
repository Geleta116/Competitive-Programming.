class Solution:
    def interpret(self, command: str) -> str:
        index_1 = 0
        index_2 = 1
        out = ""
        while index_1<len(command):
            if command[index_1]=="G":
                out += "G"
                index_1+=1
                index_2+=1
            elif command[index_1]=="(":
                if command[index_2]==")":
                    out += "o"
                    index_1+=2
                    index_2 +=2
                elif command[index_2] == "a":
                    out += "al"
                    index_1+=4
                    index_2+=4
        return out
        