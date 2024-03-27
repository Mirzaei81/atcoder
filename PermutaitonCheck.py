import sys

n = int(input())
a = [int(x) for x in input().split()]
for i in range(1,n+1):
    if i not in a:
        print("No")
        sys.exit()
print("Yes")
