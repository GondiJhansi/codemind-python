n=int(input())
for i in range(n):
    q=input()
    r=int(q,8)
    r=bin(r)
    print(r.replace("0b",""))