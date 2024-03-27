a,b = (int(x) for x in input().split(" "))

print("Yes"if(a%10==((b-1)%10) or a%10==((b+1)%10))else "No")
