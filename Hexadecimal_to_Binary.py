n = int(input())
for j in range(n):
    l = input()
    k =""
    for i in l:
        if(i=="0"):
            k+="0000"
        elif(i=="1"):
            k+="0001"
        elif(i=="2"):
            k+="0010"
        elif(i=="3"):
            k+="0011"
        elif(i=="4"):
            k+="0100"
        elif(i=="5"):
            k+="0101"
        elif(i=="6"):
            k+="0110"
        elif(i=="7"):
            k+="0111"
        elif(i=="8"):
            k+="1000"
        elif(i=="9"):
            k+="1001"
        elif(i=="A"):
            k+="1010"
        elif(i=="B"):
            k+="1011"
        elif(i=="C"):
            k+="1100"
        elif(i=="D"):
            k+="1101"
        elif(i=="E"):
            k+="1110"
        elif(i=="F"):
            k+="1111"
    print(k)
    