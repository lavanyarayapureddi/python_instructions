#armstrong
n=int(input())
temp=n
x=len(str(n))
res=0
for i in range(x+1):
    rem=n%10
    res=res+pow(rem,x)
    n=n//10
if(temp==res):
    print("armstrong")
else:
    print("not a armstrong")
