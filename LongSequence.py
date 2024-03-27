N = int(input())
A =[int(x) for x in input().split(" ")]
x = int(input())
ret = x//sum(A)*len(A)
reminder = x%sum(A)
acc = 0
i=0
while(acc<=reminder):
    acc+=A[i]
    i+=1
    ret+=1
print(ret)
