# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
value = input().split()

# converting to set
A = set(input().split())
B = set(input().split())

out = 0
for item in value:
    if item in A:
        out +=1
    elif item in B:
        out -=1
print(out)
