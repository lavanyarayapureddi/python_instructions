#Write a program to find the second largest number in a list.
list=[9,2,572,84,432]
list.sort()
print(list)
print(list[-2])

#Rotate a list n times to the right (e.g., [1,2,3,4,5] rotated twice → [4,5,1,2,3]).
#right rotation
list=[1,2,3,4,5]
n=2
n=n%len(list)
rotate=list[-2:]+list[:-2]
print(rotate)
#left rotation
list=[5,6,7,8,9]
n=2
n=n%len(list)
rotate=list[2:]+list[:2]
print(rotate)
#Given a list of numbers, find and remove all duplicates without using set().

list=[1,2,4,3,4,3,5,4]
num=[]
for i in list:
    if i not in num:
        num.append(i)
print(num)        
