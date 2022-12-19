class Solution:
    def isPalindrome(self, x: int) -> bool:
        case = ""
        store = x
        if int(x)==0:
            return True
        elif x<0:
            return False

        while x != 0:
            temp = x%10
            case += str(temp)
            x = x // 10
        print(case)
        case = int(case)
        if case == store:
            return True
        else:
            return False
