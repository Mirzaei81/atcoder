N = int(input())
A =[int(x) for x in input().split()]
s = N*sum([x**2 for x in A]) - sum(A)**2
print(s)
