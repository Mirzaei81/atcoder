a,b,c = (int(x) for x in input().split(" "))
l=  a//c
r = b//c
if (l==r):
    print(-1)
else:
    print(c*(l+1))
