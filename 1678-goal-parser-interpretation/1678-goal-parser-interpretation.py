class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        j = 1
        out = ""
        while i<len(command):
            if command[i]=="G":
                out += "G"
                i+=1
                j+=1
            elif command[i]=="(":
                if command[j]==")":
                    out += "o"
                    i+=2
                    j +=2
                elif command[j] == "a":
                    out += "al"
                    i+=4
                    j+=4
        return out
        