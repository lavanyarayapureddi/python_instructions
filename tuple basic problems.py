#Given a tuple (5, 10, 15, 20, 25), write a program to reverse it.
t=(5,10,11,24,56)
print(t)
t=t[-1: : -1]
print(t)

#Create a function that takes a tuple of numbers and returns a tuple containing only even numbers.
t=(1,2,3,4,5,6,7,8,9)
new_tuple=()
for i in t:
    if i%2==0:
        new_tuple+=(i,)
print(new_tuple)

#Convert a nested tuple ((1,2), (3,4), (5,6)) into a flat tuple (1,2,3,4,5,6)
tuple=((1,2,3),(4,5,6),(6,7,8))
flat_tuple=()
for i in tuple:
    flat_tuple+=i
print(flat_tuple)    

        
