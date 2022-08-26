import math
n,m,a = map(int, input().split())

x = 0
y = 0
if n % a == 0:
    x = n//a
else:
    x = n//a + 1
if m % a == 0:
    y = m//a
else:
    y = m//a+1
print(x*y)


'''
#Another solution I tried is the one below
import math
n,m,a = map(int,input().split())
 
x = n*m
b = a*a
if b != 1:
    while x>=n*m:
        s = math.sqrt(x)
        if int(s + 0.5) ** 2 == x and x%b ==0:
            break
        else:
            x+=1
print(x//b)

This works for many numbers it only failed on test 10
 '''
