#1 st model
s=input()
res = '-'.join(s)
print(res)
#output:sai:s-a-i


#2nd method
a=input()
c=0
b=""
for i in a:
    if c==len(a)-1:
        b+=i
        break
    b=b+i+"-"
    c+=1
    print(b)
    #output:sai:s-a-i
