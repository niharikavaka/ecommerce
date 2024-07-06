n=4  
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end = " ")
    print()   
k=n-1
for i in range(k):
    for j in range(0,i+1):
        print(end=" ")
    for j in range(k-i):
        print("*",end=" ")  
    print()            

    