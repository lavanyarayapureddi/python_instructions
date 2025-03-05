#operators 2.0
a=24
b=5
print(a//b)


#grading system
percentage=int(input())
if percentage>=90:
    print(" grade A")
elif 70<=percentage<90:
    print("grade B")
elif 50<=percentage<70:
    print("grade C")
elif 35<=percentage<50:
    print("grade D")
else:
    print("grade E")


#basic calculator using operators
a=int(input())
operator=input()
b=int(input())
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b)
elif operator=='//':
    print(a//b)
elif operator=='**':
    print(a**b)
else:
    print("invalid operator")

#Logical operators
a=4
b=2
print(a and b)
print(a or b)
a=True
b=False
print(a and b)
print(a or b)
print(not b)
a=0
b=1
print(a and b)
print(a or b)
print(not b)
a=4
b=2
print(a>b and b<a)
print(a<b or b<a)
print(not a>b)

#bitwise operator
print(0 & 1) 
print(0 | 1)
print(True & False)
print(True | False)
print(2 & 1)




    



