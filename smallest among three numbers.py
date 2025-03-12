#smallest among three numbers
a=int(input())
b=int(input())
c=int(input())
if(a<=b and a<=c):
    print("the smallest is a")
elif(b<=a and b<=c):
    print("the smallest is b")
elif(c<=a and c<=b):
    print("the smallest is c")
elif(a==b==c):
    print("the smallest is a and b and c")
    
