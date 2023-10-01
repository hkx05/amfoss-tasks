n=int(input())
lst=list(map(int,input().split()))
if lst.count(min(lst))>1:
    print("Still Aetheria")
else:
    print(lst.index(min(lst))+1)