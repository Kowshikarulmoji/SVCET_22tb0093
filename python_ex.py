#rotate the list
L = [1, 2, 3, 4, 5, 6, 7]
k = 2
L1= L[-k:] + L[:-k]
print(L1)

#odd or even using list2
n = int(input("Enter a number: "))
l = ["even", "odd"]
print(l[n % 2]) 

#code for Diamond
for i in range(0,5):
    print()
    for j in range(0,(5-i)):
        print("",end=" ")    
    for k in range(0,(2*i-1)):
            print("*",end="") 
for i in range(5,0,-1):
    print()
    for j in range(0,(5-i)):
        print("",end=" ")    
    for k in range(0,(2*i-1)):
            print("*",end="")


#code for pyramid
for i in range(0,5):
    print()
    for j in range(0,(5-i)):
        print("",end=" ")    
    for k in range(0,(2*i-1)):
            print("*",end="") 

#inverted right angle triangle
for i in range (5,0,-1):
    print()
    for k in range(0,5-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")

#Hollow square 
for i in range(0,4):
    print()
    for j in range (0,4):
        if (i==1 and (j==1 or j==2)) or (i==2 and (j==1 or j==2)):
            print(" ",end="   ")
        else:
             print("*",end="   ")

