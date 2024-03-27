N,Q=(int(x)for x in input().split())
s = list(input())
p=0
for i in range(Q):
    t,x = input().split(' ')
    t= int(t)
    x = int(x)
    if t ==1: # Perform the following x times in a row: delete the last character of S and append it to the beginning
        p+=x
    elif t==2:#Print the x-th character of S
        print(s[(x-p)%N])
        
