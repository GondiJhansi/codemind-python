t=int(input())
for i in range(t):
    q=input()
    r=int(q,2)
    r=oct(r)
    print(r.replace("0o",""))