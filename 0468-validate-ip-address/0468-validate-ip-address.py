class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        separated_segments =  queryIP.split(".")
        print(separated_segments)
        if len(separated_segments) == 4:
                for eachSegment in separated_segments:
                    if not eachSegment :
                        return "Neither"
                    if len(eachSegment) > 3:
                        return "Neither"
                    if len(eachSegment) >= 2 and eachSegment[0] == "0":
                        return "Neither"
                    for each_char in eachSegment:
                        if 48 > ord(each_char) or  ord(each_char)  > 57:

                            return "Neither"
                    if int(eachSegment) > 255:
                        return "Neither"
                    
                return "IPv4"
            
        separated_segments =  queryIP.split(":")
        
        if len(separated_segments) == 8:
                for eachSegment in separated_segments:
                    if not eachSegment :
                        return "Neither"
                    if len(eachSegment) > 4:
                        return "Neither"
                    for each_char in eachSegment:
                        temp = ord(each_char)
                        if 48 <= temp <= 57 or 65 <= temp <= 70 or 97 <= temp <= 102:
                            continue
                        else:
                            print(each_char)
                            return "Neither"

                return "IPv6"
        else:
             return "Neither"
