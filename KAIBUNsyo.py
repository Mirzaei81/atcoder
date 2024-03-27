from collections import Counter
import sys
N=int(input())
A=  [int(x) for  x in input().split()]
if N %2==0:
    Fhalve,SHalve = A[:N//2],A[N//2:]
else:
    Fhalve,SHalve = A[:N//2],A[N//2+1:]
if N==1:
    print("0")
    sys.exit()

def isPalindorm(x):
    l,r=0,len(x)-1
    while(l<r):
        if x[l]==x[r]:
            l+=1
            r-=1
        else:
            return False
    return x[l] == x[r]
def op(n):
    for i in range(len(A)):
        if A[i]==n:
            A[i]=n
print(Fhalve,SHalve) 
