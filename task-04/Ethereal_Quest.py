sum=0
count=1
lsttemp=[]
lst=[]
a=int(input())
for i in range(a):
    lsttemp=list(map(int,input().split()))
    lst.append(lsttemp)
    
for i in range(3):
    for j in range(a):
        sum+=lst[j][i]
    if sum!=0:
        count=0
    sum=0
if count==0:
    print("NO")
else:
    print("YES")