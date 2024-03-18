"""

"""
# M,N=map(int,input().split())
# s="".join([input() for _ in range(M)])
# s=[[1,0]["BW"[i%2]==s[i]] for i in range(len(s))]
# l=[]
# for i in range(M-7):
#     for j in range(N-7):
#         S=sum([sum(s[k*N+j:k*N+j+8]) for k in range(i,i+8)])
#         l+=[S,64-S]
# print(l)
# print(min(l))
N=int(input())
l=[i+(N-5*i)//3 for i in range(N//5+1) if (N-5*i)%3==0]
print(min(l) if len(l) else -1)