from collections import Counter
N = int(input())
A = [int(x) for x in input().split(" ")]
c = Counter(A)
sum = 0
for v in c.values():
    sum += v*(N-v)
    N-=v
    
print(sum)
