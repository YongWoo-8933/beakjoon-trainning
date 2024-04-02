"""
AAA
ABBA
ABABA
ABCA
PALINDROME
1 2
1 3
1 3
0 2
0 1
"""
import sys
input()
for i in sys.stdin:
    x=i.strip()
    l=[0,1]
    n=len(x)
    for j in range((n+1)//2):
        if x[j]!=x[n-j-1]:
            print(0,j+1)
            break
    else:
        print(1,1+n//2)
        







