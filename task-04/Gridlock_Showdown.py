for i in range(int(input())):
    str1=(input())
    str2=(input())
    str3=(input())
    if str1[0]==str1[1]==str1[2] and str1[0]!=".":
        print(str1[0])
    elif str2[0]==str2[1]==str2[2] and str2[0]!=".":
        print(str2[0])
    elif str3[0]==str3[1]==str3[2] and str3[0]!=".":
        print(str3[0])
    elif str1[0]==str2[0]==str3[0] and str1[0]!=".":
        print(str2[0])
    elif str1[1]==str2[1]==str3[1] and str1[1]!=".":
        print(str2[1])
    elif str1[2]==str2[2]==str3[2] and str1[2]!=".":
        print(str2[2])
    elif str1[0]==str2[1]==str3[2] and str1[0]!=".":
        print(str2[1])
    elif str1[2]==str2[1]==str3[0] and str1[2]!=".":
        print(str2[1])
    else:
        print("DRAW")