for i in range(int(input())):
    res2=input()
    wrd="amfoss"
    count=0
    for i in range(6):
        if res2[i]!=wrd[i]:
            count+=1
    print(count)