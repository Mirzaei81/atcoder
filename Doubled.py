n = int(input())
count =0 
i=0
while i <= n:  
    if len(str(i))% 2==0:
        count+=1
        i+=int("1"+"0"*((len(str(i))//2)-1)+"1")
        continue
    else:
        i=int("1"+"0"*((len(str(i))//2))+"1"+"0"*((len(str(i))//2)))

print(count)
