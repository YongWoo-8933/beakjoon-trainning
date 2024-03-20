"""

"""
M,N=map(int,input().split())
l=[]
for i in range(M):
    s=input()
    l+=[[1,0][(["BW","WB"][i%2])[j%2]==s[j]] for j in range(len(s))]
L=[]
for i in range(M-7):
    for j in range(N-7):
        S=sum([sum(l[k*N+j:k*N+j+8]) for k in range(i,i+8)])
        L+=[S,64-S]
print(min(L))