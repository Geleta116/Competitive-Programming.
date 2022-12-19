def swap_case(s):
    out = ""
    for index in s:
        if index.isupper():
            out += index.lower()
        else:
            out += index.upper()
    return out 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
