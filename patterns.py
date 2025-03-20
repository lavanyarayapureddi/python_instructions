#patterns
#solid square
n=10
for i in range(n):
    print("* "*n)
    
#solid Rhambus pattern
n=10
for i in range(n):
    print(" "*i+"* "*n)
    
#Hallow square
n=10
for i in range(n):
    if i==0 or i==n-1:
        print("* "*n)
    else:
        print("*"+"  "*(n-2)+" *")
        
# Right angle triangle
n=10
for i in range(n):
    print("* "*i)


#reverse right angle triangle
n=10
for i in range(n):
    print("* "*n)
    n-=1


#Pyramid pattern
n=5
for i in range(n):
    print(" " * (n-i) + "* " * i)

#left half pyramid
n=10
for i in range(n+1):
    print(" "*(n-i)+"*"*i)


# reverse left half pyramid
n=10
for i in range(n+1):
    print(" "*i+"*"*(n-i))

# equalateral triangle
n=10
for i in range(n+1):
    print(" "*(n-i)+"* "*i)

#  reverse equalateral triangle
n=10
for i in range(n+1):
    print(" "*(i)+"* "*(n-i))


#Hallow equalateral triangle
n=10
for i in range(n):
    if i==0:
        print(" "*(n-i)+"* "*(i+1))
    elif i==n-1:
        print(" "*(n-i-1)+"* "*(i+2))
    else:
        print(" "*(n-i-1)+"*"+"  "*(i)+" *")
#rev hallow equalateral triangle
n=10
for i in range(n):
    if i==0 or i==n-1:
        print(" "*(i+1)+"* "*(n-i))
    else:
        print(" "*i+"*"+"  "*(n-i-1)+"* ")
        
        

#rectangle star pattern
rows=4
col=6
for i in range(rows):
    print("* "*col)

#hallow rectangle star pattern
row=5
col=10
for i in range(row):
    if i==0 or i==row-1:
        print("* "*col)
    else:
        print("*"+" "*(2*col-3)+"*")
    print()        
        
# parallelogram star pattern
row=5
col=10
for i in range(row):
    print(" "*i+"*"*col)

#Basic square one pattern
n=10
for  i in range(n):
    print("1"*n)
    
     
#Basic square incrementing  pattern
n=10
for  i in range(n):
    for j in range(n):
        print(i,end='')
    print()



# basic right angle triangle number patternrows = 4
num = 1   

for i in range(1, rows + 1): 
    for j in range(i):
        print(num, end=" ")
        num += 1  
    print() 


#Basic incrementing triangle pattern
rows = 4  
col = 6  

for i in range(rows):
    print(str(col) * (rows - i)) 
    col -= 1  


    
    
    


    
    

    

