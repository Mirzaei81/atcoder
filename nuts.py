n = int(input())
trees = [int(x) for x in input().split()]
ans = 0
for nuts in trees:
    if nuts<10:
        continue
    else:
        ans+=nuts-10
print(ans)

